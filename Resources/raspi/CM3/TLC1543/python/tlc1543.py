#!/usr/bin/python
# -*- coding:utf-8 -*-
import RPi.GPIO as GPIO
import time

Clock = 16
Address = 20
DataOut = 21

def ADC_Read(channel):
	value = 0;
	for i in range(0,4):
		if((channel >> (3 - i)) & 0x01):
			GPIO.output(Address,GPIO.HIGH)
		else:
			GPIO.output(Address,GPIO.LOW)
		GPIO.output(Clock,GPIO.HIGH)
		GPIO.output(Clock,GPIO.LOW)
	for i in range(0,6):
		GPIO.output(Clock,GPIO.HIGH)
		GPIO.output(Clock,GPIO.LOW)
	time.sleep(0.001)
	for i in range(0,10):
		GPIO.output(Clock,GPIO.HIGH)
		value <<= 1
		if(GPIO.input(DataOut)):
			value |= 0x01
		GPIO.output(Clock,GPIO.LOW)
	return value
	
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(Clock,GPIO.OUT)
GPIO.setup(Address,GPIO.OUT)
GPIO.setup(DataOut,GPIO.IN,GPIO.PUD_UP)

try:
	while True:
		print("AD: %d "%ADC_Read(6))
		time.sleep(0.1)
except:
	GPIO.cleanup()

