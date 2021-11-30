from django.db                 import models

from users.models              import User
from keywords.models           import Keyword

class Posting(models.Model): 
    title         = models.CharField(max_length=100)
    sub_title     = models.CharField(max_length=200)
    content       = models.TextField()
    thumbnail     = models.URLField()
    user          = models.ForeignKey(User, on_delete=models.CASCADE)
    keyword       = models.ForeignKey(Keyword, on_delete=models.CASCADE)
    created_at    = models.DateField(auto_now_add=True)
    updated_at    = models.DateField(auto_now=True)

    class Meta:
        db_table = 'postings'

class Like(models.Model):
    user         = models.ForeignKey(User, on_delete=models.CASCADE)
    posting      = models.ForeignKey('Posting', on_delete=models.CASCADE)

    class Meta:
        db_table = 'likes'

class Comment(models.Model):
    user         = models.ForeignKey(User, on_delete=models.CASCADE)
    reply        = models.TextField()
    created_at   = models.DateField(auto_now_add=True)
    updated_at   = models.DateField(auto_now=True)

    class Meta:
        db_table = 'comments'