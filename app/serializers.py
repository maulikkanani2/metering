from .models import Metering
from rest_framework import serializers




class MeteringSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metering
        fields = ['metering_code','date','primary_value','type','apartment']