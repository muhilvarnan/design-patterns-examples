import datetime
from pytz import timezone
import pytz


class Clock(object):
    """
    Clock
    """
    def get_time(self, ):
        return None

class ClockUS(Clock):
    """
    Clock US
    """
    TIME_ZONE = timezone('US/Eastern')
    def get_time(self):
        """
        get time
        """
        return datetime.datetime.now(self.TIME_ZONE).time()

class ClockIN(Clock):
    """
    Clock India
    """
    TIME_ZONE = timezone('Asia/Kolkata')
    def get_time(self):
        """
        get time
        """
        return datetime.datetime.now(self.TIME_ZONE).time()

class ClockFactory():
    """
    Clock factory
    """
    CLOCK_TYPES = {'us':ClockUS,'in':ClockIN}
    def get_clock(self, clock_type):
        """
        get clock type
        """
        return self.CLOCK_TYPES.get(clock_type)()

class Car(object):
    """
    Car object
    """
    def get_price(self):
        """
        Get prince
        """
        return None

class AudiCar(Car):
    """
    AudiCar
    """
    price = 1000
    def get_price(self):
        """
        get price
        """
        return self.price

class BMWCar(Car):
    """
    BMW car
    """
    price = 1500
    def get_price(self):
        """
        get price
        """
        return self.price

class CarFactory():
    """
    Car Factory
    """
    CAR_TYPES = {
        'audi':AudiCar,
        'bmw':BMWCar
    }
    def get_car(self, car_type):
        return self.CAR_TYPES.get(car_type)()

class MainFactory():
    """
    Main Factory (Abstract)
    """
    FACTORY_TYPES = {
        'car':CarFactory,
        'clock':ClockFactory
    }

    def get_factory(self, factory_type):
        """
        get factory
        """
        return self.FACTORY_TYPES.get(factory_type)()


factoryObj = MainFactory()
carFactoryObj = factoryObj.get_factory('car')
cars = ['audi', 'bmw']
for car in cars:
    print carFactoryObj.get_car(car).get_price()

clockFactoryObj = factoryObj.get_factory('clock')
clocks = ['us', 'in']
for clock in clocks:
    print clockFactoryObj.get_clock(clock).get_time()
