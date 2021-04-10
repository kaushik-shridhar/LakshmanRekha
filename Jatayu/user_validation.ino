// ------------------------- authenticate user
void sendUserData(String uid, String patient_name, String floor_name, String wifi_ssid, String org) {
  user_data = "uid="+uid+"&patient_name="+patient_name+"&floor_name="+floor_name+"&wifi_ssid="+wifi_ssid+"&org="+org;
  http.begin("http://192.168.29.132:8000/tracking/validate/");
//  http.begin("http://192.168.1.5:8000/tracking/validate/");
//  http.begin("http://192.168.0.107:8000/tracking/validate/");
  http.addHeader("Content-Type", "application/x-www-form-urlencoded");

  http_code = http.POST(user_data);
  Serial.println(user_data);

  if (http_code == 200) {
    Serial.println("User values uploaded successfully");
  } else {
    Serial.println("User values failed to upload. \n");
  }
  
}

// ------------------------- read user data
void validateUser() {
  sendUserData(uid, patient_name, floor_name, wifi_ssid, org);
}
