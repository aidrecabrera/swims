#ifndef AQUARIUM_MONITORING_SYSTEM_H
#define AQUARIUM_MONITORING_SYSTEM_H

extern constexpr float kPhLevelMin;
extern constexpr float kPhLevelMax;
extern constexpr float kSalinityLevelMin;
extern constexpr float kSalinityLevelMax;
extern constexpr float kDissolvedOxygenLevelMin;
extern constexpr float kDissolvedOxygenLevelMax;
extern constexpr float kTemperatureLevelMin;
extern constexpr float kTemperatureLevelMax;

void UpdateThresholdValues(
    float new_ph_level_min = kPhLevelMin,
    float new_ph_level_max = kPhLevelMax,
    float new_salinity_level_min = kSalinityLevelMin,
    float new_salinity_level_max = kSalinityLevelMax,
    float new_dissolved_oxygen_level_min = kDissolvedOxygenLevelMin,
    float new_dissolved_oxygen_level_max = kDissolvedOxygenLevelMax,
    float new_temperature_level_min = kTemperatureLevelMin,
    float new_temperature_level_max = kTemperatureLevelMax);

bool IsValueWithinRange(float value, float min_threshold, float max_threshold);

bool CheckPhLevel(float ph_level);

bool CheckSalinityLevel(float salinity_level);

bool CheckDissolvedOxygenLevel(float dissolved_oxygen_level);

bool CheckTemperatureLevel(float temperature_level);

#endif
