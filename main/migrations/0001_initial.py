# Generated by Django 4.1 on 2022-08-11 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Donor",
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
                ("Date", models.DateField()),
                ("Financial_Year", models.IntegerField()),
                (
                    "Type",
                    models.CharField(
                        choices=[("DB", "Debit"),
                                 ("CR", "Credit"), ("NA", "N/A")],
                        max_length=2,
                    ),
                ),
                ("Amount", models.IntegerField()),
                ("Cheque_Number", models.IntegerField()),
                ("From_To", models.CharField(max_length=100)),
                ("On_Account_Of", models.CharField(max_length=100)),
                ("Country", models.CharField(max_length=20)),
                ("Remarks", models.CharField(max_length=200)),
                ("Email", models.EmailField(max_length=254)),
                ("Phone_Number", models.IntegerField()),
                (
                    "Status",
                    models.CharField(
                        choices=[
                            ("RU", "Receipt Unavailable"),
                            ("RG", "Receipt Generated"),
                        ],
                        max_length=2,
                    ),
                ),
                ("Action", models.BooleanField(default=True)),
            ],
        ),
    ]
# set_donor_123