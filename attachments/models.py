from django.db import models

# Create your models here.
class Attachments(models.Model):
    file_name = models.CharField(max_length=100)
    file_type = models.CharField(max_length=100)
    path = models.CharField(max_length=100)
    app_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
       managed = True
       db_table = 'attachments'

    def __str__(self) -> str:
        return super().__str__()