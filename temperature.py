def main():
    temperatures = degrees_fahrenheit()
    print("Temperatures: "+temperatures[0] +"F = "+ temperatures[1]+"C")


def degrees_fahrenheit():
    degrees_fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    degrees_celsius = (degrees_fahrenheit - 32) * 5/9
    return str(degrees_fahrenheit), str(degrees_celsius)

if __name__ == "__main__":
    main()