# Generated by Django 3.2.7 on 2021-10-14 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0004_profile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ('user',)},
        ),
    ]