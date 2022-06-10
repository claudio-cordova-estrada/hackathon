int valorPulsador = 1;

void setup(){
  Serial.begin(9600);
  pinMode(5, INPUT);
}

void loop(){
  if(digitalRead(5) == HIGH){
    if(digitalRead(5) == LOW){
      Serial.println(valorPulsador);
    }
  }
}
