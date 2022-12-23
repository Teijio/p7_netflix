from django.test import TestCase
from django.utils import timezone
from django.utils.text import slugify

from djangoflix.db.models import PublishStateOptions

from .models import Playlist
from videos.models import Video


class PlaylistModelTestCase(TestCase):
    def create_videos(self):
        video_a = Video.objects.create(title="Mi title1", video_id="abc1")
        video_b = Video.objects.create(title="Mi title2", video_id="abc2")
        video_c = Video.objects.create(title="Mi title3", video_id="abc3")
        self.video_a = video_a
        self.video_b = video_b
        self.video_c = video_c
        self.video_qs = Video.objects.all()

    def setUp(self):
        self.create_videos()
        self.obj_a = Playlist.objects.create(
            title="This is my title",
            video=self.video_a,
        )
        obj_b = Playlist.objects.create(
            title="This is my title",
            state=PublishStateOptions.PUBLISH,
            video=self.video_a,
        )
        # obj_b.videos.set([self.video_a, self.video_b, self.video_c])
        obj_b.videos.set(self.video_qs)
        obj_b.save()
        self.obj_b = obj_b
        # в State можно было перерадть "PU"/"DR", ноо можем забыть что это

    def test_playlist_video(self):
        self.assertEqual(self.obj_a.video, self.video_a)

    def test_playlist_video_items(self):
        count = self.obj_b.videos.all().count()
        self.assertEqual(count, 3)

    def test_playlist_video_through_model(self):
        v_qs = sorted(list(self.video_qs.values_list("id")))
        video_qs = sorted(list(self.obj_b.videos.all().values_list("id")))
        playlist_item_qs = sorted(
            list(self.obj_b.playlistitem_set.all().values_list("id"))
        )
        self.assertEqual(v_qs, video_qs, playlist_item_qs)

    def test_video_playlist_properly(self):
        ids = self.obj_a.video.get_playlists_ids()
        actual_ids = list(
            Playlist.objects.filter(video=self.video_a).values_list(
                "id", flat=True
            )
        )
        self.assertEqual(ids, actual_ids)

    # playlist_featured - Обращаемся по related_name
    def test_video_playlist(self):
        qs = self.video_a.playlist_featured.all()
        self.assertEqual(qs.count(), 2)

    def test_slug_fields(self):
        title = self.obj_a.title
        test_slug = slugify(title)
        self.assertEqual(test_slug, self.obj_a.slug)

    def test_valid_title(self):
        title = "This is my title"
        qs = Playlist.objects.filter(title=title)  # query set
        self.assertTrue(qs.exists())

    def test_created_count(self):
        qs = Playlist.objects.all()
        self.assertEqual(qs.count(), 2)

    def test_draft_case(self):
        qs = Playlist.objects.filter(state=PublishStateOptions.DRAFT)
        self.assertEqual(qs.count(), 1)

    def test_publish_case(self):
        # qs = Playlist.objects.filter(state=PublishStateOptions.PUBLISH)
        now = timezone.now()
        published_qs = Playlist.objects.filter(
            state=PublishStateOptions.PUBLISH,
            publish_timestamp__lte=now,
        )
        self.assertTrue(published_qs.exists())

    def test_publish_manager(self):
        published_qs = Playlist.objects.all().published()
        published_qs_2 = Playlist.objects.published()
        self.assertTrue(published_qs.exists())
        self.assertEqual(published_qs.count(), published_qs_2.count())
