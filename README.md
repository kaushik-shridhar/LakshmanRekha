# LakshmanRekha
<p align="center">Geofencing using IOT(GOT)</p>

<iframe width="100%" height="100%" src="https://drive.google.com/file/d/1mhQ6JXNDs80DfBCLhZ6ST3ZBmKoXHtMJ/preview"></iframe>

<p align="center">Since the outbreak of covid-19, the situation of India has worsened to an extent where we have around 80,000+ active cases coming up daily, and hence we cannot affort to put at stake the lives of our essential workers. Reports of various attempts of patients sneaking out of the hospitals have raised the concern of increasing the potential spread of virus.</p>

**LakshmanRekha** is a web based application which works along with a watch **Jatayu** consisting of an esp12 chip which helps in monitoring of covid affected patients by tracking their movements and making sure they do not leave the established geofence, also alerting the authorities in case of a breach in the geofence.

## ✨ Main Features
🌐 Geofencing
📍 Indoor Positioning
🚨 Alerting

## 🔧 Installation

Clone the repo and run -
- For windows:
```
pip install -r requirements.txt
```

#### ⚙️ Hardware
Change the ip in `Jatayu/user_validation` on line 4 and `Jatayu/wifi_functions` on line 36 and line 58. Then connect NodeMCU to your pc and upload the code in the folder.<br>
Then your NodeMCU will go into access point mode if it fails to connect to a wifi. When it does, open your browser and type `http://192.168.4.1/` and hit enter.<br>
Then enter the `WiFi` and `Patient/User` credentials and hit submit. This will save the data to the eeprom of the NodeMCU.

#### 💻 Software

Download and install xampp. Start the xampp control panel and start Apache and MySQL. Then open your browser and type`http://localhost/phpmyadmin/`.<br>
Then select `new` and create a new database named `lakshmanrekha`.

Once done, run the following commands to run the website -
```
cd LakshmanRekha/
python manage.py runserver
```

## 📈 How It Works

