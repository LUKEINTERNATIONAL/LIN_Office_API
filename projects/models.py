from django.db import models

# Create your models here.
class Projects(models.Model):
    project_name = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
       managed = True
       db_table = 'projects'

    def __str__(self) -> str:
        return super().__str__()
    
class ProjectUser(models.Model):
    project_id= models.BigIntegerField()
    user_id = models.BigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
       managed = True
       db_table = 'project_user'

    def __str__(self) -> str:
        return super().__str__()