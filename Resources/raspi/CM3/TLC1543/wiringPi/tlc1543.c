#include <stdio.h>
#include<wiringPi.h>

#define	Clock	16
#define	Address	20
#define	DataOut	21
#define Cs  22

unsigned int ADC_Read(unsigned char channel)
{
	unsigned int value;
	unsigned char i;
	unsigned char LSB = 0, MSB = 0;
 
	digitalWrite(Cs,0);
	channel = channel << 4;
	for (i = 0; i < 4; i ++) 
	{
		if(channel & 0x80)
			digitalWrite(Address,1);
		else 
			digitalWrite(Address,0);
		digitalWrite(Clock ,1);
		digitalWrite(Clock ,0);
		channel = channel << 1;
	}
	for (i = 0; i < 6;i ++) 
	{
		digitalWrite(Clock ,1);
		digitalWrite(Clock ,0);
	}

	delayMicroseconds(15);
	for (i = 0; i < 2; i ++) 
	{
		digitalWrite(Clock ,1);
		MSB <<= 1;
		if (digitalRead(DataOut))
			MSB |= 0x1;
		digitalWrite(Clock ,0);
	} 
	for (i = 0; i < 8; i ++) 
	{
		digitalWrite(Clock ,1);
		LSB <<= 1;
		if (digitalRead(DataOut))
			LSB |= 0x1;
		digitalWrite(Clock ,0);
	} 
	digitalWrite(Cs,1);
	value = MSB;
	value <<= 8;
	value |= LSB;
	return value; 
}


int main()
{
	if (wiringPiSetup() < 0)return 1 ;

	pinMode (DataOut,INPUT);
	pullUpDnControl(DataOut, PUD_UP);
	
	pinMode (Cs,OUTPUT);

	pinMode (Clock,OUTPUT);
	pinMode (Address,OUTPUT);


	while(1)
	{
  		printf("AD: %d \n",ADC_Read(6));
		delay(100);
  	}
}
