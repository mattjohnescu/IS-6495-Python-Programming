#Functions


#boolean function converters
def yes_no_boolean_converter(val):
    val = str(val).upper()
    if val == "Y" or val == "YES":
        return True
    
    return False


def boolean_yes_no_converter(val):
    if val:
        return "Yes"
    
    return "No"


def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius and return the value."""
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit and return the value."""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def NullToBooleanConverter(value):
    return value is not None
