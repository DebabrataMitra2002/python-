# Generated by Django 4.2.6 on 2024-04-29 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_api', '0002_motion_alter_plugs_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='motion',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]