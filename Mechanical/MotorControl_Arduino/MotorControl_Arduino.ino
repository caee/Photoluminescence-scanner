// Include the AccelStepper library:
#include <AccelStepper.h>
#include <Scheduler.h> // for multithreading

// Define stepper motor connections and motor interface type. Motor interface type must be set to 1 when using a driver:
//Step pins
#define X1_STEP 2
#define X2_STEP 4
#define U1_STEP 6
#define U2_STEP 8

//Direction Pins
#define X1_DIR 3
#define X2_DIR 5
#define U1_DIR 7
#define U2_DIR 9

//Enable pins
#define X1_EN
#define X2_EN
#define U1_EN
#define U2_EN

//Alarm pins
#define X1_ALM
#define X2_ALM
#define U1_ALM
#define U2_ALM

//End Stops
#define endX1_min
#define endX1_max
#define endU1_mix
#define endU1_max



#define motorInterfaceType 1

String mydata;
int rev = 0;
int dir = 0;
int spd = 0;
int motor = 0;

const int stepperAmount = 4;
const int ACCEL=800;
const int SPEED=2000;
//int positionArray[] = {500, 0, 1000}; 
// Create a new instance of the AccelStepper class:
AccelStepper stepperx1 = AccelStepper(motorInterfaceType, stepPin1, dirPin1);
AccelStepper stepperx2 = AccelStepper(motorInterfaceType, stepPin2, dirPin2);
AccelStepper stepperu1 = AccelStepper(motorInterfaceType, stepPin3, dirPin3);
AccelStepper stepperu2 = AccelStepper(motorInterfaceType, stepPin4, dirPin4);
//A bit from https://forum.arduino.cc/t/solved-accelstepper-library-and-multiple-stepper-motors/379416/2
AccelStepper* steppers[stepperAmount] ={
    
    &stepperx1,
    &stepperx2,
    &stepperu1,
    &stepperu2
};

void homingX(){
  bool homingComplete = false;
  bool x1Home = false;
  bool x2Home = falsel
  while(homingComplete == false) {
    if (digitalRead(endX1_min) {
        stepperx1.moveTo(initial_homing_stepperX);  // Set the position to move to
        initial_homing_stepperX--;
        stepperx1.run(); 
    }
    else {
        xHome = true;
    }
    // likewise for stepper X2
    if (digitalRead(endX2_min) {
        stepperx1.moveTo(initial_homing_stepperX);  // Set the position to move to
        initial_homing_stepperX--;
        stepperx1.run(); 
    }
    else {
        xHome = true;
    }
    if (xHome == true and yHome == true) {
        homingComplete = true;
    }
  }
}

void setup() {
  //Scheduler.startLoop(loop2); // for multithreading. 
  //Scheduler.startLoop(loop3); // for multithreading. 
  //Scheduler.startLoop(loop4); // for multithreading. 
  // Set the maximum speed and a cceleration:
  /*stepper1.setMaxSpeed(50);
  stepper1.setAcceleration(500);
  stepper1.setMinPulseWidth(10);
  stepper2.setMaxSpeed(50);
  stepper2.setAcceleration(500);
  stepper2.setMinPulseWidth(10);*/
  //now i can just make a for loop and iterate through the steppers array and call whatever function I want
  //Note: you have to use -> to call that function instead of a .

  for(int stepperNumber = 0; stepperNumber < stepperAmount; stepperNumber++){
      steppers[stepperNumber]->setMaxSpeed(SPEED);
      steppers[stepperNumber]->setAcceleration(ACCEL);
      steppers[stepperNumber]->setMinPulseWidth(10); //Since we are only supplying 3.3V
  }
  Serial.begin(500000);
}

void loop() {
  while (Serial.available() == 0);
  dir = mydata.substring(0, 1).toInt();
  rev = mydata.substring(2, 5).toInt();
  spd = mydata.substring(6, 9).toInt();
  motor = mydata.substring(10,13).toInt();
  Serial.print(motor);
  //https://forum.arduino.cc/t/convert-int-to-binary-array/116781/3
  for (byte i=0; i<stepperAmount; i++){
    byte state = bitRead(motor, i);
    //digitalWrite(pins[i], state);
    Serial.print(state);
  }
  Serial.println();

  
  //Set the target position:
  for(int stepperNumber = 0; stepperNumber < stepperAmount; stepperNumber++){
    
        steppers[stepperNumber]->moveTo(positionArray[stepperNumber]);
    
    }
  //Run all steppers needed
    for(int stepperNumber = 0; stepperNumber < stepperAmount; stepperNumber++){
    
        steppers[stepperNumber]->run();
    
    }
  
}
  // Set the target position:
  /*for(int stepperNumber = 0; stepperNumber < stepperAmount; stepperNumber++){
    
        steppers[stepperNumber]->moveTo(positionArray[stepperNumber]);
    
    }

    for(int stepperNumber = 0; stepperNumber < stepperAmount; stepperNumber++){
    
        steppers[stepperNumber]->run();
    
    }*/
 /*
  //stepper1.moveTo(positionArray[1]);
  if(
  stepper1.moveTo(2000);
  stepper1.runToPosition();
  delay(10);
}

void loop2(){
  stepper2.moveTo(4000);
  stepper2.runToPosition();
  delay(10);
}
void loop3(){
  stepper3.moveTo(6000);
  stepper3.runToPosition();
  delay(10);
}
void loop4(){
  stepper4.moveTo(8000);
  stepper4.runToPosition();
  delay(10);
}
*/
