from rest_framework import serializers
from .models import ActuatorMeasurement
from .models import ModuleMeasurement


class ActuatorMeasurementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ActuatorMeasurement
        fields = (
            'id',
            'water_consumption',
            'reservoir_level',
            'water_flow',
            'url'
        )


class ModuleMeasurementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ModuleMeasurement
        fields = (
            'id',
            'temperature',
            'ground_humidity',
            'battery_level',
            'url'
        )
