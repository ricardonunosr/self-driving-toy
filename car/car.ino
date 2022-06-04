#define MOTOR_FORWARD 5
#define MOTOR_BACKWARD 6
#define MOTOR_LEFT 10
#define MOTOR_RIGHT 11

void setup() {
  Serial.begin(9600);
  pinMode(MOTOR_FORWARD, OUTPUT);
  pinMode(MOTOR_BACKWARD, OUTPUT);
  pinMode(MOTOR_LEFT, OUTPUT);
  pinMode(MOTOR_RIGHT, OUTPUT);
  digitalWrite(MOTOR_FORWARD, LOW); // Start motor off
  digitalWrite(MOTOR_BACKWARD, LOW);
  digitalWrite(MOTOR_LEFT, LOW);
  digitalWrite(MOTOR_RIGHT, LOW);
}

void loop() {
  while (Serial.available()) // whatever the data that is coming in serially and
                             // assigning the value to the variable “data”
  {
    byte data = Serial.read();
    Serial.println(data);
    if (data == '1') {
      digitalWrite(MOTOR_BACKWARD, LOW);
      digitalWrite(MOTOR_FORWARD, HIGH); // Turn on motor forward
    } else if (data == '0') {
      digitalWrite(MOTOR_FORWARD, LOW); // Turn off motor forward
    } else if (data == '2') {
      digitalWrite(MOTOR_FORWARD, LOW);
      digitalWrite(MOTOR_BACKWARD, HIGH); // Turn on motor backward
    } else if (data == '3') {
      digitalWrite(MOTOR_BACKWARD, LOW); // Turn off motor backward
    } else if (data == '4') {
      digitalWrite(MOTOR_LEFT, HIGH); // Turn on motor left
    } else if (data == '5') {
      digitalWrite(MOTOR_LEFT, LOW); // Turn off motor left
    } else if (data == '6') {
      digitalWrite(MOTOR_RIGHT, HIGH); // Turn on motor right
    } else if (data == '7') {
      digitalWrite(MOTOR_RIGHT, LOW); // Turn off motor right
    }
  }
}
