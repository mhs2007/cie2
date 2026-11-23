
import sys

if __name__ == "__main__":
    
celsius = int(sys.argv[1])

farhrenheit = ((celsius*9/5) + 32)

print("Converted Celsius to farhrenheit: ",farhrenheit)