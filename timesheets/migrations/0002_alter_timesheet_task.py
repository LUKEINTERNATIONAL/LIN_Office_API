# Generated by Django 4.2.7 on 2023-11-20 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timesheets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timesheet',
            name='task',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
