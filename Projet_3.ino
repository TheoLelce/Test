
const byte numReaders = 1;
int numG = 5; // Number of Goal that you need to win

int ledR = 8; // Red led pin
int ledB = 9; // Blue led pin
int led = 10 ; //  led pin (allow to read the secret message)
byte buzzerpin = 11; // Buzzer Pin 
int  digitalPin1 = 4; // KY-025 digital interface
int  digitalPin2 = 3; // KY-025 digital interface 
int analogPin = A0; // KY-025 analog interface
int analogPin2 = A1; // KY-025 analog interface
int digitalVal; // digital readings

void setup() {
  // put your setup code here, to run once:
  // Configure the output and input pin
  pinMode (ledR, OUTPUT);
  pinMode (ledB, OUTPUT);
  pinMode (led, OUTPUT);
  pinMode(digitalPin1, INPUT);
  pinMode(digitalPin2, INPUT);
  // Initialise serial connection
  Serial.begin(9600);

}


void loop() {
  //When succefully score 5 goal ligth the led 
if( numG == 0){ 
   
   digitalWrite(led, HIGH);
   delay(200000);
   digitalWrite(led, LOW);
   numG = 5;
   
} else {
  // chose what side will score a goal 
    int Num = random(1,3);
   
    if (Num == 1){
      // make sound to indicate the side were you need to score
      tone(buzzerpin, 500,200);
      delay(200);
      tone(buzzerpin, 600,200);
      delay(200); 
      tone(buzzerpin, 700,200);
      delay(200);
      noTone(buzzerpin);
      delay(1000);
       int e = 0;  
       
      for( int e = 0; e< 75; e++){
      tone(buzzerpin, 500,50); 
      noTone(buzzerpin);
      delay(100);
      }
      delay(1000);
      digitalVal = digitalRead(digitalPin1); 
      // if the goal is done trigger sound and led 
      if(digitalVal == HIGH){
       
        numG--;
        tone(buzzerpin, 500);
        digitalWrite(ledB, HIGH);
        playPassed();
        delay(1000);
        noTone(buzzerpin);
        digitalWrite(ledB, LOW);
      } else{
       
        playFailed();
        delay(2000);
      }
    } else {
      // make sound to indicate the side were you need to score
    tone(buzzerpin, 500,200);
      delay(200);
      tone(buzzerpin,400,200);
      delay(200); 
      tone(buzzerpin, 300,200);
      delay(200);
    for( int e = 0; e< 75; e++){
      tone(buzzerpin, 500,50); 
      noTone(buzzerpin);
      delay(100);
      }
    delay(1000);
    // if the goal is done trigger sound and led 
      digitalVal = digitalRead(digitalPin2); 
      if(digitalVal == HIGH){
   µ
        numG--;
        digitalWrite(ledR, HIGH);
        playPassed();
        delay(1000);
        digitalWrite(ledR, LOW);
        noTone(buzzerpin);
        } else{
       
          playFailed();
          delay(2000);
    }
  } 
    } 
  }
//source https://www.aranacorp.com/fr/utilisation-dun-buzzer-avec-arduino/
void playPassed() { /* function playPassed */
  ////Play 'ON' Sound
  int melodyOn[] = {523, 1047, 587, 1760};
  int durationOn = 200;
  for (int thisNote = 0; thisNote < 4; thisNote++) {
    tone(buzzerpin, melodyOn[thisNote], durationOn);
    delay(200);
  }
}

void playFailed() { /* function playFailed */
  ////Play 'OFF' Sound
  int melodyOff[] = {131, 147};
  int durationOff = 200;
  for (int thisNote = 0; thisNote < 2; thisNote++) {
    tone(buzzerpin, melodyOff[thisNote], durationOff);
    delay(200);
  }
}
