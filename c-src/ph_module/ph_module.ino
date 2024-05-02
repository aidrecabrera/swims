#include <Arduino.h>
#include "sensor_data.pb.h"

float temperature = 25.5;
float pH = 7.2;
float salinity = 0.8;

uint8_t buffer[128];
size_t message_length;

bool encode_sensor_data(uint8_t* buffer, size_t* length) {
    SensorData sensor_data = SensorData_init_zero;
    sensor_data.temperature = temperature;
    sensor_data.pH = pH;
    sensor_data.salinity = salinity;

    pb_ostream_t stream = pb_ostream_from_buffer(buffer, sizeof(buffer));
    bool status = pb_encode(&stream, SensorData_fields, &sensor_data);
    *length = stream.bytes_written;

    return status;
}

void setup() {
    Serial.begin(9600);
}

void loop() {
    if (encode_sensor_data(buffer, &message_length)) {
        Serial.write(buffer, message_length);
    }

    delay(1000);
}
