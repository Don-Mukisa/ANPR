#include <Arduino_OV767X.h>

void setup() {
  Serial.begin(9600);
  if (!Camera.begin(QQVGA, GRAYSCALE)) { // start the camera
    Serial.println("CAMERA INIT FAILED");
    return;
  }
}

void loop() {
  Camera.readFrame();
  for (int i = 0; i < Camera.width(); i++) {
    for (int j = 0; j < Camera.height(); j++) {
      byte pixel = Camera.getPixel(i, j);
      Serial.write(pixel);
    }
  }
  delay(1000); // delay between each frame
}
