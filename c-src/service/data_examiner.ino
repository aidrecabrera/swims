// constants for threshold values (do not touch unless necessary).
constexpr float kPhLevelMin = 6.5f;
constexpr float kPhLevelMax = 9.0f;
constexpr float kSalinityLevelMin = 4.5f;
constexpr float kSalinityLevelMax = 5.5f;
constexpr float kDissolvedOxygenLevelMin = 4.8f;
constexpr float kDissolvedOxygenLevelMax = 5.2f;
constexpr float kTemperatureLevelMin = 25.0f;
constexpr float kTemperatureLevelMax = 32.0f;

/**
 * @brief Updates the threshold values for the parameters.
 *
 * @param new_ph_level_min New minimum threshold value for pH level (optional).
 * @param new_ph_level_max New maximum threshold value for pH level (optional).
 * @param new_salinity_level_min New minimum threshold value for salinity level (optional).
 * @param new_salinity_level_max New maximum threshold value for salinity level (optional).
 * @param new_dissolved_oxygen_level_min New minimum threshold value for dissolved oxygen level (optional).
 * @param new_dissolved_oxygen_level_max New maximum threshold value for dissolved oxygen level (optional).
 * @param new_temperature_level_min New minimum threshold value for temperature level (optional).
 * @param new_temperature_level_max New maximum threshold value for temperature level (optional).
 */
void UpdateThresholdValues(
    float new_ph_level_min = kPhLevelMin,
    float new_ph_level_max = kPhLevelMax,
    float new_salinity_level_min = kSalinityLevelMin,
    float new_salinity_level_max = kSalinityLevelMax,
    float new_dissolved_oxygen_level_min = kDissolvedOxygenLevelMin,
    float new_dissolved_oxygen_level_max = kDissolvedOxygenLevelMax,
    float new_temperature_level_min = kTemperatureLevelMin,
    float new_temperature_level_max = kTemperatureLevelMax);

/**
 * @brief Checks if the value is within the specified range.
 *
 * @param value The value to be checked.
 * @param min_threshold The minimum threshold value.
 * @param max_threshold The maximum threshold value.
 * @return true if the value is within the range, false otherwise.
 */
bool IsValueWithinRange(float value, float min_threshold, float max_threshold);

/**
 * @brief Checks if the pH level is within the acceptable range.
 *
 * @param ph_level The pH level value.
 * @return true if the pH level is within the acceptable range, false otherwise.
 */
bool CheckPhLevel(float ph_level);

/**
 * @brief Checks if the salinity level is within the acceptable range.
 *
 * @param salinity_level The salinity level value.
 * @return true if the salinity level is within the acceptable range, false otherwise.
 */
bool CheckSalinityLevel(float salinity_level);

/**
 * @brief Checks if the dissolved oxygen level is within the acceptable range.
 *
 * @param dissolved_oxygen_level The dissolved oxygen level value.
 * @return true if the dissolved oxygen level is within the acceptable range, false otherwise.
 */
bool CheckDissolvedOxygenLevel(float dissolved_oxygen_level);

/**
 * @brief Checks if the temperature level is within the acceptable range.
 *
 * @param temperature_level The temperature level value.
 * @return true if the temperature level is within the acceptable range, false otherwise.
 */
bool CheckTemperatureLevel(float temperature_level);

// Reusable function to check if a value is within a specified range.
bool IsValueWithinRange(float value, float min_threshold, float max_threshold) {
  return value >= min_threshold && value <= max_threshold;
}

bool CheckPhLevel(float ph_level) {
  return IsValueWithinRange(ph_level, kPhLevelMin, kPhLevelMax);
}

bool CheckSalinityLevel(float salinity_level) {
  return IsValueWithinRange(salinity_level, kSalinityLevelMin, kSalinityLevelMax);
}

bool CheckDissolvedOxygenLevel(float dissolved_oxygen_level) {
  return IsValueWithinRange(dissolved_oxygen_level, kDissolvedOxygenLevelMin,
                            kDissolvedOxygenLevelMax);
}

bool CheckTemperatureLevel(float temperature_level) {
  return IsValueWithinRange(temperature_level, kTemperatureLevelMin,
                            kTemperatureLevelMax);
}