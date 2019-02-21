# Code has been copied from ServoCds55.h and .cpp to use the exact 
# same control flow to make the it work with the arduino shield

#import spidev as SPI

class ServoCds55(object):
	velocity_temp = 0
	upperLimit_temp = 0
	cs = 0
	HIGH = 1
	LOW = 0

	def __init__(self, CS = 10):
		#ServoCds55::ServoCds55 (int CS):cs(CS)
		#{
		#   velocity_temp = 150
		#   upperLimit_temp = 300
		#}
		self.velocity_temp = 150
		self.upperLimit_temp = 300
		pass

	def begin(self, ):
		#pinMode(cs,OUTPUT)	
		self.digitalWrite(self.cs, self.HIGH)
		#SPI.begin ()
		#SPI.setClockDivider(SPI_CLOCK_DIV8)
		pass

	def WritePos(self, ID, Pos):
		# low
		PosB = (Pos>>8 & 0xff)
		# high
		PosS = (Pos & 0xff)
		velocityB = (self.velocity_temp>>8 & 0xff)
		velocityS = (self.velocity_temp & 0xff)
		self.digitalWrite(self.cs, self.LOW)    
		self.transferAndWait ('p')
		self.transferAndWait (ID) 
		self.transferAndWait (PosB)
		self.transferAndWait (PosS)
		self.transferAndWait (velocityB)
		self.transferAndWait (velocityS)
		self.transferAndWait ('\t')
		self.transferAndWait ('\r')
		self.transferAndWait ('\n')
		self.digitalWrite(self.cs, self.HIGH)
		#delay(10)
		pass

	def write(self, ID, Pos):
		self.SetServoLimit(ID, self.upperLimit_temp)
		# default velocity:150
		self.WritePos(ID,Pos) 
		pass

	def setVelocity(self, velocity):
		self.velocity_temp = velocity
		pass

	def setPoslimit(self, posLimit):
		self.upperLimit_temp =  posLimit
		pass

	def rotate(self, ID, velocity):
		self.SetServoLimit(ID,0)
		#delay(100)
		self.SetMotormode(ID,velocity)
		pass
	
	def SetServoLimit(self, ID, upperLimit):
		upperLimitB = (self.upperLimit_temp>>8 & 0xff)
		upperLimitS =  (self.upperLimit_temp & 0xff)
		self.digitalWrite(self.cs, self.LOW)
		self.transferAndWait ('s')
		self.transferAndWait (ID)
		self.transferAndWait (upperLimitB)
		self.transferAndWait (upperLimitS)
		self.transferAndWait ('\t')
		self.transferAndWait ('\r')
		self.transferAndWait ('\n')
		self.digitalWrite(self.cs, self.HIGH)
		#delay(10)
		pass

	def SetMotormode(self, ID, velocity):
		velocityB = (velocity>>8 & 0xff)
		velocityS = (velocity & 0xff)
		self.digitalWrite(self.cs, self.LOW)
		self.transferAndWait ('m')
		self.transferAndWait (ID)
		self.transferAndWait (velocityB)
		self.transferAndWait (velocityS)
		self.transferAndWait ('\t')
		self.transferAndWait ('\r')
		self.transferAndWait ('\n')
		self.digitalWrite(self.cs, self.HIGH)
		#delay(10)
		pass

	def SetID(self, ID, newID):
		self.digitalWrite(self.cs, self.LOW)
		self.transferAndWait ('i')
		self.transferAndWait (ID)
		self.transferAndWait (newID)
		self.transferAndWait ('\t')
		self.transferAndWait ('\r')
		self.transferAndWait ('\n')
		self.digitalWrite(self.cs, self.HIGH)
		#delay(10)
		pass

	def Reset(self, ID):
		self.digitalWrite(self.cs, self.LOW)
		self.transferAndWait ('r')
		self.transferAndWait (ID)
		self.transferAndWait ('\t')
		self.transferAndWait ('\r')
		self.transferAndWait ('\n')
		self.digitalWrite(self.cs, self.HIGH)
		#delay(10)
		pass

	def transferAndWait(self, what):
		#byte self.transferAndWait (const byte what)
		#{
		#   byte a = SPI.transfer (what)
		#   delayMicroseconds (20)
		#   return a
		#}
		pass
	
	def digitalWrite(self, pin, level):
		pass