from rest_framework import serializers
from mydashboard.models import *

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientRecord
        fields ='__all__'