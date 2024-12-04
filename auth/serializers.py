from django.core.serializers import serialize
from rest_framework import serializers


class UserCreateSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_lenth=150)
    last_name = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, min_lenth=0)
