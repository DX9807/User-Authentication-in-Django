# Generated by Django 2.2 on 2019-07-30 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='portfolio_site',
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='mobile',
            field=models.IntegerField(blank=True, default=9807045302),
            preserve_default=False,
        ),
    ]
