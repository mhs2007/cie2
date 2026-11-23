from cie2 import farhrenheit

def test_farhrenheit1():
    assert farhrenheit(26) == "Converted Celsius to farhrenheit:= 78."

def test_farhrenheit2():
    assert farhrenheit(32) == "Converted Celsius to farhrenheit: 89.6"

def test_farhrenheit3():
    assert farhrenheit(46) == "Converted Celsius to farhrenheit: 114.8"