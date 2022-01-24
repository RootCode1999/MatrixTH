#include <SPI.h>
#include <RF24.h>

RF24 radio(9, 10);

void setup() {
  Serial.begin(9600);
  radio.begin();
  radio.setPALevel(RF24_PA_MAX);
  radio.setChannel(0x76);
  radio.openWritingPipe(0xF0F0F0F0E1LL);
  radio.enableDynamicPayloads();
  radio.powerUp();
}

void loop() {
  const char text[] = "HELLO";
  radio.write(&text, sizeof(text));
  Serial.println("--> SENT");
  delay(1000);

}