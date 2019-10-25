import random
from .models import ModuleMeasurement
from .models import ActuatorMeasurement
from modules.models import Module


def create_module_measurement():
    humidity_min_limit = 30.0
    humidity_max_limit = 80.0
    temperature_min_limit = 30.0
    temperature_max_limit = 39.0
    battery_level = 5

    t_increasing = True
    h_decreasing = True

    modules = Module.objects.all()

    for module in modules:
        last_measurement = ModuleMeasurement.objects.filter(
            module=module
        ).last()

        if not last_measurement:
            humidity = 60.0
            temperature = 34.0
        else:
            if last_measurement.ground_humidity < humidity_min_limit:
                h_decreasing = False
            elif last_measurement.ground_humidity > humidity_max_limit:
                h_decreasing = True

            if last_measurement.temperature > temperature_max_limit:
                t_increasing = False
            elif last_measurement.temperature <= temperature_min_limit:
                t_increasing = True

            if h_decreasing:
                humidity_decrease = round(random.random())
                humidity = last_measurement.ground_humidity - humidity_decrease
            else:
                humidity_increase = round(random.random())
                humidity = last_measurement.ground_humidity + humidity_increase

            if t_increasing:
                temperature_increase = random.random()
                temperature = last_measurement.temperature + temperature_increase
            else:
                temperature_decrease = random.random()
                temperature = last_measurement.temperature - temperature_decrease

        measurement = ModuleMeasurement.objects.create(
            temperature=temperature,
            ground_humidity=humidity,
            battery_level=battery_level,
            module=module
        )


def create_actuator_measurement():
    
    water_consumption = float(random.randint(10,45))
    reservoir_level = random.randint(10,45)
    water_flow = 2

    actuator = ActuatorMeasurement.objects.create(
        water_consumption=water_consumption,
        reservoir_level=reservoir_level,
        water_flow=water_flow
    )