# Generated by Django 4.2.2 on 2023-07-17 18:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_social_app', '0004_alter_likestat_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likestat',
            name='active',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AlterField(
            model_name='likestat',
            name='created_date',
            field=models.DateTimeField(default=datetime.date(2023, 7, 17), null=True),
        ),
        migrations.AlterField(
            model_name='likestat',
            name='last_updated_date',
            field=models.DateTimeField(default=datetime.date(2023, 7, 17), null=True),
        ),
    ]