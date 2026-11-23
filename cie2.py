import sys

def farhrenheit(celsius):
    return (celsius * 9/5) + 32

if __name__ == "__main__":
    celsius = int(sys.argv[1])
    print("Fahrenheit:", farhrenheit(celsius))