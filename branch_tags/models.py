from django.db                 import models
from django.db.models.deletion import CASCADE

from users.models              import User
from postings.models           import Posting
from keywords.models           import Keyword

class User_tag(models.Model):
    name         = models.CharField(max_length=45, unique=True)
    user         = models.ManyToManyField(User, related_name='users')
    created_at   = models.DateField(auto_now_add=True)
    updated_at   = models.DateField(auto_now=True)

    class Meta:
        db_table = 'users_tags'

class Posting_tag(models.Model):
    name         = models.CharField(max_length=45, unique=True)
    posting      = models.ManyToManyField(Posting, related_name='posts')
    keyword      = models.ForeignKey(Keyword, on_delete=CASCADE)
    created_at   = models.DateField(auto_now_add=True)
    updated_at   = models.DateField(auto_now=True)

    class Meta:
        db_table = 'postings_tags'