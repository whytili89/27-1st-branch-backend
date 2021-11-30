from django.db                 import models
from django.db.models.deletion import CASCADE

class User(models.Model):
    name          = models.CharField(max_length=45)
    nickname      = models.CharField(max_length=45)
    email         = models.EmailField(unique=True)
    password      = models.CharField(max_length=200)
    phone_number  = models.CharField(max_length=45, unique=True)
    github        = models.CharField(max_length=200, null=True)
    profile_photo = models.URLField(max_length=200, null=True)
    description   = models.TextField(null=True)
    position      = models.CharField(max_length=45, null=True)
    subscribe     = models.ForeignKey('self', on_delete=CASCADE)
    created_at    = models.DateField(auto_now_add=True)
    updated_at    = models.DateField(auto_now=True)

    class Meta:
        db_table = 'users'
