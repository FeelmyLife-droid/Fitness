# Generated by Django 3.2.7 on 2021-10-04 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.TextField()),
                ('username', models.TextField()),
                ('club_id', models.TextField()),
                ('api_url', models.TextField()),
            ],
        ),
    ]
