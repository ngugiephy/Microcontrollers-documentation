#include <Keypad.h>
#include <LiquidCrystal.h>

LiquidCrystal lcd(8, 9, 10, 11, 12, 13);

const byte rows = 4; //four rows
const byte cols = 3; //three columns
char keys[rows][cols] = {
  {'1','2','3'},
  {'4','5','6'},
  {'7','8','9'},
  {'*','0','#'}
};
byte rowPins[rows] = {0, 1, 2, 3}; //connect to the row pinouts of the keypad
byte colPins[cols] = {4, 5, 6}; //connect to the column pinouts of the keypad
Keypad keypad = Keypad( makeKeymap(keys), rowPins, colPins, rows, cols );

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  
  lcd.begin(16,1);
  lcd.print("hello, world!");
  delay(1000);
  lcd.clear();
}

void loop() {
  // put your main code here, to run repeatedly:
  char pressedKey = keypad.getKey();
  if(pressedKey != NO_KEY){
    lcd.print(pressedKey);
  }
}