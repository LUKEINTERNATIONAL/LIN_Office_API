from pkg_resources import require
from rest_framework import serializers

class RegisterRequestSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    phone = serializers.CharField(max_length=200)
    district_id = serializers.CharField(max_length=200, required=False,default=0)
    birthdate = serializers.CharField(max_length=100, default='')
    occupation = serializers.CharField(max_length=100, default='')
    email = serializers.EmailField(required=False)
    username = serializers.CharField(max_length=200)
    password = serializers.CharField(max_length=200)
    validate_password = serializers.CharField(max_length=200)
    is_superuser = serializers.BooleanField()

class PatchRequestSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    phone = serializers.CharField(max_length=200)
    district_id = serializers.CharField(max_length=200,required=False,default=0)
    birthdate = serializers.CharField(max_length=100, default='')
    occupation = serializers.CharField(max_length=100, default='')
    email = serializers.EmailField(required=False)
    username = serializers.CharField(max_length=200)
    password = serializers.CharField(max_length=200, required=False)
    validate_password = serializers.CharField(max_length=200, required=False)
    is_superuser = serializers.BooleanField()


class LoginSerializers(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128)