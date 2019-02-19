/*
 # This Sample code is for testing the Digital Servo Shield.
  
 # Editor : YouYou
 # Date   : 2014.10.24
 # Ver    : 1.0
 # Product: Digital Servo Shield for Arduino
 # SKU    : 
   
 # Hardwares:
 1. Arduino UNO
 2. Digital Servo Shield for Arduino
 3. Digital Servos( Compatible with AX-12,CDS55xx...etc)
 4. Power supply:6.5 - 12V 
  
 */

#include <SPI.h>
#include <ServoCds55.h>
ServoCds55 myservo;

void setup (void)
{
  Serial.begin (115200);
  myservo.begin ();
} 

void loop (void)
{

  if(Serial.available()){
    char val = Serial.read();
    if(val != -1)
    {
      switch(val)
      {
      case 'p':
        myservo.write(1,300);//ID:1  Pos:300  velocity:150
        delay(3000);
        myservo.write(1,0);//ID:1  Pos:0  velocity:150  
        break;

      case 'v':
        myservo.setVelocity(100);// set velocity to 100(range:0-300) in Servo mode
        break;  

      case 'm': 
        myservo.rotate(1,150);//   CCW    ID:1  Velocity: 150  middle velocity  300 max   
        delay(2000);
        myservo.rotate(1,-150);//  CW     ID:1  Velocity: -150  middle velocity  -300 max      
        break;  

//      case 'i': 
//        myservo.SetID(1,2);//ID:1   newID:2
//        break; 
//        
//        case 'r': 
//         myservo.Reset(2);//Restore ID2 servo to factory Settings ( ID:1  Baud rate:1000000)
//         break;
   
      }
    }  
    else   
      Serial.println("Wait");
    delay(500);

  }

}  

