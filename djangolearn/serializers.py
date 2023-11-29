from.models import Location
from rest_framework import serializers

class  LocationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('country','timezone')

