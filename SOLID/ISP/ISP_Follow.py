from abc import ABC, abstractmethod

class Protocol(ABC):
    @abstractmethod
    def open(self):
        pass
    @abstractmethod
    def close(self):
        pass
    @abstractmethod
    def read(self):
        pass
    @abstractmethod
    def write(self, data):
        pass

class UARTConfig:
    def __init__(self, baudrate: int, parity: str = 'N'):
        self.baudrate = baudrate
        self.parity = parity

class I2CConfig:
    def __init__(self, slave_address: int, frequency: int = 100000):
        self.slave_address = slave_address
        self.frequency = frequency

class UART(Protocol):
    def __init__(self, config: UARTConfig):
        self.config = config
        self.is_open = False
    def open(self):
        self.is_open = True
        print(f"[UART] Opened with baudrate={self.config.baudrate}, parity={self.config.parity}")
    def write(self, data):
        if not self.is_open:
            raise RuntimeError("UART port not open.")
        print(f"[UART] TX → {data}")
    def read(self):
        if not self.is_open:
            raise RuntimeError("UART port not open.")
        print("[UART] RX ← GPS data stream")
        return "GPS: Lat=51.5074, Lon=-0.1278"
    def close(self):
        self.is_open = False
        print("[UART] Closed connection")

class I2C(Protocol):
    def __init__(self, config: I2CConfig):
        self.config = config
        self.is_open = False
    def open(self):
        self.is_open = True
        print(f"[I2C] Opened on slave={hex(self.config.slave_address)}, frequency={self.config.frequency}Hz")
    def write(self, data):
        if not self.is_open:
            raise RuntimeError("I2C bus not open.")
        print(f"[I2C] TX → {data}")
    def read(self):
        if not self.is_open:
            raise RuntimeError("I2C bus not open.")
        print("[I2C] RX ← Temperature data")
        return "Temperature: 25.6°C"
    def close(self):
        self.is_open = False
        print("[I2C] Closed bus")

class IoTDeviceManager:
    def __init__(self, protocol: Protocol):
        self.protocol = protocol
    def start(self):
        self.protocol.open()
    def send_command(self, data):
        self.protocol.write(data)
    def get_data(self):
        return self.protocol.read()
    def stop(self):
        self.protocol.close()

def main():
    # ---- Example 1: I2C Temperature Sensor ----
    i2c_config = I2CConfig(slave_address=0x48, frequency=400000)
    i2c_device = I2C(i2c_config)
    iot_i2c = IoTDeviceManager(i2c_device)

    print("\n=== I2C Temperature Sensor ===")
    iot_i2c.start()
    iot_i2c.send_command("Measure Temperature")
    print("Response:", iot_i2c.get_data())
    iot_i2c.stop()

    # ---- Example 2: UART GPS Module ----
    uart_config = UARTConfig(baudrate=9600, parity='N')
    uart_device = UART(uart_config)
    iot_uart = IoTDeviceManager(uart_device)

    print("\n=== UART GPS Module ===")
    iot_uart.start()
    iot_uart.send_command("Request Coordinates")
    print("Response:", iot_uart.get_data())
    iot_uart.stop()

if __name__ == "__main__":
    main()
