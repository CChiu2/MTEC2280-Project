#include "pitches.h"

int melody[] = {
  NOTE_FS2, NOTE_AS4, NOTE_F3, NOTE_G3 , NOTE_A2, NOTE_DS3, NOTE_E1, NOTE_D3,
  NOTE_F3 , NOTE_B2, NOTE_D3, NOTE_DS3, NOTE_F3, NOTE_B2, NOTE_DS3, NOTE_D3, NOTE_C3
};
int noteDurations[] = {
  3, 3, 1, 1, 2, 2, 1, 1, 9,
  3, 3, 1, 1, 2, 2, 1, 1, 9
};


String inputString = "";         // a string to hold incoming data
boolean stringComplete = false;  // whether the string is complete
const int ledPin = 8;


void setup() {
  // iterate over the notes of the melody:
  for (int thisNote = 0; thisNote < 18; thisNote++) {


    //e.g. quarter note = 1000 / 4, eighth note = 1000/8, etc.
    int noteDuration = 300 * noteDurations[thisNote];
    tone(8, melody[thisNote], noteDuration);

    //pause for the note’s duration plus 30 ms:
    delay(noteDuration + 30);
  }
  {
    Serial.begin(9600);
    // reserve 200 bytes for the inputString:
    inputString.reserve(200);
    pinMode(ledPin, OUTPUT);
  }
}

void loop() {

 SerialEvent(); //call the function
  // print the string when a newline arrives:
  if (stringComplete) {
    Serial.println(inputString);

    if (inputString == "hello") {
      for (int thisNote = 0; thisNote < 18; thisNote++)
      {

        int noteDuration = 300 * noteDurations[thisNote];
        tone(8, melody[thisNote], noteDuration);

        delay(noteDuration + 30);
      }
      state = 1;
    }
    // clear the string:
    inputString = "";
    stringComplete = false;

  }
}
/*
  SerialEvent occurs whenever a new data comes in the
  hardware serial RX.  This routine is run between each
  time loop() runs, so using delay inside loop can delay
  response.  Multiple bytes of data may be available.
*/
void serialEvent() {
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read();
    // add it to the inputString:
    // if the incoming character is a newline, set a flag
    // so the main loop can do something about it:
    if (inChar == '\n') {
      stringComplete = true;
    } else {
      inputString += inChar;
    }
  }






}


