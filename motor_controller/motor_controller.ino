#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();

#define SERVOMIN 100
#define SERVOMAX 600
#define STEP_SIZE 5
#define CONTINIOUS_MOTOR_STATIONARY_PULSE 377
#define CONTINIOUS_MOTOR_CW_PULSE 330
#define CONTINIOUS_MOTOR_CCW_PULSE 440

#define CHANNEL_CONTINIOUS_MOTOR 0
#define MOTOR_ONE 1
#define MOTOR_TWO 3
#define MOTOR_THREE 4
#define callibration_angle 90

int motor1_cur_angle = 90;
int motor2_cur_angle = 90;
int motor3_cur_angle = 90;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600); // opens serial port, sets data rate to 9600 bps
  pwm.begin();
  pwm.setPWMFreq(60);
  Serial.println("reset");
  pwm.setPWM(CHANNEL_CONTINIOUS_MOTOR, 0, CONTINIOUS_MOTOR_STATIONARY_PULSE);
  pwm.setPWM(MOTOR_ONE, 0, angleToPulse(callibration_angle, MOTOR_ONE));
  pwm.setPWM(MOTOR_TWO, 0, angleToPulse(callibration_angle, MOTOR_TWO)); 
  pwm.setPWM(MOTOR_THREE, 0, angleToPulse(callibration_angle, MOTOR_THREE));
}

/* Function to convert angle to pulse, then print status */
int angleToPulse(int angle, int motor_id){
  int pulse = map(angle, 0, 180, SERVOMIN, SERVOMAX);
  Serial.print("Motor ID: ");Serial.print(motor_id);
  Serial.print(" Angle: ");Serial.print(angle);
  Serial.print(" Pulse: "); Serial.println(pulse);
  return pulse;
}

void loop() {
  // put your main code here, to run repeatedly:
    
    if(Serial.available() > 0){
      char cmd = Serial.read(); //The arduino reads this data and writes it as one of our variables.
      Serial.print("Command: "); //The arduino prints this data to the serial monitor so we can see what it
      Serial.println(cmd);
      
      /* Motor Base Continious */
      if(cmd == 'b'){
        pwm.setPWM(CHANNEL_CONTINIOUS_MOTOR, 0, CONTINIOUS_MOTOR_CCW_PULSE);
        delay(100);  
      } else if(cmd == 'a'){
        pwm.setPWM(CHANNEL_CONTINIOUS_MOTOR, 0, CONTINIOUS_MOTOR_CW_PULSE);
        delay(100);   
      } 
      /* Motor 1 */
      else if (cmd == 'c'){
        if(motor1_cur_angle + STEP_SIZE <= 180){
          motor1_cur_angle += STEP_SIZE;
        }
      } else if (cmd == 'd'){
        if(motor1_cur_angle - STEP_SIZE > 0){
          motor1_cur_angle -= STEP_SIZE; 
        }
      } 

      /* Motor 2 */
      else if (cmd == 'e'){
        if(motor2_cur_angle + STEP_SIZE <= 180){
          motor2_cur_angle += STEP_SIZE;
        }
      } else if (cmd == 'f'){
        if(motor2_cur_angle - STEP_SIZE > 0){
          motor2_cur_angle -= STEP_SIZE; 
        }
      }

       /* Motor 3 */
      else if (cmd == 'g'){
        if(motor3_cur_angle + STEP_SIZE <= 180){
          motor3_cur_angle += STEP_SIZE;
        }
      } else if (cmd == 'h'){
        if(motor3_cur_angle - STEP_SIZE > 0){
          motor3_cur_angle -= STEP_SIZE; 
        }
      }

      else if(cmd == 'x'){
        motor1_cur_angle = callibration_angle;
        motor2_cur_angle = callibration_angle;
        motor3_cur_angle = callibration_angle;
        setup();
      }
       pwm.setPWM(CHANNEL_CONTINIOUS_MOTOR, 0, CONTINIOUS_MOTOR_STATIONARY_PULSE);  
       pwm.setPWM(MOTOR_ONE, 0, angleToPulse(motor1_cur_angle, MOTOR_ONE));
       pwm.setPWM(MOTOR_TWO, 0, angleToPulse(motor2_cur_angle, MOTOR_TWO)); 
       pwm.setPWM(MOTOR_THREE, 0, angleToPulse(motor3_cur_angle, MOTOR_THREE));
    }
}
