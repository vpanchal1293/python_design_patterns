from abc import ABC, abstractmethod
import random
import time

# Base abstract class (supertype)
class Sensor(ABC):
    """Abstract base class for all sensors."""
    @abstractmethod
    def read(self) -> float:
        """Return the sensor reading as a float value."""
        pass
    @abstractmethod
    def name(self) -> str:
        """Return the sensor name."""
        pass

# Valid subclasses — follow LSP
class TemperatureSensor(Sensor):
    def read(self) -> float:
        value = 25.0 + random.uniform(-1.5, 1.5)
        return value
    def name(self) -> str:
        return "Temperature (°C)"

class HumiditySensor(Sensor):
    def read(self) -> float:
        value = 60.0 + random.uniform(-5, 5)
        return value
    def name(self) -> str:
        return "Humidity (%RH)"

class LightSensor(Sensor):
    def read(self) -> float:
        value = 300 + random.uniform(-50, 50)
        return value
    def name(self) -> str:
        return "Light (Lux)"

# LSP Violation example
class BrokenSensor(Sensor):
    """This violates LSP because it does not return a float as promised."""
    def read(self):
        print("[BrokenSensor] Error reading sensor!")
        return "ERROR"  # violates the base class contract (should return float)
    def name(self):
        return "Broken Sensor"

# Class that depends on the abstraction
class SensorReader:
    """Works with any Sensor that follows the Sensor contract."""
    def __init__(self, sensors: list[Sensor]):
        self.sensors = sensors
    def poll_all(self):
        """Read and log all sensor values (LSP in action)."""
        for sensor in self.sensors:
            value = sensor.read()
            try:
                # Reader assumes all sensors return a float (LSP contract)
                print(f"{sensor.name():<20}: {value:.2f}")
            except Exception as e:
                print(f"{sensor.name():<20}: ERROR ({e})")
        print("-" * 40)

# Demo
if __name__ == "__main__":
    # LSP-following sensors
    temp_sensor = TemperatureSensor()
    humid_sensor = HumiditySensor()
    light_sensor = LightSensor()

    # LSP-violating sensor
    broken_sensor = BrokenSensor()

    # Put them all together
    sensors = [temp_sensor, humid_sensor, light_sensor, broken_sensor]

    reader = SensorReader(sensors)

    for _ in range(2):
        reader.poll_all()
        time.sleep(1)
