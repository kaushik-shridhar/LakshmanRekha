#include<ESP8266WebServer.h>
#include<ESP8266WiFi.h>
#include<ESP8266HTTPClient.h>
#include<EEPROM.h>
#include<String>

String st;
String content;
int statusCode;

// ------------------------- WiFi credentials
const char *WIFI = "Shetty_23";
const char *PASS = "Shinit5201";
String wifi_ssid = "Shetty_23";
String wifi_pass = "";
// -------------------------

// ------------------------- user and device details
String patient_name = "";//"Shinit";
String uid = WiFi.macAddress();
String floor_name = "";//"table";
String org = "";
// -------------------------

// ------------------------- access points details for positioning
String ssid;
String rssi;
String a;
// -------------------------

// ------------------------- details to send to the server
String user_data;
String post_data;
int http_code;
// -------------------------

// ------------------------- Function Decalration
bool testWifi(void);
void launchWeb(void);
void setupAP(void);

// ------------------------- object of HTTPClient
HTTPClient http;

// ------------------------- Establishing Local server at port 80 whenever required
ESP8266WebServer server(80);

void setup() {
//    EEPROM.begin(512);
//  // write a 0 to all 512 bytes of the EEPROM
//  for (int i = 0; i < 512; i++) {
//    EEPROM.write(i, 0);
//  }
//  EEPROM.end();
//  // put your setup code here, to run once:
  //  pinMode(LED_BUILTIN, OUTPUT);

  //  Serial.begin(115200);
  //
  //  // ------------------------- connect to wifi
  //
  //  WiFi.begin(WIFI, PASS);
  //
  //  while (WiFi.status() != WL_CONNECTED) {
  //    Serial.print("*");
  //    delay(2000);
  //  }
  //
  //  Serial.println("");
  //  Serial.println("WiFi connected");
  //
  //  Serial.print("Device MAC: ");
  //  Serial.println(WiFi.macAddress());

  // -------------------------

  Serial.begin(115200); //Initialising if(DEBUG)Serial Monitor
  Serial.println();
  Serial.println("Disconnecting previously connected WiFi");
  WiFi.disconnect();
  EEPROM.begin(512); //Initialasing EEPROM
  delay(10);
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.println();
  Serial.println();
  Serial.println("Startup");

  // ------------------------- read EEPROM for SSID
  Serial.println("Reading EEPROM SSID");
//  String esid = "";
  wifi_ssid = "";
  for (int i = 0; i < 32; i++) {
//    esid += char(EEPROM.read(i));
     wifi_ssid += char(EEPROM.read(i));
  }
  Serial.println();
  Serial.println("SSID: ");
  Serial.println(wifi_ssid);

  // ------------------------- read EEPROM for PASSWORD
  Serial.println("Reading EEPROM PASSWORD");
  wifi_pass = "";
//  String epass = "";
  for (int i = 32; i < 64; i++) {
//    epass += char(EEPROM.read(i));
    wifi_pass += char(EEPROM.read(i));
  }
  Serial.println();
  Serial.println("PASSWORD: ");
  Serial.println(wifi_pass);

  // ------------------------- read EEPROM for PATIENT
  Serial.println("Read EEPROM PATIENT");
  patient_name = "";
//  String epatient = "";
  for (int i = 64; i < 96; i++) {
//    epatient += char(EEPROM.read(i));
    patient_name += char(EEPROM.read(i));
  }
  Serial.println();
  Serial.println("PATIENT: ");
  Serial.println(patient_name);

  // ------------------------- read EEPROM for FLOOR_NAME
  Serial.println("Read EEPROM FLOOR_NAME");
  floor_name = "";
//  String efloor = "";
  for (int i = 96; i < 128; i++) {
//    efloor += char(EEPROM.read(i));
    floor_name += char(EEPROM.read(i));
  }
  Serial.println();
  Serial.println("FLOOR_NAME: ");
  Serial.println(floor_name);

  // reading org
  org = "";
  for (int i=128;i<160;i++) {
    org += char(EEPROM.read(i));
  }
  Serial.println();
  Serial.println("ORG: ");
  Serial.println(org);


//  WiFi.begin(esid.c_str(), epass.c_str());
//  WiFi.begin(wifi_ssid.str(), wifi_pass.str());
  WiFi.begin(wifi_ssid, wifi_pass);
  if (testWifi())
  {
    Serial.println("Succesfully Connected!!!");
    validateUser();
    return;
  }
  else
  {
    Serial.println("Turning the HotSpot On");
    launchWeb();
    setupAP();// Setup HotSpot
  }

  Serial.println();
  Serial.println("Waiting.");

  while ((WiFi.status() != WL_CONNECTED))
  {
    Serial.print(".");
    delay(2000);
    server.handleClient();
  }
  validateUser();

  //  validateUser();
}

void loop() {
  // put your main code here, to run repeatedly:
  if (WiFi.status() == WL_CONNECTED) {
    digitalWrite(LED_BUILTIN, HIGH);
    scanWiFi();
    sendData();
    liveData();
    digitalWrite(LED_BUILTIN, LOW);
  } else {
    
  }
//  scanWiFi();
//  sendData();
//  liveData();
}

//-------- Fuctions used for WiFi credentials saving and connecting to it which you do not need to change
bool testWifi(void)
{
  int c = 0;
  Serial.println("Waiting for Wifi to connect");
  while ( c < 20 ) {
    if (WiFi.status() == WL_CONNECTED)
    {
      return true;
    }
    delay(500);
    Serial.print("*");
    c++;
  }
  Serial.println("");
  Serial.println("Connect timed out, opening AP");
  return false;
}

void launchWeb()
{
  Serial.println("");
  if (WiFi.status() == WL_CONNECTED)
    Serial.println("WiFi connected");
  Serial.print("Local IP: ");
  Serial.println(WiFi.localIP());
  Serial.print("SoftAP IP: ");
  Serial.println(WiFi.softAPIP());
  createWebServer();
  // Start the server
  server.begin();
  Serial.println("Server started");
}

void setupAP(void)
{
  WiFi.mode(WIFI_STA);
  WiFi.disconnect();
  delay(100);
  int n = WiFi.scanNetworks();
  Serial.println("scan done");
  if (n == 0)
    Serial.println("no networks found");
  else
  {
    Serial.print(n);
    Serial.println(" networks found");
    for (int i = 0; i < n; ++i)
    {
      // Print SSID and RSSI for each network found
      Serial.print(i + 1);
      Serial.print(": ");
      Serial.print(WiFi.SSID(i));
      Serial.print(" (");
      Serial.print(WiFi.RSSI(i));
      Serial.print(")");
      Serial.println((WiFi.encryptionType(i) == ENC_TYPE_NONE) ? " " : "*");
      delay(10);
    }
  }
  Serial.println("");
  st = "<ol>";
  for (int i = 0; i < n; ++i)
  {
    // Print SSID and RSSI for each network found
    st += "<li>";
    st += WiFi.SSID(i);
    st += " (";
    st += WiFi.RSSI(i);

    st += ")";
    st += (WiFi.encryptionType(i) == ENC_TYPE_NONE) ? " " : "*";
    st += "</li>";
  }
  st += "</ol>";
  delay(100);
//  WiFi.softAP("how2electronics", "");
  WiFi.softAP("jatayu", "");
  Serial.println("softap");
  launchWeb();
  Serial.println("over");
}

void createWebServer()
{
  {
    server.on("/", []() {

      IPAddress ip = WiFi.softAPIP();
      String ipStr = String(ip[0]) + '.' + String(ip[1]) + '.' + String(ip[2]) + '.' + String(ip[3]);
      content += "<!DOCTYPE HTML>\r\n<HTML>Hello from ESP8266 at ";
      content += "<form action=\"/scan\" method=\"POST\"><input type=\"submit\" value=\"scan\"></form>";
      content += ipStr;
      content += "<p>";
      content += st;
      content += "</p><form method='get' action='setting'><label>SSID: </label><input name='ssid' length=32><input name='password' length=64><input name='patient' placeholder='patient name'><input name='org' placeholder='organization name'><input name='floor' placeholder='floor_name'><input type='submit'></form>";
      server.send(200, "text/html", content);
    });
    server.on("/scan", []() {
      //setupAP();
      IPAddress ip = WiFi.softAPIP();
      String ipStr = String(ip[0]) + '.' + String(ip[1]) + '.' + String(ip[2]) + '.' + String(ip[3]);

      content = "<!DOCTYPE HTML>\r\n<html>go back";
      server.send(200, "text/html", content);
    });

    server.on("/setting", []() {
      String qsid = server.arg("ssid");
      String qpass = server.arg("password");
      String qpatient = server.arg("patient");
      String qfloor = server.arg("floor");
      String qorg = server.arg("org");
      if (qsid.length() > 0 && qpass.length() > 0) {
        Serial.println("clearing eeprom");
        for (int i = 0; i < 96; ++i) {
          EEPROM.write(i, 0);
        }
        Serial.println(qsid);
        Serial.println("");
        Serial.println(qpass);
        Serial.println("");

        // ------------------------- write SSID to EEPROM
        Serial.println("writing eeprom ssid: ");
        for (int i = 0; i < qsid.length(); ++i) {
          EEPROM.write(i, qsid[i]);
          Serial.print("Wrote: ");
          Serial.println(qsid[i]);
        }

        // ------------------------- write PASSWORD to EEPROM
        Serial.println("writing eeprom ssid: ");
        for (int i = 0; i < qpass.length(); ++i) {
          EEPROM.write(32 + i, qpass[i]);
          Serial.print("Wrote: ");
          Serial.println(qpass[i]);
        }

        // ------------------------- write PATIENT to EEPROM
        Serial.println("writing eeprom ssid: ");
        for (int i = 0; i < qpatient.length(); ++i) {
          EEPROM.write(64 + i, qpatient[i]);
          Serial.print("Wrote: ");
          Serial.println(qpass[i]);
        }

        // ------------------------- write FLOOR_NAME to EEPROM
        for (int i = 0; i < qfloor.length(); ++i) {
          EEPROM.write(96 + i, qfloor[i]);
          Serial.print("Wrote: ");
          Serial.println(qfloor[i]);
        }
        // ------------------------- write FLOOR_NAME to EEPROM
        for (int i = 0; i < qorg.length(); ++i) {
          EEPROM.write(128 + i, qorg[i]);
          Serial.print("Wrote: ");
          Serial.println(qorg[i]);
        }
        EEPROM.commit();

        content = "{\"Success\":\"saved to eeprom... reset to boot into new wifi\"}";
        statusCode = 200;
        ESP.reset();
      } else {
        content = "{\"Error\":\"404 not found\"}";
        statusCode = 404;
        Serial.println("Sending 404");
      }
      server.sendHeader("Access-Control-Allow-Origin", "*");
      server.send(statusCode, "application/json", content);

    });
  }
}
