#include "sim800lv2.h"

SIM800L::SIM800L(int rxPin, int txPin) : sim(rxPin, txPin), _previousMillis(0), _step(0) {
    _buffer.reserve(50);
}

void SIM800L::begin(long baudRate) {
    sim.begin(baudRate);
}

void SIM800L::setNumber(const String& number) {
    _number = number;
}

void SIM800L::sendMessage(const String& message) {
    _step = 1;
}

void SIM800L::receiveMessage() {
    _step = 6;
}

void SIM800L::callNumber() {
    _step = 8;
}

int SIM800L::getSignalStrength() {
    _step = 10;
    return -1;
}

String SIM800L::getSimProvider() {
    _step = 13;
    return "";
}

void SIM800L::update() {
    unsigned long currentMillis = millis();

    switch (_step) {
        case 1:
            sim.println("AT+CMGF=1");
            _previousMillis = currentMillis;
            _step++;
            break;
        case 2:
            if (currentMillis - _previousMillis >= 200) {
                sim.println("AT+CMGS=\"" + _number + "\"\r");
                _previousMillis = currentMillis;
                _step++;
            }
            break;
        case 3:
            if (currentMillis - _previousMillis >= 200) {
                sim.println(_buffer);
                _previousMillis = currentMillis;
                _step++;
            }
            break;
        case 4:
            if (currentMillis - _previousMillis >= 100) {
                sim.println((char)26);
                _previousMillis = currentMillis;
                _step++;
            }
            break;
        case 5:
            if (currentMillis - _previousMillis >= 200) {
                _readSerial();
                _step = 0;
            }
            break;
        case 6:
            sim.println("AT+CMGF=1");
            _previousMillis = currentMillis;
            _step++;
            break;
        case 7:
            if (currentMillis - _previousMillis >= 200) {
                sim.println("AT+CNMI=1,2,0,0,0");
                _step = 0;
            }
            break;
        case 8:
            sim.print("ATD");
            sim.print(_number);
            sim.print(";\r\n");
            _previousMillis = currentMillis;
            _step++;
            break;
        case 9:
            if (currentMillis - _previousMillis >= 200) {
                _readSerial();
                _step = 0;
            }
            break;
        case 10:
            sim.println("AT+CSQ");
            _previousMillis = currentMillis;
            _step++;
            break;
        case 11:
            if (currentMillis - _previousMillis >= 200) {
                _buffer = _readSerial();
                int csqStart = _buffer.indexOf("+CSQ:");
                if (csqStart != -1) {
                    int signalStrength = _buffer.substring(csqStart + 5).toInt();
                    _step = 0;
                    return signalStrength;
                }
                _step++;
            }
            break;
        case 12:
            if (currentMillis - _previousMillis >= 200) {
                _step = 0;
            }
            break;
        case 13:
            sim.println("AT+CSPN?");
            _previousMillis = currentMillis;
            _step++;
            break;
        case 14:
            if (currentMillis - _previousMillis >= 200) {
                _buffer = _readSerial();
                int cspnStart = _buffer.indexOf("+CSPN:");
                if (cspnStart != -1) {
                    int providerStart = _buffer.indexOf('"', cspnStart);
                    if (providerStart != -1) {
                        int providerEnd = _buffer.indexOf('"', providerStart + 1);
                        if (providerEnd != -1) {
                            _step = 0;
                            return _buffer.substring(providerStart + 1, providerEnd);
                        }
                    }
                }
                _step++;
            }
            break;
        case 15:
            if (currentMillis - _previousMillis >= 200) {
                _step = 0;
            }
            break;
    }
}

String SIM800L::_readSerial() {
    if (sim.available()) {
        return sim.readString();
    }
    return "";
}
