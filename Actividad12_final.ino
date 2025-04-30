#include "BluetoothSerial.h"
#define PIN_ANALOGICO_X 34
#define PIN_ANALOGICO_Y 35
BluetoothSerial SerialBT;

void setup() {
  Serial.begin(115200);
  SerialBT.begin("ESP32_POULET"); // Inicia puerto serial y establece el nombre del dispositivo
  Serial.println("Esperando conexion Bluetooth..."); 
}

void loop() {
  if(SerialBT.available()) { // mientras el dispositivo este disponible 
    // Los valores analógicos y prepara mensaje
    int valor_x = analogRead(PIN_ANALOGICO_X);
  int valor_y = analogRead(PIN_ANALOGICO_Y);
  float x = (float)valor_x / 4095.0;
  float y = (float)valor_y / 4095.0;
  
  // Formato: "x, y" ->"0.025, 0.364"
    String message = String(x)+ "," + String(y);
    // Envío del mensaje
    SerialBT.println(message);
      SerialBT.println("Enviando: " + message);
      delay(50);
  }  
}
