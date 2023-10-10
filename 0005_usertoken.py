# Generated by Django 4.1.7 on 2023-03-08 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yt_search', '0004_alter_songs_playlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(max_length=255, unique=True)),
                ('token', models.TextField()),
            ],
            options={
                'db_table': 'user_tokens',
            },
        ),
    ]
