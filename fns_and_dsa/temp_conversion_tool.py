FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    celcius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celcius

def convert_to_fahrenheit(celsius):
    farenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return farenheit

def main():
    temperature = input("Enter the temperature to convert: ")
    temperature_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
    if temperature.isnumeric():
        temperature = float(temperature)
        if temperature_type in "Ff":
            result = convert_to_celsius(temperature)
        elif temperature_type in "Cc":
            result = convert_to_fahrenheit(temperature)
        print("{}°F is {}°C".format(temperature, result))
    else:
        raise ValueError("invalid temperature. Pleease enter a numeric value")

if __name__ == "__main__":
    main()