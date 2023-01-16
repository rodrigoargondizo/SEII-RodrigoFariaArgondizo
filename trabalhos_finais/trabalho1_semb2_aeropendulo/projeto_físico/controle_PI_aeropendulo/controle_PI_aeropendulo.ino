  // Controle PID

int pot_angulo = A0;
int pot_referencia = A1;
int motor = 6;
int erro = 0;
int controle = 0;


float tempo_antigo = 0;
float tempo = 0;
float delta_t = 0;

int erro_antigo = 0;
int delta_erro = 0;
//Derivada
float derivada = 0;
// Integral
float integral = 0;
float integral_antiga = 0;
void setup() {
  pinMode(motor, OUTPUT);
  Serial.begin(9600);
  }

void loop() {
 float kp = 0.3;
 float kd = 0;
 float ki = 1.5;
 
  int referencia = map(analogRead(pot_referencia), 0, 1023, 60, 120); //Leitura do setpoint
  int angulo = map(analogRead(pot_angulo), 0, 600, 0, 200); //Leitura do angulo

  // Declaracao do valor do controle
  erro = angulo - referencia;
  controle = floor(abs(kp * ( erro + kd * derivada + ki * integral)));

  Serial.print("Angulo: ");
  Serial.print(angulo);
  Serial.print(" Referencia: ");
  Serial.print(referencia);
  Serial.print(" Controle: ");
  Serial.println(controle);
  // Controle
  //if(angulo < referencia){
    analogWrite(motor, controle);
   // }else{
     // if((75 - controle) >= 0){
       // analogWrite(motor, (75 - controle));
      //}else{
        //digitalWrite(motor, LOW);
      //}
    //}

      tempo = millis();
      delta_t = tempo - tempo_antigo;
      integral = integral_antiga + erro * delta_t;
      delta_erro = erro - erro_antigo;
      derivada = delta_erro/delta_t;
      erro_antigo = erro;
      tempo_antigo = tempo;
      integral_antiga = integral;
}

