# Generated by Django 4.1.7 on 2023-03-31 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=200)),
                ('time', models.CharField(max_length=10)),
                ('comments', models.IntegerField(max_length=7)),
                ('likes', models.IntegerField(max_length=7)),
            ],
            options={
                'verbose_name': 'audio',
                'verbose_name_plural': 'audios',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('author', models.CharField(max_length=50)),
                ('comments', models.IntegerField(max_length=7)),
                ('likes', models.IntegerField(max_length=7)),
            ],
            options={
                'verbose_name': 'post',
                'verbose_name_plural': 'posts',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('comments', models.IntegerField(max_length=7)),
                ('likes', models.IntegerField(max_length=7)),
            ],
            options={
                'verbose_name': 'video',
                'verbose_name_plural': 'videos',
            },
        ),
    ]
