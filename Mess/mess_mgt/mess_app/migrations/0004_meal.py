# Generated by Django 4.2.4 on 2023-08-30 22:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("mess_app", "0003_rename_mail_member_email"),
    ]

    operations = [
        migrations.CreateModel(
            name="Meal",
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
                ("MealDate", models.DateField()),
                ("Deposite", models.ImageField(upload_to="")),
                (
                    "Meal",
                    models.IntegerField(
                        choices=[
                            (1, "One"),
                            (1.5, "One_half"),
                            (2, "Two"),
                            (2.5, "Two_half"),
                            (3, "Three"),
                            (3.5, "Tree_half"),
                            (4, "Four"),
                        ]
                    ),
                ),
                (
                    "member",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mess_app.member",
                    ),
                ),
            ],
        ),
    ]
