from django.contrib.auth.models import User
from rest_framework import serializers, viewsets


# Serializers define the API representation.

class UserListAPISerializer(serializers.Serializer):
    username = serializers.CharField(label="username", help_text='username',required=False)

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        # fields = ['url', 'username', 'email', 'is_staff']

