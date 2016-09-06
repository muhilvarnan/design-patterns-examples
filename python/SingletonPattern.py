class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class DatabaseConnection(object):
    
    __metaclass__ = Singleton

    connection = None
    
    def __init__(self,):
    	self.connection = "connected"

    def get_connection(self):
    	"""
    	get connection
    	"""
    	return self.connection

db = DatabaseConnection()
print db
print db.get_connection()
db = DatabaseConnection()
print db
print db.get_connection()