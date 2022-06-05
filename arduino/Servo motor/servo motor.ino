#include <Servo.h>
Servo Motor;
int pos;
void setup()
{
 Motor.attach(3); 
Motor.writeMicroseconds(1000); //fully counter clockwise
Motor.writeMicroseconds(1500); // mid 
Motor.writeMicroseconds(2000);// fully clockwise
int pos = Motor.read();
Serial.println(pos);
delay(1000);
}

void loop()
{


  for(pos=0;pos<=180; pos++)
  {Motor.write(pos);
  
   //delay(20);
  }
  delay(1000);
  for(pos=180; pos>=0; pos--){
    Motor.write(pos);
    // delay(20);
  }
  delay(1000);

}