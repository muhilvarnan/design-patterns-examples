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

clockFactoryObj = ClockFactory()
clocks = ['us', 'in']
for clock in clocks:
    print clockFactoryObj.get_clock(clock).get_time()
