#define Relay 13
#define buzzer A0
static const int sensorPin = 10;                    // sensor input pin 
int SensorStatePrevious = LOW;                      // previousstate of the sensor

unsigned long minSensorDuration = 3000; // Time we wait before  the sensor active as long 
unsigned long minSensorDuration2 = 6000;
unsigned long SensorLongMillis;                // Time in ms when the sensor was active
bool SensorStateLongTime = false;                  // True if it is a long active

const int intervalSensor = 50;                      // Time between two readings sensor state
unsigned long previousSensorMillis;                 // Timestamp of the latest reading

unsigned long SensorOutDuration;                  // Time the sensor is active in ms

//// GENERAL ////

unsigned long currentMillis;          // Variabele to store the number of milleseconds since the Arduino has started

void setup() {
  Serial.begin(9600);                 // Initialise the serial monitor

  pinMode(sensorPin, INPUT);          // set sensorPin as input
  Serial.println("Press button");
  pinMode(Relay,OUTPUT);
  pinMode(buzzer,OUTPUT);
}

// Function for reading the sensor state
void readSensorState() {

  // If the difference in time between the previous reading is larger than intervalsensor
  if(currentMillis - previousSensorMillis > intervalSensor) {
    
    // Read the digital value of the sensor (LOW/HIGH)
    int SensorState = digitalRead(sensorPin);    

    // If the button has been active AND
    // If the sensor wasn't activated before AND
    // IF there was not already a measurement running to determine how long the sensor has been activated
    if (SensorState == LOW && SensorStatePrevious == HIGH && !SensorStateLongTime) {
     SensorLongMillis = currentMillis;
       SensorStatePrevious = LOW;
      
      Serial.println("Button pressed");
    }

    // Calculate how long the sensor has been activated
   SensorOutDuration = currentMillis - SensorLongMillis;

    // If the button is active AND
    // If there is no measurement running to determine how long the sensor is active AND
    // If the time the sensor has been activated is larger or equal to the time needed for a long active
    if (SensorState == LOW && !SensorStateLongTime && SensorOutDuration >= minSensorDuration) {
      SensorStateLongTime = true;
      digitalWrite(Relay,HIGH);
      Serial.println("Button long pressed");
    }
    if (SensorState == LOW && SensorStateLongTime && SensorOutDuration >= minSensorDuration2) {
     SensorStateLongTime = true;
      digitalWrite(buzzer,HIGH);
      delay(1000);
      Serial.println("Button long pressed");
    }
      
    // If the sensor is released AND
    // If the sensor was activated before
    if (SensorState == HIGH && SensorStatePrevious == LOW) {
      SensorStatePrevious = HIGH;
      SensorStateLongTime = false;
      digitalWrite(Relay,LOW);
      digitalWrite(buzzer,LOW);
      Serial.println("Button released");

  
    }
    
    // store the current timestamp in previousSensorMillis
   previousSensorMillis = currentMillis;

  }

}