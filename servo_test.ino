#include<Servo.h>

Servo servoHor;

int y;

int prevX;

void setup()
{
  Serial.begin(115200);
  servoHor.attach(9);
  servoHor.write(90);
//  delay(15);
  
}

void Posi(int x)
{

//    Serial.print(x);
    int servoX = map(x,190,503,0,180); //x,190,503,70,179

    servoX = min(servoX,180);
    servoX = max(servoX,1);

//    Serial.print('lol");
    Serial.print(servoX);
    delay(2);
    servoHor.write(servoX);
    delay(2);
    
    
  
}

void loop()


{
  if (Serial.available() > 0) {

    int incomingByte = Serial.readString().toInt(); //prints ascii representation


      
    
   
//
//    
//      Serial.print(incomingByte);
      Posi(incomingByte);

  }
}
  
