import random
from .models import ModuleMeasurement
from .models import ActuatorMeasurement
from modules.models import Module


def create_module_measurement():
    humidity_min_limit = 30.0
    humidity_max_limit = 80.0
    temperature_max_limit = 39.0
    temperature_max_limit = 30.0

    t_increasing = True
    h_decreasing = True

    modules = Module.objects.all()

    for module in modules:
        last_measurement = ModuleMeasurement.objects.filter(
            module=module
        )

        if last_measurement is None:
            humidity = 60.0
            temperature = 34.0
        else:
            if last_measurement.humidity < humidity_min_limit:
                h_decreasing = False
            elif last_measurement.humidity > humidity_max_limit:
                h_decreasing = True

            if last_measurement.temperature > temperature_max_limit:
                t_increasing = False
            elif last_measurement.temperature < temperature_min_limit
                t_increasing = True

            if h_decreasing:
                humidity_decrease = random.randrange(0.001, 0.1)
                humidity = last_measurement.humidity - humidity_decrease
            else:
                humidity_increase = random.randrange(0.001, 0.1)
                humidity = last_measurement.humidity + humidity_increase

            if t_increasing:
                temperature_increase = random.randrange(0.001, 0.1)
                temperature = last_measurement.temperature + temperature_increase
            else:
                temperature_increase = random.randrange(0.001, 0.1)
                temperature = last_measurement.temperature + temperature_increase

        ModuleMeasurement.objects.create(
            temperature=temperature,
            ground_humidity=humidity
        )

def create_actuator_measurement():
    pass
