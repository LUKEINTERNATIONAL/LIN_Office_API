from rest_framework import serializers
from holidays.models import Holidays

class HolidaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Holidays
        fields = "__all__"
