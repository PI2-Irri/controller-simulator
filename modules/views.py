from rest_framework import viewsets
from .serializers import ModuleSerializer
from .models import Module


class ModuleViewSet(viewsets.ModelViewSet):
    model = Module
    queryset = Module.objects.none()
    serializer_class = ModuleSerializer

    def get_queryset(self):
        self.queryset = self.model.objects.all()

        return self.queryset
