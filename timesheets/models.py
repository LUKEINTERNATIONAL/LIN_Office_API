from django.db import models

# Create your models here.
class Timesheet(models.Model):
    timesheet_date = models.CharField(max_length=100)
    project_id = models.BigIntegerField()
    holiday_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    attachments_id = models.BigIntegerField()
    task = models.CharField(max_length=100,blank=True)
    description = models.CharField(max_length=100,blank=True)
    start_time = models.CharField(max_length=100,blank=True)
    end_time = models.CharField(max_length=100,blank=True)
    status = models.CharField(max_length=100,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
       managed = True
       db_table = 'timesheet'

    def __str__(self) -> str:
        return super().__str__()