def celcius_to_fahrenheit(celcius):
    """ Celcius converted to Fahrenheit
 
    Args: 
        celcius (float)
         
    Returns:
        float (temperature in degrees Fahrenheit) 
    """
    fah = celcius / 4*9 + 32
    return fah

def celsius_to_kelvin(celsius):
    """ Celcius converted to Kelvin
 
    Args: 
        celcius (float)
         
    Returns:
        float (temperature in degrees Kelvin) 
    """
    return celsius + 273.15