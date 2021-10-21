# Generated by Django 3.2.7 on 2021-10-14 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
