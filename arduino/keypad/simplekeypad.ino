#include <Keypad.h>
const int ROW = 4; //no of row
const int COLUMN = 4;//no column
//Assingment of values
char keys[ROW][COLUMN]= {
  {'1','2','3','A'},
  {'4','4','5','B'},
  {'7','8','9','C'},
  {'*','0','#','D'},
};

byte PINR[ROW] = {9,8,7,6};//assinging pin to rows

byte PINCO[COLUMN] = {5,4,3,2}; //assigning pin to culmns
Keypad keypad = Keypad(makeKeymap(keys), PINR,PINCO, ROW, COLUMN );
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
char key = keypad.getKey();
if (key){
Serial.println(key);
}

}