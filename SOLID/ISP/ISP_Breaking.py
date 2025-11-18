from abc import ABC, abstractmethod

class Protocol(ABC):
    @abstractmethod
    def set_baud_rate(self, baud_rate):
        """UART-only configuration"""
        pass
    @abstractmethod
    def set_slave_address(self, address):
        """I2C-only configuration"""
        pass
    @abstractmethod
    def open(self):
        pass
    @abstractmethod
    def read(self):
        pass
    @abstractmethod
    def write(self, data):
        pass
    @abstractmethod
    def close(self):
        pass

class I2C(Protocol):
    def __init__(self, slave_address):
        self.slave_address = slave_address
    def set_baud_rate(self, baud_rate):
        print("[I2C] Ignoring baud rate — not applicable for I2C")
    def set_slave_address(self, address):
        self.slave_address = address
        print(f"[I2C] Slave address set to {hex(address)}")
    def open(self):
        print(f"[I2C] Bus opened with slave={hex(self.slave_address)}")
    def read(self):
        print("[I2C] Reading temperature data...")
        return "Temperature: 25.6°C"
    def write(self, data):
        print(f"[I2C] Writing data: {data}")
    def close(self):
        print("[I2C] Bus closed")

class UART(Protocol):
    def __init__(self, baud_rate):
        self.baud_rate = baud_rate
    def set_baud_rate(self, baud_rate):
        self.baud_rate = baud_rate
        print(f"[UART] Baud rate set to {baud_rate}")
    def set_slave_address(self, address):
        print("[UART] Ignoring slave address — not applicable for UART")
    def open(self):
        print(f"[UART] Port opened at {self.baud_rate} baud")
    def read(self):
        print("[UART] Reading GPS data...")
        return "GPS: Lat=51.5074, Lon=-0.1278"
    def write(self, data):
        print(f"[UART] Sending data: {data}")
    def close(self):
        print("[UART] Port closed")

def main():
    print("\n=== ISP VIOLATION DEMO ===")

    i2c = I2C(slave_address=0x48)
    i2c.set_baud_rate(9600)     # Nonsense for I2C
    i2c.open()
    print(i2c.read())
    i2c.close()

    print("")

    uart = UART(baud_rate=115200)
    uart.set_slave_address(0x48) # Nonsense for UART
    uart.open()
    print(uart.read())
    uart.close()


if __name__ == "__main__":
    main()
