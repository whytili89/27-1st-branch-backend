from django.db                 import models

from users.models              import User
from postings.models           import Posting
from keywords.models           import Keyword
from core.models               import TimeStampModel

class UserTag(TimeStampModel):
    name       = models.CharField(max_length=45, unique=True)
    users      = models.ManyToManyField(User, related_name='user_tags')

    class Meta:
        db_table = 'user_tags'

class PostingTag(TimeStampModel):
    name       = models.CharField(max_length=45, unique=True)
    postings   = models.ManyToManyField(Posting, related_name='posting_tags')
    keyword    = models.ForeignKey(Keyword, on_delete=models.CASCADE)

    class Meta:
        db_table = 'posting_tags'