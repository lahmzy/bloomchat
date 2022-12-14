# Generated by Django 4.0.5 on 2022-07-19 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_reply_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='slug',
            field=models.SlugField(default='', null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='mail',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='reply',
            name='slug',
            field=models.SlugField(default='', null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='slug',
            field=models.SlugField(default='', null=True),
        ),
    ]
