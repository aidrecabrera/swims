#include <Arduino.h>
#include <EEPROM.h>
#include <SoftwareSerial.h>
#include <math.h>
#include <ph4502c_sensor.h>
#include <OneWire.h>
#include <DallasTemperature.h>

#include "DFRobot_EC.h"
#include "sim800lv2.h"
#include "pb.h"
#include "pb_decode.h"
#include "pb_encode.h"
#include "sensor_data.pb.h"

// pin definitions
#define EC_PIN A1
#define PH4502C_TEMPERATURE_PIN A1
#define PH4502C_PH_PIN A0
#define PH4502C_PH_TRIGGER_PIN 14
#define DS18B20_PIN 2

// constants
#define PH4502C_CALIBRATION 19.8f
#define PH4502C_READING_INTERVAL 100
#define PH4502C_READING_COUNT 10
#define ADC_RESOLUTION 1024.0f

// globals
float voltage, ecValue, temperature = 0;
String userNumber = "+639604377530";

DFRobot_EC ec;
PH4502C_Sensor ph4502c(PH4502C_PH_PIN, PH4502C_TEMPERATURE_PIN, PH4502C_CALIBRATION,
                       PH4502C_READING_INTERVAL, PH4502C_READING_COUNT, ADC_RESOLUTION);
SIM800L sim(10, 11);
// Setup a oneWire instance to communicate with any OneWire devices (not just Maxim/Dallas temperature ICs)
OneWire oneWire(DS18B20_PIN);
// Pass our oneWire reference to Dallas Temperature. 
DallasTemperature sensors(&oneWire);

// sms module
void sms(int action, String alertMessage = "")
{
  if (Serial.available() > 0)
  {
    char command = Serial.read();
    switch (command)
    {
    case 0:
      sim.sendMessage(alertMessage);
      break;
    case 1:
      sim.receiveMessage();
      break;
    case 2:
      sim.callNumber();
      break;
    case 3:
      sim.getSignalStrength();
      break;
    case 4:
      sim.getSimProvider();
      break;
    }
  }
//  sim.update();
//  if (sim.available() > 0)
//  {
//    Serial.write(sim.read());
//  }
}

// serial communication
void serialComms(bool status, uint8_t buffer[20], pb_ostream_t &stream);
void serialComms(bool status, uint8_t buffer[20], pb_ostream_t &stream)
{
  if (status)
  {
    Serial.write(buffer, stream.bytes_written);
  }
  else
  {
    Serial.println("Encoding failed");
  }
}

// salinity measurement
float readSalinity(float tempVal)
{
  static unsigned long timepoint = millis();
  if (millis() - timepoint > 1000U)
  { // time interval: 1s
    timepoint = millis();
    voltage = analogRead(EC_PIN) / 1024.0 * 5000; // read the voltage
    ecValue = ec.readEC(voltage, tempVal);    // convert voltage to EC with temperature compensation
    return ecValue;
  }
  ec.calibration(voltage, tempVal);
  return ecValue;
}

// dissolved oxygen measurement
float estimateDissolvedOxygen(float phLevel, float temperature, float salinity)
{
  float T = temperature + 273.15;  // celsius to kelvin
  float S = salinity;               // salinity in parts per thousand (ppt)
  float A = 457.88;                // constant a
  float B = 2.00907;               // constant b
  float C = 1737.62;               // constant c
  float DO = (A * exp(B - C / T)) * (1.0 - 0.000025 * S); 

  // pH correction factor
  float pHCorrection = 1.0;
  if (phLevel < 7.0) {
    pHCorrection = 1.0 - 0.032 * (7.0 - phLevel);
  } else if (phLevel > 7.0) {
    pHCorrection = 1.0 - 0.032 * (phLevel - 7.0);
  }
  DO *= pHCorrection;

  return DO;
}

void setup()
{
  Serial.begin(9600);  // for sensors
  // Serial.begin(14400); // for sms module
  // sim800l v2
  // sim.begin(14400);
  // sim.setNumber(userNumber);
  // sensor initializations
  ph4502c.init();
  ec.begin();
  sensors.begin();
  while (!Serial)
  {
    ; // necessary to wait for serial port connection
  }
}

void loop()
{
  sensors.requestTemperatures();
  SensorData sensorData = SensorData_init_zero;
  sensorData.temperature = sensors.getTempCByIndex(0);                                                             // Temperature Measurement
  sensorData.pH = ph4502c.read_ph_level();                                                                  // pH Measurement
  sensorData.salinity = readSalinity(sensors.getTempCByIndex(0));                                                                     // Salinity Measurement
  sensorData.dOxygen = estimateDissolvedOxygen(sensorData.pH, sensorData.temperature, sensorData.salinity); // Dissolved Oxygen Measurement

  // protobuf encoding
  uint8_t buffer[SensorData_size];
  size_t buffer_len = SensorData_size;
  pb_ostream_t stream = pb_ostream_from_buffer(buffer, buffer_len);
  bool status = pb_encode(&stream, SensorData_fields, &sensorData);

  // serial communication
  serialComms(status, buffer, stream);
  delay(1000);
}
