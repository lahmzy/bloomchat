# Generated by Django 4.0.5 on 2022-07-29 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0029_latest'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='latest',
            options={'ordering': ('-created',)},
        ),
    ]