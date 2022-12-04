from django.db import models

class Video(models.Model):
    title = models.CharField() # name
    description = models.TextField()
    slug = models.SlugField(blank=True, null=True) # this is my video
    video_id = models.CharField()
    # timestamp
    # updated
    # state
    # publish_timestamp
