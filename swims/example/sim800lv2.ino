#include <SoftwareSerial.h>
#include "SIM800L.h"

SIM800L sim(10, 11); // RX, TX pins

void setup() {
    Serial.begin(9600);
    Serial.println("System Started...");
    sim.begin(9600);
    sim.setNumber("+6281222329xxx");
    Serial.println("Type s to send an SMS, r to receive an SMS, c to make a call, q to check signal strength, and p to get SIM provider");
}

void loop() {
    if (Serial.available() > 0) {
        char command = Serial.read();
        switch (command) {
            case 's':
                sim.sendMessage("Hello, how are you? Greetings from miliohm.com admin");
                break;
            case 'r':
                sim.receiveMessage();
                Serial.println("Unread Message done");
                break;
            case 'c':
                sim.callNumber();
                break;
            case 'q':
                sim.getSignalStrength();
                break;
            case 'p':
                sim.getSimProvider();
                break;
        }
    }

    sim.update();

    if (sim.available() > 0) {
        Serial.write(sim.read());
    }
}