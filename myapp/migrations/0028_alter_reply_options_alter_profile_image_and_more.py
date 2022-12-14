# Generated by Django 4.0.5 on 2022-07-28 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0027_alter_profile_cover_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reply',
            options={'ordering': ('-created',), 'verbose_name_plural': 'Replies'},
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(null=True, upload_to='xmedia'),
        ),
        migrations.AlterField(
            model_name='reply',
            name='body',
            field=models.TextField(max_length=10000),
        ),
    ]
