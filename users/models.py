from core.models import TimeStampModel
from django.db   import models

class User(TimeStampModel):
    name          = models.CharField(max_length=45)
    nickname      = models.CharField(max_length=45)
    email         = models.EmailField(unique=True)
    password      = models.CharField(max_length=200)
    phone_number  = models.CharField(max_length=45, unique=True)
    github        = models.CharField(max_length=200, null=True)
    profile_photo = models.URLField(max_length=200, null=True)
    description   = models.TextField(null=True)
    position      = models.CharField(max_length=45, null=True)
    subscribe     = models.ManyToManyField('self', through='Subscribe', symmetrical=False)

    class Meta:
        db_table = 'users'

class Subscribe(models.Model) :
    subscribing = models.ForeignKey('User', on_delete=models.CASCADE, related_name='subscriber')
    subscriber = models.ForeignKey('User', on_delete=models.CASCADE, related_name='subscribing')
    
    class Meta:
        db_table = 'subscribe'

        constraints = [
            models.constraints.UniqueConstraint(
            fields=['subscribing', 'subscriber'], name='unique_subscribing_subscriber'
            )
        ]