from django.contrib import admin

from .models import VideoPublishedProxy, VideoAllProxy


@admin.register(VideoAllProxy)
class VideoAllAdmin(admin.ModelAdmin):
    list_display = ["title", "id", "state", "video_id", "is_published"]
    search_fields = ["title"]
    list_filter = ["state", "active"]
    # у юзеров не будет доступа к полям ниже (всё это будет происходить автоматически)
    # при выборе Publish или Draft
    readonly_fields = ["id", "is_published", "publish_timestamp"]

    class Meta:
        model = VideoAllProxy

    # def published(self, obj, *args, **kwargs):
    #     return obj.active
    # сделали эту функцию в классе модели, чтобы админка не была слишком объёмной


@admin.register(VideoPublishedProxy)
class VideoPublishedProxyAdmin(admin.ModelAdmin):
    list_display = ["title", "video_id"]
    search_fields = ["title"]
    # list_filter = ["video_id"]
    class Meta:
        model = VideoPublishedProxy

    def get_queryset(self, request):
        return VideoPublishedProxy.objects.filter(active=True)
