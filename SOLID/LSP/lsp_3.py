class Car:
    def start(self):
        print("Car started.")
    def change_gear(self, gear: int):
        print(f"Changed to gear {gear}.")
    def press_clutch(self):
        print("Clutch pressed.")

# Subclass 1 — Manual Car
class ManualCar(Car):
    def change_gear(self, gear):
        self.press_clutch()  # Manual requires clutch
        print(f"Manual car in gear {gear}")

# Subclass 2 — Automatic Car
class AutomaticCar(Car):
    def press_clutch(self):
        # Automatic cars don’t have a clutch!
        raise Exception("Automatic car does not have a clutch!")
    def change_gear(self, gear):
        print(f"Automatic transmission changed to gear {gear}")
        
# Client code
def test_drive(car: Car):
    car.start()
    car.press_clutch()     # expected to work for all cars
    car.change_gear(1)

# Run
manual = ManualCar()
automatic = AutomaticCar()

print("Manual Car Drive:")
test_drive(manual)

print("Automatic Car Drive:")
try:
    test_drive(automatic)   #Crashes — LSP violated
except Exception as e:
    print(str(e))
#================================================================================================================
from abc import ABC, abstractmethod
# Base abstraction
class Car(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def drive(self):
        pass


# ManualCar subclass (has clutch)
class ManualCar(Car):
    def start(self):
        print("Manual car started.")
    def press_clutch(self):
        print("Clutch pressed.")
    def change_gear(self, gear):
        print(f"Manual car: gear changed to {gear}")
    def drive(self):
        self.press_clutch()
        self.change_gear(1)
        print("Manual car driving...")

# AutomaticCar subclass (no clutch)
class AutomaticCar(Car):
    def start(self):
        print("Automatic car started.")
    def drive(self):
        print("Automatic transmission engaged.")
        print("Automatic car driving...")

# Client code
def take_for_drive(car: Car):
    car.start()
    car.drive()

# Run demo
manual = ManualCar()
auto = AutomaticCar()

print("Manual Car Drive:")
take_for_drive(manual)

print("Automatic Car Drive:")
take_for_drive(auto)
