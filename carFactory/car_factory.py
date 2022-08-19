from urllib.parse import SplitResult
from car.car import Car
from car.engine import WilloughbyEngine, CapuletEngine, SternmanEngine
from car.battery import NubbinBattery, SpindlerBattery
from car.tire import CarriganTire, OctoprimeTire

TIRE_DEFAULT = [0,0, 0,0]

class CarFactory():
    def __init__(self):
        self.model_info = dict()
        self.model_info["calliope"] = ["capulet", "spindler", "carrigan"]
        self.model_info["glissade"] = ["willoughby", "spindler", "carrigan"]
        self.model_info["palindrome"] = ["sternman", "spindler", "octoprime"]
        self.model_info["rorschach"] = ["willoughby", "nubbin", "carrigan"]
        self.model_info["thovex"] = ["capulet", "nubbin", "octoprime"]
        self.tireDefault = [0, 0, 0, 0]
        pass

    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage, tire_wornness_array = TIRE_DEFAULT):
        myEngine = CapuletEngine(last_service_mileage, current_mileage)
        myBattery = SpindlerBattery(last_service_date, current_date)
        myTires = CarriganTire(tire_wornness_array)
        return Car(myEngine, myBattery, myTires)

    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage, tire_wornness_array = TIRE_DEFAULT):
        myEngine = WilloughbyEngine(last_service_mileage, current_mileage)
        myBattery = SpindlerBattery(last_service_date, current_date)
        myTires = CarriganTire(tire_wornness_array)
        return Car(myEngine, myBattery, myTires)

    def create_palindrome(self, current_date, last_service_date, warning_light_on, tire_wornness_array = TIRE_DEFAULT):
        myEngine = SternmanEngine(warning_light_on)
        myBattery = SpindlerBattery(last_service_date, current_date)
        myTires = OctoprimeTire(tire_wornness_array)
        return Car(myEngine, myBattery, myTires)

    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage, tire_wornness_array = TIRE_DEFAULT):
        myEngine = WilloughbyEngine(last_service_mileage, current_mileage)
        myBattery = NubbinBattery(last_service_date, current_date)
        myTires = CarriganTire(tire_wornness_array)
        return Car(myEngine, myBattery, myTires)

    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage, tire_wornness_array = TIRE_DEFAULT):
        myEngine = CapuletEngine(last_service_mileage, current_mileage)
        myBattery = NubbinBattery(last_service_date, current_date)
        myTires = OctoprimeTire(tire_wornness_array)
        return Car(myEngine, myBattery, myTires)