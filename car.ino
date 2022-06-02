int motorForward = 5;
int motorBackward = 6;
int motorLeft = 10;
int motorRight = 11;
int data;

void setup() {
  Serial.begin(9600);
  pinMode(motorForward, OUTPUT);
  pinMode(motorBackward, OUTPUT);
  pinMode(motorLeft, OUTPUT);
  pinMode(motorRight, OUTPUT);
  digitalWrite(motorForward, LOW); // Start motor off
  digitalWrite(motorBackward, LOW);
  digitalWrite(motorLeft, LOW);
  digitalWrite(motorRight, LOW);
}

void loop() {
  while (Serial.available()) // whatever the data that is coming in serially and
                             // assigning the value to the variable “data”
  {
    data = Serial.read();
  }
  if (data == '1')
    digitalWrite(motorForward, HIGH); // Turn on motor forward
  else if (data == '0')
    digitalWrite(motorForward, LOW); // Turn off motor forward
  else if (data == '2')
    digitalWrite(motorBackward, HIGH); // Turn on motor backward
  else if (data == '3')
    digitalWrite(motorBackward, LOW); // Turn off motor backward
  else if (data == '4')
    digitalWrite(motorLeft, HIGH); // Turn on motor left
  else if (data == '5')
    digitalWrite(motorLeft, LOW); // Turn off motor left
  else if (data == '6')
    digitalWrite(motorRight, HIGH); // Turn on motor right
  else if (data == '7')
    digitalWrite(motorRight, LOW); // Turn off motor right
}
