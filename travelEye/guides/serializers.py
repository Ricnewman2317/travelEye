from  rest_framework import serializers
from guides.models import PointsOfInterest, Streets

class PointsOfInterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PointsOfInterest
        fields = ('id', 'name', 'location')

class StreetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Streets
        fields = ('id','name', 'location')
