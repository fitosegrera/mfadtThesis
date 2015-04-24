#include "SoftwareSerial.h"

SoftwareSerial alphaSerial(3, 2); // RX, TX

int solenoid = 6;
int red = 7; 
int green = 8;

String ID = "4";

int dropCount = 0;
String toSend;
char bytes[4];

void setup(){
	Serial.begin(9600);//Initiate serial communication XBEE
	Serial.setTimeout(10);
	alphaSerial.begin(9600);//Initiate serial communication to send to atmega328 ALPHA-DISPLAY
	pinMode(solenoid, OUTPUT);//Set Digital Pin 6 from the atmega328 as an output to SOLENOID
	pinMode(red, OUTPUT);//RED LED
	pinMode(green, OUTPUT);//GREEN LED
}

void loop(){
	//Data comming from the UDOO via XBEE
	String data = Serial.readStringUntil(';');
    if (data == ID){
		digitalWrite(solenoid, HIGH);
		digitalWrite(red, LOW);
		digitalWrite(green, HIGH);
		dropCount++;
		alphaSerial.println(String(dropCount));//Send Data to ALPHA-DISPLAY
    }else{
    	digitalWrite(solenoid, LOW);
      	digitalWrite(red, HIGH);
      	digitalWrite(green, LOW);
    }
}