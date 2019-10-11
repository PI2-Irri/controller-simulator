from rest_framework import viewsets
from .serializers import ModuleMeasurementSerializer
from .serializers import ActuatorMeasurementSerializer
from .models import ActuatorMeasurement
from .models import ModuleMeasurement


class ActuatorMeasurementViewSet(viewsets.ModelViewSet):
    model = ActuatorMeasurement
    queryset = ActuatorMeasurement.objects.none()
    serializer_class = ActuatorMeasurementSerializer

    def get_queryset(self):
        self.queryset = self.model.objects.all()

        return self.queryset


class ModuleMeasurementViewSet(viewsets.ModelViewSet):
    model = ModuleMeasurement
    queryset = ModuleMeasurement.objects.none()
    serializer_class = ModuleMeasurementSerializer

    def get_queryset(self):
        self.queryset = self.model.objects.all()

        return self.queryset
