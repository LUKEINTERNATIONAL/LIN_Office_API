from rest_framework import serializers
from timesheets.models import Timesheet

class TimesheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timesheet
        fields = "__all__"
