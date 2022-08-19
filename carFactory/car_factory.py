from urllib.parse import SplitResult
from car.car import Car
from car.engine import WilloughbyEngine, CapuletEngine, SternmanEngine
from car.battery import NubbinBattery, SpindlerBattery

class CarFactory():
    def __init__(self):
        self.model_info = dict()
        self.model_info["calliope"] = ["capulet", "spindler"]
        self.model_info["glissade"] = ["willoughby", "spindler"]
        self.model_info["palindrome"] = ["sternman", "spindler"]
        self.model_info["rorschach"] = ["willoughby", "nubbin"]
        self.model_info["thovex"] = ["capulet", "nubbin"]
        pass

    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
        myEngine = CapuletEngine(last_service_mileage, current_mileage)
        myBattery = SpindlerBattery(last_service_date, current_date)
        return Car(myEngine, myBattery)

    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage):
        myEngine = WilloughbyEngine(last_service_mileage, current_mileage)
        myBattery = SpindlerBattery(last_service_date, current_date)
        return Car(myEngine, myBattery)

    def create_palindrome(self, current_date, last_service_date, warning_light_on):
        myEngine = SternmanEngine(warning_light_on)
        myBattery = SpindlerBattery(last_service_date, current_date)
        return Car(myEngine, myBattery)

    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage):
        myEngine = WilloughbyEngine(last_service_mileage, current_mileage)
        myBattery = NubbinBattery(last_service_date, current_date)
        return Car(myEngine, myBattery)

    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage):
        myEngine = CapuletEngine(last_service_mileage, current_mileage)
        myBattery = NubbinBattery(last_service_date, current_date)
        return Car(myEngine, myBattery)