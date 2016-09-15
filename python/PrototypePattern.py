import copy

class DatabasePrototype:
	"""
	Database Prototype class
	"""

	_database = None
	_connection = None

	def clone(self): pass

	def getDatabase(self):
		return self._database

	def getConnection(self):
		return self._connection


class MySqlDatabase(DatabasePrototype):
	"""
	Mysql Databbase
	"""
	def __init__(self, connection):
		self._database = "mysql"
		self._connection = connection

	def clone(self):
		return copy.deepcopy(self)


class MongoDBDatabase(DatabasePrototype):
	"""
	MongoDb Databbase
	"""
	def __init__(self, connection):
		self._database = "mongodb"
		self._connection = connection

	def clone(self):
		return copy.deepcopy(self)



class DatabaseFactory:
	"""
	Database factory
	"""
	__mysqlDatabase = None
	__mongoDatabase = None

	@staticmethod
	def initialize():
		DatabaseFactory.__mysqlDatabase = MySqlDatabase("mysql Connected")
		DatabaseFactory.__mongoDatabase = MongoDBDatabase("mongo Connected")	


	@staticmethod
	def getMysqlConnection():
		return DatabaseFactory.__mysqlDatabase.clone()

	@staticmethod
	def getMongoDbConnection():
		return DatabaseFactory.__mongoDatabase.clone()



def main():
	DatabaseFactory.initialize()
	mysql = DatabaseFactory.getMysqlConnection()
	print mysql
	print "%s %s" % (mysql.getDatabase(), mysql.getConnection())

	mongodb = DatabaseFactory.getMongoDbConnection()
	print mongodb
	print "%s %s" % (mongodb.getDatabase(), mongodb.getConnection())


if __name__ == "__main__":
	main()