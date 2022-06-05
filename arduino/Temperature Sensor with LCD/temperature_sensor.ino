#include <LiquidCrystal.h>

LiquidCrystal lcd(8, 9, 10, 11, 12, 13);
float tempValue;
int tempPin = A0;

void setup(){
  Serial.begin(9600);
  lcd.begin(16,1);
  lcd.print("Temperature Sensor");
  delay(1000);
  lcd.clear();
}

void loop(){
  tempValue = analogRead(tempPin);
  tempValue *= 0.48828125;
  lcd.clear();
  lcd.print("Temp = ");
  lcd.print(tempValue);
  lcd.print(" *C");
  delay(1000);
}