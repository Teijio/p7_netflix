# Generated by Django 4.1.3 on 2022-12-06 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("videos", "0006_video_active"),
    ]

    operations = [
        migrations.CreateModel(
            name="VideoAllProxy",
            fields=[],
            options={
                "verbose_name": "All Video",
                "verbose_name_plural": "All Videos",
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("videos.video",),
        ),
    ]