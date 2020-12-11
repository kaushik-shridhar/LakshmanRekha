void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  connect_wifi();
//  scan_wifi();
//  send_data();

}

void loop() {
  // put your main code here, to run repeatedly:
  scan_wifi();
  send_data();

}
