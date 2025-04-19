def main():
    # Ask the user to enter temperature in Fahrenheit
    degrees_fahrenheit = float(input("Enter temperature in Fahrenheit: "))

    # Convert to Celsius using the formula
    degrees_celsius = (degrees_fahrenheit - 32) * 5.0 / 9.0

    # Print the result
    print("Temperature:", degrees_fahrenheit, "F =", degrees_celsius, "C")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
