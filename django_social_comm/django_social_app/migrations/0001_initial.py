# Generated by Django 4.2.2 on 2023-07-13 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CommentStat',
            fields=[
                ('comment_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField(null=True)),
                ('drama_id', models.IntegerField(null=True)),
                ('comment_message', models.CharField(max_length=255)),
                ('active', models.BooleanField(null=True)),
                ('created_date', models.DateTimeField(null=True)),
                ('last_updated_date', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Drama',
            fields=[
                ('drama_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
                ('image_url', models.URLField(null=True)),
                ('like_count', models.IntegerField(null=True)),
                ('comment_count', models.IntegerField(null=True)),
                ('active', models.BooleanField(null=True)),
                ('created_date', models.DateTimeField(null=True)),
                ('last_updated_date', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LikeStat',
            fields=[
                ('like_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField(null=True)),
                ('drama_id', models.IntegerField(null=True)),
                ('active', models.BooleanField(null=True)),
                ('created_date', models.DateTimeField(null=True)),
                ('last_updated_date', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20)),
                ('fullname', models.CharField(max_length=50)),
                ('contact_no', models.BigIntegerField(null=True)),
                ('email', models.CharField(max_length=100)),
                ('active', models.BooleanField(null=True)),
                ('created_date', models.DateTimeField(null=True)),
                ('last_updated_date', models.DateTimeField(null=True)),
            ],
        ),
    ]
