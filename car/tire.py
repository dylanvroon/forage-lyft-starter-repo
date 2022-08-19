from abc import ABC, abstractmethod

class Tire(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def needs_service(self):
        pass

class CarriganTire(Tire):
    def __init__(self, tire_wornness_array):
        self.tire_wornness_array = tire_wornness_array

    def needs_service(self):
        for val in self.tire_wornness_array:
            if val >= 0.9:
                return True
        return False

class OctoprimeTire(Tire):
    def __init__(self, tire_wornness_array):
        self.tire_wornness_array = tire_wornness_array

    def needs_service(self):
        return sum(self.tire_wornness_array) >= 3