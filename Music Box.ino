// defines pins numbers
const int trigPin1 = 9;
const int echoPin1 = 10;
const int trigPin2 = 3;
const int echoPin2 = 4;

// defines variables
long duration1;
int distance1;
long duration2;
int distance2;

int a = 0;

void setup() {
    pinMode(trigPin1, OUTPUT); // Sets the trigPin as an Output
    pinMode(echoPin1, INPUT); // Sets the echoPin as an Input
    pinMode(trigPin2, OUTPUT); // Sets the trigPin as an Output
    pinMode(echoPin2, INPUT); // Sets the echoPin as an Input
    Serial.begin(9600); // Starts the serial communication
}

void loop() {
    // Clears the trigPin
    digitalWrite(trigPin1, LOW);
    digitalWrite(trigPin2, LOW);
    delayMicroseconds(2);
    
    digitalWrite(trigPin1, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin1, LOW);
    duration1 = pulseIn(echoPin1, HIGH);

    digitalWrite(trigPin2, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin2, LOW); 
    duration2 = pulseIn(echoPin2, HIGH);
    
    // Calculating the distance
    distance1 = duration1*0.034/2;
    distance2 = duration2*0.034/2;


    if (a == 0){
        if (distance1 <= 20 && distance2 <= 20){
            Serial.print("1");
            delay(1000);
        }
        else if (distance1 <= 20 && distance2 > 20){
            a = 1;
            delayMicroseconds(100);
        }
        else if (distance2 <= 20 && distance1 > 20){
            a = 2;
            delayMicroseconds(100);
        }
    }
    else if (a == 1){
      if (distance2 <= 20){
          a = 0;
          Serial.print("2");
          delay(1000);      
      }
    }
    else if (a == 2){
        if (distance1 <= 20){
          a = 0;
          Serial.print("3");
          delay(1000);      
      }
    }
    
    // Prints the distance on the Serial Monitor
//    Serial.print("Distance1: ");
//    Serial.println(distance1);
//    Serial.print("Distance2: ");
//    Serial.println(distance2);
}
