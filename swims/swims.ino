#include <Arduino.h>
#include "sensor_data.pb.h"
#include "pb.h"
#include "pb_encode.h"
#include "pb_decode.h"

// ec
#include "DFRobot_EC.h"
#include <EEPROM.h>
#include <math.h>

#define EC_PIN A1
float voltage, ecValue, temperature = 25;
DFRobot_EC ec;

#include <ph4502c_sensor.h>

#define PH4502C_TEMPERATURE_PIN A1
#define PH4502C_PH_PIN A0
#define PH4502C_PH_TRIGGER_PIN 14
#define PH4502C_CALIBRATION 19.8f
#define PH4502C_READING_INTERVAL 100
#define PH4502C_READING_COUNT 10
#define ADC_RESOLUTION 1024.0f

PH4502C_Sensor ph4502c(
    PH4502C_PH_PIN,
    PH4502C_TEMPERATURE_PIN,
    PH4502C_CALIBRATION,
    PH4502C_READING_INTERVAL,
    PH4502C_READING_COUNT,
    ADC_RESOLUTION);

float salinity()
{
  static unsigned long timepoint = millis();
    if(millis()-timepoint>1000U)  //time interval: 1s
    {
      timepoint = millis();
      voltage = analogRead(EC_PIN)/1024.0*5000;   // read the voltage
      //temperature = readTemperature();          // read temperature sensor to execute temperature compensation
      ecValue =  ec.readEC(voltage,temperature);  // convert voltage to EC with temperature compensation
      return ecValue;
    }
    ec.calibration(voltage,temperature);
}

float EstimateDissolvedOxygen(float phLevel, float temperature, float salinity) {
    float T = temperature + 273.15;
    float S = salinity;
    float A = 457.88;
    float B = 2.00907;
    float C = 1737.62;

    float DO = (A * exp(B - C / T)) * (1.0 - 0.000025 * S);
    
    return DO;
}

void setup()
{
  Serial.begin(9600);
  ph4502c.init();
  ec.begin();
  while (!Serial)
  {
    ; // necessary to wait for serial port connection
  }
}

void loop()
{
  // sensor data
  SensorData sensorData = SensorData_init_zero;
  sensorData.temperature = ph4502c.read_temp();
  sensorData.pH = ph4502c.read_ph_level();
  sensorData.salinity = salinity();
  sensorData.dOxygen = EstimateDissolvedOxygen(sensorData.pH, sensorData.temperature, sensorData.salinity);

  // buffer alloc to store the encoded data
  uint8_t buffer[SensorData_size];
  size_t buffer_len = SensorData_size;

  // encode into the buffer
  pb_ostream_t stream = pb_ostream_from_buffer(buffer, buffer_len);
  bool status = pb_encode(&stream, SensorData_fields, &sensorData);

  if (status)
  {
    // send over the serial port
    Serial.write(buffer, stream.bytes_written);
  }
  else
  {
    Serial.println("Encoding failed");
  }

  delay(1000);
}
