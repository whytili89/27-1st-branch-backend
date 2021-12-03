from django.db                 import models

from core.models               import TimeStampModel

class Keyword(TimeStampModel):
    name         = models.CharField(max_length=45, unique=True)

    class Meta:
        db_table = 'keywords'