class PhoneBuilder:
	"""
	Builder class
	"""
	def getRam(self): pass
	def getScreen(self): pass
	def getManufacturer(self): pass


class Ram:
	"""
	Ram class
	"""
	memory = None

class Screen:
	"""
	Screen class
	"""
	size = None

class Manufacturer:
	"""
	Manufacturer class
	"""
	name = None

class XperiaZBuilder(PhoneBuilder):
	"""
	Xperia z phone builder
	"""
	def getRam(self):
		"""
		get Ram
		"""
		ram = Ram()
		ram.memory = "2GB"
		return ram

	def getScreen(self):
		"""
		get Screen 
		"""
		screen = Screen()
		screen.size = "5.5"
		return screen

	def getManufacturer(self):
		"""
		get Manufacturer
		"""
		manufacturer = Manufacturer()
		manufacturer.name = "Sony"
		return manufacturer

class Iphone4sBuilder(PhoneBuilder):
	"""
	Xperia z phone builder
	"""
	def getRam(self):
		"""
		get Ram
		"""
		ram = Ram()
		ram.memory = "1GB"
		return ram

	def getScreen(self):
		"""
		get Screen 
		"""
		screen = Screen()
		screen.size = "4.5"
		return screen

	def getManufacturer(self):
		"""
		get Manufacturer
		"""
		manufacturer = Manufacturer()
		manufacturer.name = "Apple"
		return manufacturer


class Director():
	"""
	Director class
	"""
	__builder = None

	def setBuilder(self, builder):
		self.__builder = builder

	def getPhone(self):
		"""
		get Phone
		"""
		phone = Phone()
		ram = self.__builder.getRam()
		phone.setRam(ram)

		screen = self.__builder.getScreen()
		phone.setScreen(screen)

		manufacturer = self.__builder.getManufacturer()
		phone.setMaufacturer(manufacturer)

		return phone

class Phone:
	"""
	Phone
	"""

	def __init__(self):
		self.__ram = None
		self.__screen = None
		self.__manufacturer = None


	def setRam(self, ram):
		self.__ram = ram

	def setScreen(self, screen):
		self.__screen = screen

	def setMaufacturer(self, manufacturer):
		self.__manufacturer = manufacturer


	def specification(self):
		print "Ram : %s" % self.__ram.memory
		print "Screen: %s " % self.__screen.size  
		print "Manufacturer: %s" % self.__manufacturer.name

def main():
	"""
	main function
	"""
	xperiaz = XperiaZBuilder()
	iphone45 = Iphone4sBuilder()

	
	director = Director()
	print "xperia z"
	director.setBuilder(xperiaz)
	phone = director.getPhone()
	phone.specification()

	print "iphone 4s"
	director.setBuilder(iphone45)
	phone = director.getPhone()
	phone.specification()


if __name__ == "__main__":
	main()