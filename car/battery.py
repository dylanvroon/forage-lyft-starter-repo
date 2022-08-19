from abc import ABC, abstractmethod

class Battery(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def needs_service(self):
        pass

class SpindlerBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date
        self.service_time = 3
    
    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + self.service_time)
        return service_threshold_date < self.current_date

class NubbinBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date
        self.service_time = 4
    
    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + self.service_time)
        return service_threshold_date < self.current_date