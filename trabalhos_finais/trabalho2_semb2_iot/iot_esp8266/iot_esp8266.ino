#include<ESP8266WiFi.h>

const char* ssid = "Pedro 2.4";
const char* password = "Pedrolindo7";


//IP FIXO PARA O NODEMCU 
IPAddress ip(192,168,0,144);
IPAddress gateway(192,168,1,1);
IPAddress subnet(255,255,255,0);

WiFiServer server(80);

#define led_1 4
#define led_2 5

bool led1Status = false;
bool led2Status = false;

void requisicao(String);

//PAGINA HTML
#include "pagina.h"

void setup(){

Serial.begin(115200);
delay(10);

pinMode(led_1, OUTPUT);
digitalWrite(led_1, !led1Status);

pinMode(led_2, OUTPUT);
digitalWrite(led_2, !led2Status);

Serial.println("");
Serial.println("");
Serial.print("conectando a: ");
Serial.print(ssid);

WiFi.begin(ssid, password);
WiFi.config(ip, gateway, subnet);

while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
 
 Serial.println("");
 Serial.print("Conectado a rede sem fio ");
 Serial.println(ssid);
 server.begin();
 Serial.println("Servidor Iniciado");
 
 Serial.print("IP para se conectar: ");
 Serial.print("http://");
 Serial.println(WiFi.localIP());
 }
 
 
 void loop(){
 
 WiFiClient client = server.available();
 if (!client){
 return;
 }
 Serial.println("Novo cliente");
 while(!client.available()){
 delay(1);
}
 
String request = client.readStringUntil('\r');
requisicao(request);
Serial.println(request);

 
String request2 = client.readStringUntil('\r');
requisicao2(request2);
Serial.println(request2);


 
 client.flush();
 client.println("HTTP/1.1 200 OK");
 client.println("Content-Type: text/html"); 
 client.println("");
 client.println(pagina);
 
 
 client.println("<section>");
 client.println("<div class='item-head'>");
 client.println("<div class='titulo'>LED 1</div>");
 led1Status ? client.println("<div class='estado on'>on</div>") : client.println("<div class='estado off'>off</div>");
 client.println("</div>");
 client.println("<div class='acoes'>");
 client.println("<a href='/LED=ON' class='ligar'>ligar</a>");
 client.println("<a href='/LED=OFF' class='desligar'>desligar</a>");
 client.println("</div>");
 client.println("</section>");


 client.println("<section>");
 client.println("<div class='item-head'>");
 client.println("<div class='titulo'>LED 2</div>");
 led2Status ? client.println("<div class='estado on'>on</div>") : client.println("<div class='estado off'>off</div>");
 client.println("</div>");
 client.println("<div class='acoes'>");
 client.println("<a href='/LED2=ON' class='ligar'>ligar</a>");
 client.println("<a href='/LED2=OFF' class='desligar'>desligar</a>");
 client.println("</div>");
 client.println("</section>");
 


client.println("<section>");
client.println("<div class='item-head'>");
client.println("<div class='titulo'>Temperatura Ambiente</div>");
client.println("</div>");
client.println("<div class='acoes'>");
client.println("<div class='leitura'>23°C</div>");
client.println("</div>");
client.println("</section>");
 
 client.println(rodape);
 delay(1);
 
 Serial.println("Cliente desconectado");
 Serial.println("");
 
 }
 
 void requisicao(String request){
 
 if(request.indexOf("/LED=ON") != -1)
 {
  led1Status = true;
  digitalWrite(led_1, led1Status);
 }
 
  if(request.indexOf("/LED=OFF") != -1)
 {
  led1Status = false;
  digitalWrite(led_1, led1Status);
 }

 }

void requisicao2(String request2){
 
  if(request2.indexOf("/LED2=ON") != -1)
 {
  led2Status = true;
  digitalWrite(led_2, led2Status);
 }
 
  if(request2.indexOf("/LED2=OFF") != -1)
 {
  led2Status = false;
  digitalWrite(led_2, led2Status);
 }
}
