#include <Arduino.h>
#include <math.h>

float EstimateDissolvedOxygen(float phLevel, float temperature, float salinity) {
    float T = temperature + 273.15;
    float S = salinity;
    float A = 457.88;
    float B = 2.00907;
    float C = 1737.62;

    float DO = (A * exp(B - C / T)) * (1.0 - 0.000025 * S);
    
    return DO;
}