#
# conversions.py – module with functions to convert between units
#
# fahr2cel : Convert from Fahrenheit to Celsius.
# fahr2kel : Convert from Fahrenheit to Kelvin.
# cel2fahr : Convert from Celsius to Fahrenheit.
# cel2kel : Convert from Celsius to Kelvin.
# kel2cel : Convert from Kelvin to Celsius.
# kel2fahr : Convert from Kelvin to Fahrenheit.
#

def fahr2cel(fahr):
    """Convert from Fahrenheit to Celsius.
    Argument:
    fahr - the temperature in Fahrenheit
    """
    celsius = (fahr - 32) * (5/9)
    return celsius

def cel2fahr(cel):
    """Convert from Celsius to Fahrenheit.
    Argument:
    cel - the temperature in Celsius
    """
    fahrenheit = cel * (9/5) + 32
    return fahrenheit

def cel2kel(cel):
    """Convert from Celsius to Kelvin.
    Argument:
    cel - the temperature in Celsius
    """
    kelvin = cel + 273.15
    return kelvin

def kel2cel(kel):
    """Convert from Kelvin to Celsius.
    Argument:
    kel - the temperature in Kelvin
    """
    celsius = kel - 273.15
    return celsius

def fahr2kel(fahr):
    """Convert from Fahrenheit to Kelvin.
    Argument:
    fahr - the temperature in Fahrenheit
    """
    kelvin = (fahr + 459.67) * (5/9)
    return kelvin

def kel2fahr(kel):
    """Convert from Kelvin to Celsius.
    Argument:
    kel - the temperature in Kelvin
    """
    fahrenheit = kel * (9/5) - 459.67
    return fahrenheit
