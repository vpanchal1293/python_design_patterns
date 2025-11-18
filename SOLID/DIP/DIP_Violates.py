# Below is low level module
import smbus2  # I2C library

class SensorReader:
    def __init__(self):
        self.bus = smbus2.SMBus(1)
        self.address = 0x48

    def read_data(self):
        return self.bus.read_byte_data(self.address, 0)


# Below is considered as high level module
sensor = SensorReader()
sensor.read_data()

# Now if UART is added then it will create problem 
