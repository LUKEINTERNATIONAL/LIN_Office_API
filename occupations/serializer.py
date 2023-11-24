from rest_framework import serializers
from occupations.models import Occupations

class OccupationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Occupations
        fields = "__all__"
