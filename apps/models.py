from django.db import models

# Create your models here.
class Apps(models.Model):
    app_name = models.CharField(max_length=100)
    icon_path = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
       managed = True
       db_table = 'apps'

    def __str__(self) -> str:
        return super().__str__()