
from .models import InfoList
from rest_framework import serializers


# Serializers define the API representation.



class NullARGSSerializer(serializers.Serializer):
    pass

class HostListAPISerializer(serializers.Serializer):
    ip = serializers.CharField(label="ip", help_text='ip',required=False)

class HostListDBSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoList
        fields = '__all__'

