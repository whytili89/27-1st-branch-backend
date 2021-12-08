from django.db                 import models
from django.db.models.deletion import CASCADE

from users.models              import User
from postings.models           import Posting
from keywords.models           import Keyword
from core.models               import TimeStampModel

class UserTag(TimeStampModel):
    name       = models.CharField(max_length=45, unique=True)
    users      = models.ManyToManyField(User, through='UsersUserTags', related_name='user_tags')

    class Meta:
        db_table = 'user_tags'

class UsersUserTags(models.Model):
    id = models.AutoField(primary_key=True)

    user      = models.ForeignKey(User, db_column='user_id', on_delete=CASCADE)
    user_tag  = models.ForeignKey('UserTag', db_column='user_tag_id', on_delete=CASCADE)

    class Meta:
        db_table = 'users_usertags'
        constraints = [
            models.constraints.UniqueConstraint(
            fields=['user', 'user_tag'], name='unique_user_user_tag'
            )
        ]

class PostingTag(TimeStampModel):
    name       = models.CharField(max_length=45, unique=True)
    postings   = models.ManyToManyField(Posting, through='PostingsPostingTags', related_name='posting_tags')
    keyword    = models.ForeignKey(Keyword, on_delete=models.CASCADE)

    class Meta:
        db_table = 'posting_tags'

class PostingsPostingTags(models.Model):
    id = models.AutoField(primary_key=True)

    posting      = models.ForeignKey(Posting, db_column='posting_id', on_delete=CASCADE)
    posting_tag  = models.ForeignKey('PostingTag', db_column='posting_tag_id', on_delete=CASCADE)

    class Meta:
        db_table = 'postings_postingtags'
        constraints = [
            models.constraints.UniqueConstraint(
            fields=['posting', 'posting_tag'], name='unique_posting_posting_tag'
            )
        ]