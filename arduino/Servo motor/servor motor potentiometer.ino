#include <Servo.h>

Servo myservo;  

int potpin = 0;  
int val;    // variable to read the value from the analog pin

void setup() {
  myservo.attach(9);  // attaches the servo on pin 9 to the servo object
}

void loop() {
  val = analogRead(potpin);            
  val = map(val, 0, 1023, 0, 180);
  myservo.write(val);                  
  delay(15);                           
}