# default thresholds based on paper (do not change unless necessary)
THRESHOLDS = {
    'ph': (6.5, 9.0),
    'salinity': (4.5, 5.5),
    'dissolved_oxygen': (4.8, 5.2),
    'temperature': (25.0, 32.0)
}

class SensorDataMonitor: 
    """
    Example:
        monitor = SensorDataMonitor()
        print(monitor.check_parameter_level('ph', 7.0)) Output: True
    """
    def update_threshold_values(self, **kwargs):
        """
        Update the threshold values for parameters.

        Args:
            **kwargs: Keyword arguments for parameter names and new threshold values.
                      For example: update_threshold_values(ph=(6.0, 8.0), salinity=(4.0, 6.0))
        """
        for key, value in kwargs.items():
            if key in THRESHOLDS:
                THRESHOLDS[key] = value

    def is_value_within_range(self, value, threshold):
        """
        Check if a value is within a specified range.

        Args:
            value: The value to be checked.
            threshold: Tuple representing the range (min, max).

        Returns:
            bool: True if the value is within the range, False otherwise.
        """
        return threshold[0] <= value <= threshold[1]

    def check_parameter_level(self, parameter, value):
        """
        Check if a parameter value is within the acceptable range.

        Args:
            parameter: The parameter to be checked (e.g., 'ph', 'salinity').
            value: The value of the parameter to be checked.

        Returns:
            bool: True if the value is within the acceptable range, False otherwise.

        Raises:
            ValueError: If the provided parameter is not recognized.
        """
        threshold = THRESHOLDS.get(parameter)
        if threshold:
            return self.is_value_within_range(value, threshold)
        else:
            raise ValueError(f"Unknown parameter '{parameter}'")
