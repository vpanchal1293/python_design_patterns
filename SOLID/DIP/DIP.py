# Below abstraction is used to follow DIP
from abc import ABC, abstractmethod

class CommunicationInterface(ABC):
    @abstractmethod
    def write(self, data: bytes):
        pass
    @abstractmethod
    def read(self, length: int) -> bytes:
        pass

# Belwo both are low level module
import smbus2

class I2CCommunication(CommunicationInterface):
    def __init__(self, bus_id=1, address=0x48):
        self.bus = smbus2.SMBus(bus_id)
        self.address = address
    def write(self, data: bytes):
        self.bus.write_i2c_block_data(self.address, 0, list(data))
    def read(self, length: int) -> bytes:
        data = self.bus.read_i2c_block_data(self.address, 0, length)
        return bytes(data)

import serial

class UARTCommunication(CommunicationInterface):
    def __init__(self, port='/dev/ttyUSB0', baudrate=9600):
        self.ser = serial.Serial(port, baudrate)
    def write(self, data: bytes):
        self.ser.write(data)
    def read(self, length: int) -> bytes:
        return self.ser.read(length)


# Belwo is high level module
class SensorReader:
    def __init__(self, comm: CommunicationInterface):
        self.comm = comm  # Depends on abstraction, not implementation
    def get_sensor_data(self):
        self.comm.write(b'\x01')  # Send command
        data = self.comm.read(2)
        return int.from_bytes(data, 'big')

# Below is main code
# Use I2C
i2c = I2CCommunication()
sensor = SensorReader(i2c)
print(sensor.get_sensor_data())

# Use UART
uart = UARTCommunication()
sensor = SensorReader(uart)
print(sensor.get_sensor_data())
