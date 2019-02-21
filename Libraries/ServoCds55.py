# Code has been copied from ServoCds55.h and .cpp to use the exact 
# same control flow to make the it work with the arduino shield

import spidev as SPI

class ServoCds55(object):
	self.velocity_temp = 0
	self.upperLimit_temp = 0
	self.cs = 0

	def __init__(CS = 10):
		#ServoCds55::ServoCds55 (int CS):cs(CS)
		#{
		#   velocity_temp = 150
		#   upperLimit_temp = 300
		#}
		pass

	def begin():
		#pinMode(cs,OUTPUT)	
		#digitalWrite(cs,HIGH)
		#SPI.begin ()
		#SPI.setClockDivider(SPI_CLOCK_DIV8)
		pass

	def WritePos(int ID,int Pos):
		#int PosB = (Pos>>8 & 0xff)//low
		#int PosS = (Pos & 0xff)//high
		#int velocityB = (velocity_temp>>8 & 0xff)
		#int velocityS = (velocity_temp & 0xff)
		#digitalWrite(cs, LOW)    
		self.transferAndWait ('p')
		self.transferAndWait (ID) 
		self.transferAndWait (PosB)
		self.transferAndWait (PosS)
		self.transferAndWait (velocityB)
		self.transferAndWait (velocityS)
		self.transferAndWait ('\t')
		self.transferAndWait ('\r')
		self.transferAndWait ('\n')
		#digitalWrite(cs, HIGH)
		#delay(10)
		pass

	def write(int ID,int Pos):
		#SetServoLimit(ID,upperLimit_temp)
		#WritePos(ID,Pos)// default velocity:150 
		pass

	def setVelocity(int velocity):
		#velocity_temp = velocity
		pass

	def setPoslimit(int posLimit):
		#upperLimit_temp =  posLimit
		pass

	def rotate(int ID,int velocity):
		#SetServoLimit(ID,0)
		#delay(100)
		#SetMotormode(ID,velocity)
		pass
	
	def SetServoLimit(int ID,int upperLimit):
		#int upperLimitB = (upperLimit_temp>>8 & 0xff)
		#int upperLimitS =  (upperLimit_temp & 0xff)
		#digitalWrite(cs, LOW)
		self.transferAndWait ('s')
		self.transferAndWait (ID)
		self.transferAndWait (upperLimitB)
		self.transferAndWait (upperLimitS)
		self.transferAndWait ('\t')
		self.transferAndWait ('\r')
		self.transferAndWait ('\n')
		#digitalWrite(cs, HIGH)
		#delay(10)
		pass

	def SetMotormode(int ID, int velocity):
		#int velocityB = (velocity>>8 & 0xff)
		#int velocityS = (velocity & 0xff)
		#digitalWrite(cs, LOW)    
		self.transferAndWait ('m')
		self.transferAndWait (ID)
		self.transferAndWait (velocityB)
		self.transferAndWait (velocityS)
		self.transferAndWait ('\t')
		self.transferAndWait ('\r')
		self.transferAndWait ('\n')
		#digitalWrite(cs, HIGH)
		#delay(10)
		pass

	def SetID(int ID, int newID):
		#digitalWrite(cs, LOW)    
		self.transferAndWait ('i')
		self.transferAndWait (ID)
		self.transferAndWait (newID)
		self.transferAndWait ('\t')
		self.transferAndWait ('\r')
		self.transferAndWait ('\n')
		#digitalWrite(cs, HIGH)
		#delay(10)
		pass

	def Reset(int ID):
		#digitalWrite(cs, LOW)    
		self.transferAndWait ('r')
		self.transferAndWait (ID)
		self.transferAndWait ('\t')
		self.transferAndWait ('\r')
		self.transferAndWait ('\n')
		#digitalWrite(cs, HIGH)
		#delay(10)
		pass


	def self.transferAndWait(what):
		#byte self.transferAndWait (const byte what)
		#{
		#   byte a = SPI.transfer (what)
		#   delayMicroseconds (20)
		#   return a
		#}
		pass