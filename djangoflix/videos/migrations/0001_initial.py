# Generated by Django 4.1.3 on 2022-12-04 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Video",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=220)),
                ("description", models.TextField(blank=True, null=True)),
                ("slug", models.SlugField(blank=True, null=True)),
                ("video_id", models.CharField(max_length=220)),
            ],
        ),
    ]
