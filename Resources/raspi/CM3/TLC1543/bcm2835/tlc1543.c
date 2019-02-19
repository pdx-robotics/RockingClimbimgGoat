#include <stdio.h>
#include <bcm2835.h>

#define	Clock	16
#define	Address	20
#define	DataOut	21
//#define Cs  22
unsigned int ADC_Read(unsigned char channel)
{
	unsigned int value;
	unsigned char i;
	unsigned char LSB = 0, MSB = 0;
 
//	bcm2835_gpio_write(Cs,LOW);
	channel = channel << 4;
	for (i = 0; i < 4; i ++) 
	{
		if(channel & 0x80)
			bcm2835_gpio_write(Address,1);
		else 
			bcm2835_gpio_write(Address,0);
		bcm2835_gpio_write(Clock ,1);
	//	delayMicroseconds(100);
		bcm2835_gpio_write(Clock ,0);
	//	delayMicroseconds(100);
		channel = channel << 1;
	}
	for (i = 0; i < 6;i ++) 
	{
		bcm2835_gpio_write(Clock ,1);
	//	delayMicroseconds(100);
		bcm2835_gpio_write(Clock ,0);
	//	delayMicroseconds(100);
	}
//	bcm2835_gpio_write(Cs,1);
	delayMicroseconds(50);
//bcm2835_delay(1);
//	bcm2835_gpio_write(Cs,0);
	for (i = 0; i < 2; i ++) 
	{
		bcm2835_gpio_write(Clock ,1);
	//	delayMicroseconds(100);
		MSB <<= 1;
		if (bcm2835_gpio_lev(DataOut))
			MSB |= 0x1;
		bcm2835_gpio_write(Clock ,0);
	//	delayMicroseconds(100);
	} 
	for (i = 0; i < 8; i ++) 
	{
		bcm2835_gpio_write(Clock ,1);
	//	delayMicroseconds(100);
		LSB <<= 1;
		if (bcm2835_gpio_lev(DataOut))
			LSB |= 0x1;
		bcm2835_gpio_write(Clock ,0);
	//	delayMicroseconds(100);
	} 
	value = MSB;
	value <<= 8;
	value |= LSB;
//	bcm2835_gpio_write(Cs,LOW);
delayMicroseconds(50);
//bcm2835_delay(10);
	return value; 
}


int main()
{
	if (!bcm2835_init())return 1 ;

	bcm2835_gpio_fsel(DataOut,BCM2835_GPIO_FSEL_INPT);
	bcm2835_gpio_set_pud(DataOut, BCM2835_GPIO_PUD_UP);

//	bcm2835_gpio_fsel(Cs,BCM2835_GPIO_FSEL_OUTP);

	bcm2835_gpio_fsel(Clock,BCM2835_GPIO_FSEL_OUTP);
	bcm2835_gpio_fsel(Address,BCM2835_GPIO_FSEL_OUTP);

//	bcm2835_gpio_write(Cs,LOW);

	while(1)
	{
/*  		printf("AD: %d ",ADC_Read(0));//delayMicroseconds(50);//bcm2835_delay(1);
	 	 printf("%d ",ADC_Read(1)); //delayMicroseconds(50); //bcm2835_delay(1);

               printf("%d ",ADC_Read(2));//delayMicroseconds(50); // bcm2835_delay(1);

               printf("%d ",ADC_Read(3));//delayMicroseconds(50);  //bcm2835_delay(1);

               printf("%d ",ADC_Read(4));//delayMicroseconds(50); // bcm2835_delay(1);

               printf("%d ",ADC_Read(5));//delayMicroseconds(50); // bcm2835_delay(1);

               printf("%d ",ADC_Read(6));//delayMicroseconds(50); // bcm2835_delay(1);

               printf("%d ",ADC_Read(7));//delayMicroseconds(50); // bcm2835_delay(1);

               printf("%d ",ADC_Read(8));// delayMicroseconds(50);// bcm2835_delay(1);

               printf("%d ",ADC_Read(9));// delayMicroseconds(50);// bcm2835_delay(1);

               printf("%d\r\n",ADC_Read(10));//delayMicroseconds(50); // bcm2835_delay(1);
*/
               printf("%d \r\n",ADC_Read(6));
              
               bcm2835_delay(100);
  	}
}
