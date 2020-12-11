#include<ESP8266WiFi.h>
#include<ESP8266HTTPClient.h>

// credentials
#define HOST "" // host URL or IP address
#define WIFI_SSID "Shridhar" // WiFi name
#define WIFI_PASSWORD "9322238787" // WiFi password

// declare global variables to be uploaded to the server
String ssid, rssi, send_ssid, send_rssi, post_data;

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
      ssid = WiFi.SSID(i);
      Serial.println(ssid);
      Serial.print("WiFi RSSI : ");
      rssi = WiFi.RSSI(i);
      Serial.println(rssi);
      //send_data();
      Serial.println("-------------------------");
    }
  }
}

// send data to the web server
void send_data() {
  HTTPClient http; // creating object of HTTPClient

  // storing the values to be sent to the server
  send_ssid = ssid;
  send_rssi = rssi;

  post_data = "ssid=" + send_ssid + "&rssi=" + send_rssi;

  http.begin("http://192.168.1.5:8000/tracking/"); // connect to the host where the server is hosted(IP needs to be updated)
  http.addHeader("Content-Type", "application/x-www-form-urlencoded"); // specify the content-type header

  int http_code = http.POST(post_data);
  Serial.println("Values sent are : " + send_ssid + ", " + send_rssi);

  // if connection established then do this
  if (http_code == 200) {
    Serial.println("Value uploaded successfully.");
    Serial.println(http_code);
    String webpage = http.getString(); // get webpage output and store it in a string
    Serial.println(webpage + "\n");
  } else { // if failed to connect then return and restart
    Serial.println(http_code);
    Serial.println("Failed to upload values. \n");
    http.end();
    return;
  }

  delay(3000);
  digitalWrite(LED_BUILTIN, LOW);
  delay(3000);
  digitalWrite(LED_BUILTIN, HIGH);
}
