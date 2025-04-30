#include "BluetoothSerial.h"
BluetoothSerial SerialBT;

void setup() {
  Serial.begin(115200);
  SerialBT.begin("ESP32_POULET"); // Inicia puerto serial y establece el nombre del dispositivo
  Serial.println("Esperando conexion Bluetooth..."); 
}

void loop() {
  if(SerialBT.available()) { // mientras el dispositivo este disponible 
  // Recepcion
    String incoming = SerialBT.readStringUntil('\n');
    Serial.print("Mensaje recibido");
    Serial.println(incoming);
    
    // Envio
      SerialBT.println("Mensaje recibido: " + incoming);
  }  
}
