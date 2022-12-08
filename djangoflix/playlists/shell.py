from videos.models import Video
from playlists.models import Playlist

video_a = Video.objects.create(title="Mi title", video_id="abc123")

playlist_a = Playlist.objects.create(
    title="This is my title",
    video=video_a,
)