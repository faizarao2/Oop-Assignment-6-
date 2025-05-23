# 12. Static Methods
# Assignment:
# Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the
#  Fahrenheit value.


class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        fehrenheit = (c * 9/5) + 32
        return fehrenheit

print("Temperature in Fahrenheit : ", TemperatureConverter.celsius_to_fahrenheit(25))  # Output: 77.0