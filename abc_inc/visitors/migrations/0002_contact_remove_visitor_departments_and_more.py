# Generated by Django 5.1.4 on 2024-12-11 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("visitors", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
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
                ("name", models.CharField(max_length=100)),
                ("department", models.CharField(max_length=100)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Available", "Available"),
                            ("Occupied", "Occupied"),
                            ("Absent", "Absent"),
                        ],
                        default="Available",
                        max_length=10,
                    ),
                ),
            ],
        ),
        migrations.RemoveField(
            model_name="visitor",
            name="departments",
        ),
        migrations.RenameField(
            model_name="visitor",
            old_name="visit_date",
            new_name="date_of_visit",
        ),
        migrations.RenameField(
            model_name="visitor",
            old_name="first_name",
            new_name="name",
        ),
        migrations.RenameField(
            model_name="visitor",
            old_name="phone_number",
            new_name="phone",
        ),
        migrations.RemoveField(
            model_name="visitor",
            name="last_name",
        ),
        migrations.AddField(
            model_name="visitor",
            name="purpose",
            field=models.TextField(default="No purpose specified"),
        ),
        migrations.DeleteModel(
            name="Department",
        ),
    ]