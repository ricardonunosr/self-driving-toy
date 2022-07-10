#define MOTOR_LEFT_FORWARD 5
#define MOTOR_LEFT_BACKWARD 6
#define MOTOR_RIGHT_FORWARD 10
#define MOTOR_RIGHT_BACKWARD 11

void setup()
{
  Serial.begin(9600);
  pinMode(MOTOR_LEFT_FORWARD, OUTPUT);
  pinMode(MOTOR_LEFT_BACKWARD, OUTPUT);
  pinMode(MOTOR_RIGHT_FORWARD, OUTPUT);
  pinMode(MOTOR_RIGHT_BACKWARD, OUTPUT);
  digitalWrite(MOTOR_LEFT_FORWARD, LOW); // Start motor off
  digitalWrite(MOTOR_LEFT_BACKWARD, LOW);
  digitalWrite(MOTOR_RIGHT_FORWARD, LOW);
  digitalWrite(MOTOR_RIGHT_BACKWARD, LOW);
}

void loop()
{
  while (Serial.available()) // whatever the data that is coming in serially and
                             // assigning the value to the variable “data”
  {
    byte data = Serial.read();
    Serial.println(data);
    switch (data)
    {
    case '0': // FORWARD ON
      digitalWrite(MOTOR_LEFT_FORWARD, HIGH);
      digitalWrite(MOTOR_RIGHT_FORWARD, HIGH);
      break;
    case '1': // FORWARD OFF
      digitalWrite(MOTOR_LEFT_FORWARD, LOW);
      digitalWrite(MOTOR_RIGHT_FORWARD, LOW);
      break;
    case '2': // BACKWARD ON
      digitalWrite(MOTOR_LEFT_BACKWARD, HIGH);
      digitalWrite(MOTOR_RIGHT_BACKWARD, HIGH);
      break;
    case '3': // BACKWARD OFF
      digitalWrite(MOTOR_LEFT_BACKWARD, LOW);
      digitalWrite(MOTOR_RIGHT_BACKWARD, LOW);
      break;
    case '4': // LEFT ON
      digitalWrite(MOTOR_LEFT_FORWARD, LOW);
      digitalWrite(MOTOR_RIGHT_FORWARD, HIGH);
      break;
    case '5': // LEFT OFF
      digitalWrite(MOTOR_LEFT_FORWARD, LOW);
      digitalWrite(MOTOR_RIGHT_FORWARD, LOW);
      break;
    case '6': // RIGHT ON
      digitalWrite(MOTOR_LEFT_FORWARD, HIGH);
      digitalWrite(MOTOR_RIGHT_FORWARD, LOW);
      break;
    case '7': // RIGHT OFF
      digitalWrite(MOTOR_LEFT_FORWARD, LOW);
      digitalWrite(MOTOR_RIGHT_FORWARD, LOW);
      break;
    }
  }
}
