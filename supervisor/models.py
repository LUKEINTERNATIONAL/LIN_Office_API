from django.db import models

# Create your models here.
class Supervisor(models.Model):
    supervisor_id = models.CharField(max_length=100)
    employee_id = models.BigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
       managed = True
       db_table = 'supervisor'

    def __str__(self) -> str:
        return super().__str__()