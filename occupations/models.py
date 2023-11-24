from django.db import models

# Create your models here.
class Occupations(models.Model):
    occupation_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
       managed = True
       db_table = 'occupations'

    def __str__(self) -> str:
        return super().__str__()
    
class OccupationUser(models.Model):
    occupation_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
       managed = True
       db_table = 'occupation_user'

    def __str__(self) -> str:
        return super().__str__()