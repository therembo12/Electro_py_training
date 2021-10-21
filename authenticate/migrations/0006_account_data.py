# Generated by Django 3.2.7 on 2021-10-17 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0005_alter_profile_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='account_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('key', models.CharField(max_length=30)),
                ('value', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'unique_together': {('username', 'key')},
            },
        ),
    ]