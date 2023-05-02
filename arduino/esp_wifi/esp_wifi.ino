
/* This example is written for Nodemcu Modules */

#include "ESP_Wahaj.h" // importing our library

int left = 16; // pin D0
int middle = 5; // pin D1
int right = 4; // pin D2

String path = "nothing";
void setup(){
  Serial.begin(9600);
  start("dlink-FB82","oikzd47889");  // Wifi details connect to
  // initialize GPIO 5 as an output

  pinMode(left, OUTPUT);
  pinMode(middle, OUTPUT);
  pinMode(right, OUTPUT);
}

void loop(){
  //waitUntilNewReq();  //Waits until a new request from python come

  if(CheckNewReq() == 1)
  {
    Serial.println(getPath());
    if (getPath()=="/1"){
      digitalWrite(left, HIGH); // turn the LED on
      digitalWrite(middle, LOW); // turn the LED on
      digitalWrite(right, LOW); // turn the LED on
      delay(10); // wait for 10ms
    returnThisStr("1");
    }
    else if (getPath()=="/2"){
      digitalWrite(left, HIGH); // turn the LED on
      digitalWrite(middle, HIGH); // turn the LED on
      digitalWrite(right, LOW); // turn the LED on
      delay(10); // wait for 10ms
    returnThisStr("2");
    }
    else if (getPath()=="/3"){
      digitalWrite(left, LOW); // turn the LED on
      digitalWrite(middle, HIGH); // turn the LED on
      digitalWrite(right, LOW); // turn the LED on
      delay(10); // wait for 10ms
    returnThisStr("3");
    }
    else if (getPath()=="/4"){
      digitalWrite(left, LOW); // turn the LED on
      digitalWrite(middle, HIGH); // turn the LED on
      digitalWrite(right, HIGH); // turn the LED on
      delay(10); // wait for 10ms
    returnThisStr("4");
    }
    else if (getPath()=="/5"){
      digitalWrite(left, LOW); // turn the LED on
      digitalWrite(middle, LOW); // turn the LED on
      digitalWrite(right, HIGH); // turn the LED on
      delay(10); // wait for 10ms
    returnThisStr("5");
    }
    else if (getPath()=="/6"){
      digitalWrite(left, HIGH); // turn the LED on
      digitalWrite(middle, HIGH); // turn the LED on
      digitalWrite(right, HIGH); // turn the LED on
      delay(10); // wait for 10ms
    returnThisStr("6");
    }

    else        //here we receive data. You can receive pwm255 and the decode it to 255 and also get more variables like this
    {
      path = getPath();
      Serial.println(path);
    }
    
  }
  
//Serial.println("tesiting....");
//if(pwm == 255) Serial.println("highhhhh");
//if(pwm == 0) Serial.println("lowwwwsssh");
//analogWrite(led,pwm);
  
}