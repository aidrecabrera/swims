#ifndef SIM800LV2_H
#define SIM800LV2_H

#include <SoftwareSerial.h>
#include <Arduino.h>

class SIM800L {
public:
    SIM800L(int rxPin, int txPin);
    void begin(long baudRate);
    void setNumber(const String& number);
    void sendMessage(const String& message);
    void receiveMessage();
    void callNumber();
    int getSignalStrength();
    String getSimProvider();
    void update();

private:
    SoftwareSerial sim;
    unsigned long _previousMillis;
    int _step;
    String _buffer;
    String _number;

    String _readSerial();
};

#endif