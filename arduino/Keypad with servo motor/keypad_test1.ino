#include <Wire.h> 
#include <LiquidCrystal.h>
#include <Keypad.h>
#include <Servo.h>

//define your password length here
#define Password_Length 9


Servo myservo;
int signalPin = 12;
int servopin = 11;

char Data[Password_Length]; 
char Master[Password_Length] = "123A456B"; //You can choose any password here
byte data_count = 0, master_count = 0;
bool Pass_is_good;
char customKey;
int position=0;

const int rs = A0, en = A1, d4 = A2, d5 = A3, d6 = A4, d7 = A5;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);
const byte ROWS = 4;
const byte COLS = 4;

char hexaKeys[ROWS][COLS] = {
  {'1', '2', '3', 'A'},
  {'4', '5', '6', 'B'},
  {'7', '8', '9', 'C'},
  {'*', '0', '#', 'D'}
};

byte rowPins[ROWS] = {9, 8, 7, 6};
byte colPins[COLS] = {5, 4, 3, 2};

Keypad customKeypad = Keypad(makeKeymap(hexaKeys), rowPins, colPins, ROWS, COLS);

int cursor=0;

void setup(){
  pinMode(signalPin,OUTPUT);
  myservo.attach(servopin);
  myservo.write(0);
  lcd.begin(16, 2); 
  Serial.begin(9600);
}


 void loop(){

  lcd.setCursor(0,0);
  lcd.print("Enter Password:");

  customKey = customKeypad.getKey();
  if (customKey){
    Data[data_count] = customKey; 
    lcd.setCursor(data_count,1); 
    lcd.print(Data[data_count]); 
    data_count++; 
    }

  if(data_count == Password_Length-1){
    lcd.clear();

    if(!strcmp(Data, Master)){
      lcd.print("Correct");
      digitalWrite(signalPin, HIGH);
      myservo.write(90);
      delay(5000);
      digitalWrite(signalPin, LOW);
      }
    else{
      lcd.print("Incorrect");
      delay(1000);
      }
    
    lcd.clear();
    clearData();  
  }
}

void clearData(){
  while(data_count !=0){
    Data[data_count--] = 0; 
    myservo.write(0);
  }
  return;
} 
  