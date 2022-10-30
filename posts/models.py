from email.policy import default
from pickle import TRUE
from re import L
from tokenize import blank_re
from unittest.util import _MAX_LENGTH
from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Post(models.Model):
    class Meta(object):
        db_table = 'post'

    name = models.CharField(
        'Name', blank=False, null=False, max_length=14, db_index=True, default='Anonymous'
    )
    body = models.CharField(
        'Body', blank=TRUE, null=True, max_length=140, db_index=True
    )
    image = CloudinaryField(
        'image', null =TRUE
    )

    like = models.IntegerField(default=0,blank=True)
    created_at = models.DateTimeField(
        'Created DateTime', blank=True, auto_now_add=True
    )