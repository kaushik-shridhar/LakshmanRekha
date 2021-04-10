// ------------------------- scan for available SSID and their RSSI
void scanWiFi() {
  Serial.println("Scan started...");

  int n = WiFi.scanNetworks();

  a = "";

  if (n == 0) {
    Serial.println("No networks found");
  } else {
    for (int i = 0; i < n; i++) {
      if (WiFi.SSID(i) == "Shetty_23" || WiFi.SSID(i) == "Shetty" || WiFi.SSID(i) == "Shetty_room1") {
        ssid = WiFi.SSID(i);
        int sum = 0;
        String rssi_str = "";
        int rssi_int = 0;
        for (int j=0;j<6;j++) {
          rssi_str = WiFi.RSSI(i);
          rssi_int += rssi_str.toInt();
        }
        rssi_int = rssi_int / 6;
        rssi = String(rssi_int);
        a += ssid+"/"+rssi+"/"+uid+"/"+floor_name+",";
      }
    }
  }
}

// ------------------------- send the AP data to the server
void sendData() {
  HTTPClient http;

  post_data = "a="+a;

  http.begin("http://192.168.29.132:8000/tracking/recieve/");
//  http.begin("http://192.168.0.107:8000/tracking/recieve/");
  http.addHeader("Content-Type", "application/x-www-form-urlencoded");

  http_code = http.POST(post_data);
  Serial.println(post_data);

  if (http_code == 200) {
    Serial.println("Send Data Values uploaded successfully");
  } else {
    Serial.println(http_code);
    Serial.println("Failed to upload send data values. \n");
    http.end();
    return;
  }
}

void liveData() {
  HTTPClient http;

  post_data = "a="+a;

  http.begin("http://192.168.29.132:8000/tracking/stream/");
//  http.begin("http://192.168.0.107:8000/tracking/stream/");
  http.addHeader("Content-Type", "application/x-www-form-urlencoded");

  http_code = http.POST(post_data);
  Serial.println(post_data);

  if (http_code == 200) {
    Serial.println("Live Data Values uploaded successfully");
  } else {
    Serial.println(http_code);
    Serial.println("Failed to upload live data values. \n");
    http.end();
    return;
  }
}
