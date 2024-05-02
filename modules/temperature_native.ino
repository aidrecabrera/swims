#define ONE_WIRE_BUS 2

uint8_t oneWireBus = ONE_WIRE_BUS;

uint8_t sensor[8];

void setup() {
  Serial.begin(9600);
}

void loop() {
  reset_search();
  
  if (search_sensors()) {
    get_temperature();
  }
  
  delay(1000);
}

void reset_search() {
  pinMode(oneWireBus, OUTPUT);
  digitalWrite(oneWireBus, LOW);
  delayMicroseconds(480);
  digitalWrite(oneWireBus, HIGH);
  delayMicroseconds(80);
  pinMode(oneWireBus, INPUT);
  delayMicroseconds(400);
}

uint8_t search_sensors() {
  uint8_t sensor_count = 0;
  uint8_t data[8];
  
  reset_search();
  write_byte(0xF0);
  
  // sensor data
  for (int i = 0; i < 8; i++) {
    data[i] = read_byte();
  }
  
  if (crc8(data, 7) == data[7]) {
    sensor_count++;
    for (int i = 0; i < 8; i++) {
      sensor[i] = data[i];
    }
  }
  
  return sensor_count;
}

void get_temperature() {
  reset_search();
  write_byte(0x55);
  
  for (int i = 0; i < 8; i++) {
    write_byte(sensor[i]);
  }
  
  write_byte(0xBE);
  
  // temperature conversion
  delay(750);
  
  reset_search();
  write_byte(0xCC);
  write_byte(0xBE);
  
  // temperature data
  uint8_t temp_lsb = read_byte();
  uint8_t temp_msb = read_byte();
  
  int16_t temperature = (temp_msb << 8) | temp_lsb;
  
  // raw temperature to celsius
  float celsius = (float)temperature / 16.0;
  
  Serial.print("Temperature: ");
  Serial.print(celsius);
  Serial.println(" C");
}

void write_byte(uint8_t byte) {
  for (uint8_t i = 0; i < 8; i++) {
    pinMode(oneWireBus, OUTPUT);
    digitalWrite(oneWireBus, (byte >> i) & 0x01);
    delayMicroseconds(80);
    pinMode(oneWireBus, INPUT);
    delayMicroseconds(10);
  }
}

uint8_t read_byte() {
  uint8_t byte = 0;
  
  for (uint8_t i = 0; i < 8; i++) {
    pinMode(oneWireBus, OUTPUT);
    digitalWrite(oneWireBus, LOW);
    delayMicroseconds(3);
    pinMode(oneWireBus, INPUT);
    delayMicroseconds(10);
    byte |= (digitalRead(oneWireBus) << i);
    delayMicroseconds(60);
  }
  
  return byte;
}

uint8_t crc8(uint8_t *addr, uint8_t len) {
  uint8_t crc = 0;
  
  for (uint8_t i = 0; i < len; i++) {
    uint8_t inbyte = addr[i];
    for (uint8_t j = 0; j < 8; j++) {
      uint8_t mix = (crc ^ inbyte) & 0x01;
      crc >>= 1;
      if (mix) crc ^= 0x8C;
      inbyte >>= 1;
    }
  }
  
  return crc;
}