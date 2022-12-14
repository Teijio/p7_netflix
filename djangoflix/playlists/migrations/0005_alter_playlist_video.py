# Generated by Django 4.1.3 on 2022-12-08 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("videos", "0013_alter_video_video_id"),
        ("playlists", "0004_alter_playlist_video"),
    ]

    operations = [
        migrations.AlterField(
            model_name="playlist",
            name="video",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="videos.video",
            ),
        ),
    ]
