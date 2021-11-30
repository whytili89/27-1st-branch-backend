from django.db                 import models

class Keyword(models.Model):
    name         = models.CharField(max_length=45, unique=True)
    created_at   = models.DateField(auto_now_add=True)
    updated_at   = models.DateField(auto_now=True)

    class Meta:
        db_table = 'keywords'