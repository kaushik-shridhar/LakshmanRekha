#include<ESP8266WiFi.h>

// credentials
#define HOST "" // host URL or IP address
#define WIFI_SSID "Shridhar" // WiFi name
#define WIFI_PASSWORD "9322238787" // WiFi password

// connecting to the network
void connect_wifi() {
  // connecting to the specified network
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  Serial.print("Connecting...");
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(1000);
  }
  Serial.println();
  Serial.print("Connected, IP address : ");
  Serial.println(WiFi.localIP()); // IP address of the device
}

// scan for nearby access points and their signal strengths
void scan_wifi() {
  Serial.println("Scan started...");

  // get the total number of scanned networks
  int n = WiFi.scanNetworks();

  if (n == 0) {
    Serial.println("No networks found");
  } else {
    for (int i=0;i<n;i++) {
      Serial.print("WiFi SSID : ");
      Serial.println(WiFi.SSID(i));
      Serial.print("WiFi RSSI : ");
      Serial.println(WiFi.RSSI(i));
      Serial.println("-------------------------");
    }
  }
}
