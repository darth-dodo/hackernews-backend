# Generated by Django 2.2 on 2020-04-19 16:01

import datetime

import django.db.models.deletion
import django_extensions.db.fields
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ("hn_users", "0001_initial"),
        ("links", "0002_link_posted_by"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="link",
            options={
                "get_latest_by": "modified",
                "ordering": ("-modified", "-created"),
            },
        ),
        migrations.AddField(
            model_name="link",
            name="created",
            field=django_extensions.db.fields.CreationDateTimeField(
                auto_now_add=True,
                default=datetime.datetime(2020, 4, 19, 16, 1, 53, 867014, tzinfo=utc),
                verbose_name="created",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="link",
            name="modified",
            field=django_extensions.db.fields.ModificationDateTimeField(
                auto_now=True, verbose_name="modified"
            ),
        ),
        migrations.CreateModel(
            name="Voting",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    django_extensions.db.fields.CreationDateTimeField(
                        auto_now_add=True, verbose_name="created"
                    ),
                ),
                (
                    "modified",
                    django_extensions.db.fields.ModificationDateTimeField(
                        auto_now=True, verbose_name="modified"
                    ),
                ),
                (
                    "link",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="link_votes",
                        to="links.Link",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="hn_user_votes",
                        to="hn_users.HNUser",
                    ),
                ),
            ],
            options={
                "ordering": ("-modified", "-created"),
                "get_latest_by": "modified",
                "abstract": False,
            },
        ),
    ]
