from conversion import celcius_to_fahrenheit
from conversion import celcius_to_kelvin

# Must: start function with "test_" and start filename with "test_" in order to automatically apply pytest

def test_celcius_to_fahrenheit():
    assert celcius_to_fahrenheit(20) == 68
    assert celcius_to_fahrenheit(0) ==32
    assert celcius_to_fahrenheit(None) is None
    

def test_celcius_to_kelvin():
    assert celcius_to_kelvin(0) == 273.15
    assert celcius_to_kelvin(None) is None
 
