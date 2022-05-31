#include <NewPing.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#define LED 6
LiquidCrystal_I2C lcd(0x27, 16, 2);
NewPing sonar(5,4, 100);
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  lcd.begin(16,2);
  lcd.backlight();
  lcd.clear();
  //lcd.autoscroll();
}

void loop() {
  // put your main code here, to run repeatedly:
  int distance = sonar.ping_cm();
  Serial.println(distance);
  lcd.setCursor(0,0);
  lcd.print("Distance in cm: ");
  lcd.setCursor(0,1);
  lcd.print(distance);
  delay(1000);
  lcd.clear();
  if distance<=5{
    BlinlFast(LED);
  }
  if distance >= 6 && distance <=10{
    BlinkSlow(LED);
  }
}
void BlinkFast(int pin){
  digitalWrite(pin, 1);
  delay(500);
  digitalWrite(pin, 0);
  delay(500);
}
void BlinkSlow(int pin){
  digitalWrite(pin, 1);
  delay(1000);
  digitalWrite(pin, 0);
  delay(1000);
}
