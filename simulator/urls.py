from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter

from modules import views as modules_views
from measurements import views as measurements_views

router = DefaultRouter()

router.register(
    r'modules', modules_views.ModuleViewSet
)
router.register(
    r'module_measurements', measurements_views.ModuleMeasurementViewSet
)
router.register(
    r'actuator_measurements', measurements_views.ActuatorMeasurementViewSet
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('', include(router.urls))
]
