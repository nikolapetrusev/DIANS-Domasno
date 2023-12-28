# Generated by Django 4.2.6 on 2023-11-27 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="City",
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
                ("name", models.TextField()),
            ],
            options={
                "verbose_name": "Град",
                "verbose_name_plural": "Градови",
                "db_table": "city",
            },
        ),
        migrations.CreateModel(
            name="Coords",
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
                ("longitude", models.TextField()),
                ("latitude", models.TextField()),
            ],
            options={
                "verbose_name": "Координати",
                "verbose_name_plural": "Координати",
                "db_table": "coords",
            },
        ),
        migrations.CreateModel(
            name="Winery",
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
                ("name", models.TextField()),
                ("address", models.TextField()),
                ("phone", models.TextField()),
                ("work", models.TextField(blank=True, null=True)),
                (
                    "city",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="app.city",
                    ),
                ),
                (
                    "coords",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="app.coords",
                    ),
                ),
            ],
            options={
                "verbose_name": "Винарија",
                "verbose_name_plural": "Винарии",
                "db_table": "winery",
            },
        ),
    ]