import json
from .models import Metering
from .serializers import MeteringSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime
from django.db import transaction
from rest_framework import status


class MeteringView(APIView):
    def get(self, request):
        metering = Metering.objects.all()
        serializer = MeteringSerializer(metering,many=True)
        return Response(serializer.data)
    
    @transaction.atomic
    def post(self, request):
        try:
            with open('app/json/unique.json') as f:
                json_data=json.load(f)
            for i in json_data:
                i['TIMESTAMP_UTC']
                date = datetime.strptime(i['TIMESTAMP_UTC'], "%Y/%m/%dZ%H:%M:%S").date()
                Metering.objects.create(
                    metering_code=i['METERING_CODE'],
                    date=date, 
                    primary_value=i['PRIMARY VALUE']
                )
            return Response({'message':'Data created successfully!!'}, status=status.HTTP_201_CREATED)    
        except Exception as e:
            return Response({'message':e}, status=status.HTTP_400_BAD_REQUEST)