from django.db import models

'''
User Details
'''


class User(models.Model):

    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20,unique=True)
    fullname = models.CharField(max_length=50)
    contact_no = models.BigIntegerField(null=True,unique=True)
    email = models.CharField(max_length=100,unique=True)
    active = models.BooleanField(null=True)
    created_date = models.DateTimeField(null=True)
    last_updated_date = models.DateTimeField(null=True)


'''
TV Show Details
'''


class Drama(models.Model):

    drama_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=255)
    image_url = models.URLField(null=True)
    like_count = models.IntegerField(null=True)
    comment_count = models.IntegerField(null=True)
    active = models.BooleanField(null=True)
    created_date = models.DateTimeField(null=True)
    last_updated_date = models.DateTimeField(null=True)


'''
Likes
'''


class LikeStat(models.Model):
    like_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(
        "User", on_delete=models.CASCADE)
    drama_id = models.ForeignKey(
        "Drama", on_delete=models.CASCADE)
    active = models.BooleanField(null=True)
    created_date = models.DateTimeField(null=True)
    last_updated_date = models.DateTimeField(null=True)


'''
Comment
'''


class CommentStat(models.Model):
    comment_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(
        "User", on_delete=models.CASCADE)
    drama_id = models.ForeignKey(
        "Drama", on_delete=models.CASCADE)
    comment_message = models.CharField(max_length=255)
    active = models.BooleanField(null=True)
    created_date = models.DateTimeField(null=True)
    last_updated_date = models.DateTimeField(null=True)
