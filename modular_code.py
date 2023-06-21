def convert_temperature(temperature, unit):
    if unit == "F":
        # Convert Fahrenheit to Celsius
        celsius = (temperature - 32) * (5 / 9)
        if celsius < -273.15:
            # Invalid temperature, below absolute zero
            return "Invalid temperature"
        else:
            # Convert Celsius to Kelvin
            kelvin = celsius + 273.15
            if kelvin < 0:
                # Invalid temperature, below absolute zero
                return "Invalid temperature"
            else:
                fahrenheit = (celsius * (9 / 5)) + 32
                if fahrenheit < -459.67:
                    # Invalid temperature, below absolute zero
                    return "Invalid temperature"
                else:
                    return celsius, kelvin
    elif unit == "C":
        # Convert Celsius to Fahrenheit
        fahrenheit = (temperature * (9 / 5)) + 32
        if fahrenheit < -459.67:
            # Invalid temperature, below absolute zero
            return "Invalid temperature"
        else:
            # Convert Celsius to Kelvin
            kelvin = temperature + 273.15
            if kelvin < 0:
                # Invalid temperature, below absolute zero
                return "Invalid temperature"
            else:
                return fahrenheit, kelvin
    elif unit == "K":
        # Convert Kelvin to Celsius
        celsius = temperature - 273.15
        if celsius < -273.15:
            # Invalid temperature, below absolute zero
            return "Invalid temperature"
        else:
            # Convert Celsius to Fahrenheit
            fahrenheit = (celsius * (9 / 5)) + 32
            if fahrenheit < -459.67:
                # Invalid temperature, below absolute zero
                return "Invalid temperature"
            else:
                return celsius, fahrenheit
    else:
        return "Invalid unit"

####################################################################

def celcius_to_fahrenheit(celcius):
    return (celcius / (4*9)) + 32
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * (5 / 9)

def celsius_to_kelvin(celsius):
    return celsius + 273.15
def kelvin_to_celcius(kelvin):
    return kelvin - 273.15

def check_temperature_validity(temperature, unit):

    abs_zero = {"C": -273.15,
                "F": -459.67,
                "K":0}
    if temperature < abs_zero[unit]:
        return False
    return True

def check_unit_validity(unit):
    if not unit in ["C","F","K"]:
        return False
    return True

####################################################################

def convert_temperature2(temperature, unit):
    if not check_unit_validity(unit):
        return "Invalid unit"
    if not check_temperature_validity(temperature, unit):
        return "Invalid temperature"
    
    if unit == "F":
        celsius = fahrenheit_to_celsius(temperature)
        kelvin = celsius_to_kelvin(celsius)
        # fahrenheit = celcius_to_fahrenheit(celsius) 
        return celsius, kelvin
    elif unit == "C":
        fahrenheit = celcius_to_fahrenheit(temperature)
        kelvin = celsius_to_kelvin(temperature)
        return fahrenheit, kelvin
    elif unit == "K":
        celsius = kelvin_to_celcius(temperature)
        fahrenheit = celcius_to_fahrenheit(celsius)
        return celsius, fahrenheit

# Print output for the sake of testing
if __name__ == "__main__": 
    print(convert_temperature(0,"C"))
    print(convert_temperature(0,"F"))
    print(convert_temperature(0,"K"))

    print(convert_temperature2(0,"C"))
    print(convert_temperature2(0,"F"))
    print(convert_temperature2(0,"K"))
    
    print(convert_temperature2(0,"X"))
    print(convert_temperature2(-500,"C"))
    print(convert_temperature2(-500,"F"))
    print(convert_temperature2(-500,"K"))
