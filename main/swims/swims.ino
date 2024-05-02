#include <Arduino.h>
#include "sensor_data.pb.h"
#include "pb.h"
#include "pb_encode.h"
#include "pb_decode.h"

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
  ADC_RESOLUTION
);

void setup() {
  Serial.begin(9600);
  ph4502c.init();
  while (!Serial) {
    ; // necessary to wait for serial port connection
  }
}

void loop() {
  // sensor data
  SensorData sensorData = SensorData_init_zero;
  sensorData.temperature = ph4502c.read_temp();
  sensorData.pH = ph4502c.read_ph_level();
  sensorData.dOxygen = 0;
  sensorData.salinity = 0;

  // buffer alloc to store the encoded data
  uint8_t buffer[SensorData_size];
  size_t buffer_len = SensorData_size;

  // encode into the buffer
  pb_ostream_t stream = pb_ostream_from_buffer(buffer, buffer_len);
  bool status = pb_encode(&stream, SensorData_fields, &sensorData);

  if (status) {
    // send over the serial port
    Serial.write(buffer, stream.bytes_written);
  } else {
    Serial.println("Encoding failed");
  }

  delay(1000);
}
