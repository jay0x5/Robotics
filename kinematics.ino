#include <Servo.h>

Servo Hipservo;  // create servo object to control a servo

void setup() {
//  Hipservo.attach(9);  // attaches the servo on pin 9 to the servo object
  
}

void loop() {
  int thighLength = 100; //Side B
  int HipToGroundlength = 190; //Side C
  int FemurLength = 100; //Side A
  float hipangleA;
  float hipangleA2;
  float hipangleAfinal;
  float acosfunc;
  float CosAtoDegress;

  //calculate up and down angle
  hipangleA = sq(thighLength) + sq(HipToGroundlength) - sq(FemurLength);
  hipangleA2 = 2 * thighLength * HipToGroundlength;
  hipangleAfinal = hipangleA /hipangleA2;
  acosfunc = acosf(hipangleAfinal);
  CosAtoDegress = acosfunc * (180/PI);
  Serial.print(CosAtoDegress);
  
// Hipservo.write(val)
}
