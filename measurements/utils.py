import random
from .models import ModuleMeasurement
from .models import ActuatorMeasurement
from modules.models import Module


def create_module_measurement():
    humidity_min_limit = 30.0
    humidity_max_limit = 80.0
    temperature_max_limit = 39.0
    temperature_max_limit = 30.0
    battery_level = 5

    t_increasing = True
    h_decreasing = True

    modules = Module.objects.all()

    for module in modules:
        last_measurement = ModuleMeasurement.objects.filter(
            module=module
        ).last()

        if last_measurement is None:
            humidity = 60.0
            temperature = 34.0
        else:
            if last_measurement.ground_humidity < humidity_min_limit:
                h_decreasing = False
            elif last_measurement.ground_humidity >= humidity_max_limit:
                h_decreasing = True
            else:
                h_decreasing = h_decreasing

            if last_measurement.temperature > temperature_max_limit:
                t_increasing = False
            elif last_measurement.temperature <= temperature_min_limit:
                t_increasing = True
            else:
                t_increasing = t_increasing

            if h_decreasing:
                humidity_decrease = random.random()
                humidity = last_measurement.ground_humidity - humidity_decrease
            else:
                humidity_increase = random.random()
                humidity = last_measurement.ground_humidity + humidity_increase

            if t_increasing:
                temperature_increase = random.random()
                temperature = last_measurement.temperature + temperature_increase
            else:
                temperature_increase = random.random()
                temperature = last_measurement.temperature - temperature_increase


        measurement = ModuleMeasurement.objects.create(
            temperature=temperature,
            ground_humidity=humidity,
            battery_level=battery_level,
            module=module
        )
        print(measurement)


def create_actuator_measurement():
    pass
