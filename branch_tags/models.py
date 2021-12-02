from django.db                 import models

from users.models              import User
from postings.models           import Posting
from keywords.models           import Keyword

class UserTag(models.Model):
    name         = models.CharField(max_length=45, unique=True)
    user         = models.ManyToManyField(User, related_name='utags')
    created_at   = models.DateField(auto_now_add=True)
    updated_at   = models.DateField(auto_now=True)

    class Meta:
        db_table = 'user_tags'

class PostingTag(models.Model):
    name         = models.CharField(max_length=45, unique=True)
    posting      = models.ManyToManyField(Posting, related_name='ptags')
    keyword      = models.ForeignKey(Keyword, on_delete=models.CASCADE)
    created_at   = models.DateField(auto_now_add=True)
    updated_at   = models.DateField(auto_now=True)

    class Meta:
        db_table = 'posting_tags'