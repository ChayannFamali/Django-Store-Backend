# Generated by Django 5.1.2 on 2024-10-25 07:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0003_alter_user_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="id",
            field=models.BigIntegerField(default=1, primary_key=True, serialize=False),
        ),
    ]
