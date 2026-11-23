from cie2 import farhrenheit

def test_farhrenheit1():
    assert farhrenheit(26) == 78.8

def test_farhrenheit2():
    assert farhrenheit(32) == 89.6

def test_farhrenheit3():
    assert farhrenheit(46) == 114.8