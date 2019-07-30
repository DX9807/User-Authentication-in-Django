# Generated by Django 2.2 on 2019-07-30 03:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0002_auto_20190730_0822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='user',
            field=models.OneToOneField(on_delete='CASCADE_DELETE', related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
    ]