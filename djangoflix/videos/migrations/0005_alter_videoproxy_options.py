# Generated by Django 4.1.3 on 2022-12-06 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("videos", "0004_videoproxy"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="videoproxy",
            options={
                "verbose_name": "Published Video",
                "verbose_name_plural": "Published Videos",
            },
        ),
    ]