from conversion import celcius_to_fahrenheit
from conversion import celsius_to_kelvin
from conversion import check_unit_validity

# Must: start function with "test_" and start filename with "test_" in order to automatically apply pytest

def test_celcius_to_fahrenheit():
    assert celcius_to_fahrenheit(20) == 68
    assert celcius_to_fahrenheit(0) ==32
    # assert celcius_to_fahrenheit(None) is None
    

def test_celcius_to_kelvin():
    assert celsius_to_kelvin(0) == 273.15
    # assert celsius_to_kelvin(None) is None
   
def test_check_unit_validity():
    assert check_unit_validity("C") == True
    assert check_unit_validity("F") == True
    assert check_unit_validity("K") == True
    assert check_unit_validity("X") == False
 
