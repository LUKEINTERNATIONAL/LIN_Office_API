from django.db import models

# Create your models here.
class Holidays(models.Model):
    holiday_name = models.CharField(max_length=100,blank=True)
    max_days = models.BigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
       managed = True
       db_table = 'holidays'

    def __str__(self) -> str:
        return super().__str__()