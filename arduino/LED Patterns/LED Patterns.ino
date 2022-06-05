int a = 2;
int b = 3;
int c = 4;
int d = 5;
int e = 6;
int f = 7;
void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
pinMode(a, OUTPUT);
pinMode(b, OUTPUT);
pinMode(c, OUTPUT);
pinMode(d, OUTPUT);
pinMode(e, OUTPUT);
pinMode(f, OUTPUT);


}

void loop() {
  // put your main code here, to run repeatedly:
  
  digitalWrite(a, HIGH);
  digitalWrite(f, HIGH);
  digitalWrite(c, LOW);
  digitalWrite(d, LOW);
  digitalWrite(e, LOW);
  digitalWrite(b, LOW);
  delay(100);
digitalWrite(b, HIGH);
  digitalWrite(e, HIGH);
  digitalWrite(f, LOW);
  digitalWrite(a, LOW);
  digitalWrite(c, LOW);
  digitalWrite(d, LOW);
  delay(100);
digitalWrite(c, HIGH);
  digitalWrite(d, HIGH);
  digitalWrite(a, LOW);
  digitalWrite(b, LOW);
  digitalWrite(e, LOW);
  digitalWrite(f, LOW);
  delay(100);
digitalWrite(c, HIGH);
  digitalWrite(d, HIGH);
  digitalWrite(a, LOW);
  digitalWrite(b, LOW);
  digitalWrite(e, LOW);
  digitalWrite(f, LOW);
  delay(100);
digitalWrite(b, HIGH);
  digitalWrite(e, HIGH);
  digitalWrite(f, LOW);
  digitalWrite(a, LOW);
  digitalWrite(c, LOW);
  digitalWrite(d, LOW);
  delay(100);
digitalWrite(a, HIGH);
  digitalWrite(f, HIGH);
  digitalWrite(c, LOW);
  digitalWrite(d, LOW);
  digitalWrite(e, LOW);
  digitalWrite(b, LOW);
  delay(500);
digitalWrite(a, LOW);
delay(100);
digitalWrite(b, HIGH);
delay(100);
digitalWrite(c, LOW);
delay(100);
digitalWrite(d, HIGH);
delay(100);
digitalWrite(e, LOW);
delay(100);
digitalWrite(f, HIGH);
delay(100);
digitalWrite(a, HIGH);
delay(100);
digitalWrite(b, LOW);
delay(100);
digitalWrite(c, HIGH);
delay(100);
digitalWrite(d, LOW);
delay(100);
digitalWrite(c, HIGH);
  digitalWrite(d, HIGH);
  digitalWrite(a, LOW);
  digitalWrite(b, LOW);
  digitalWrite(e, LOW);
  digitalWrite(f, LOW);
  delay(100);
digitalWrite(c, HIGH);
  digitalWrite(d, LOW);
  digitalWrite(a, HIGH);
  digitalWrite(b, LOW);
  digitalWrite(e, HIGH);
  digitalWrite(f, LOW);
  delay(100);
digitalWrite(c, LOW);
delay(200);
digitalWrite(e, LOW);
delay(100);

}
