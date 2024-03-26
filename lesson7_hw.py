# Lesson Seven Homework

script_name = "main"

def get_input():
    while True:
        try:
            temperature_fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
            return temperature_fahrenheit
        except ValueError:
            print("Please enter a valid temperature.")

def fahrenheit_to_celsius(fahrenheit):
    try:
        celsius = (fahrenheit - 32) * 5/9
        return celsius
    except Exception as e:
        print(f"An error occurred during temperature conversion: {e}")

def main():
    temperature_fahrenheit = get_input()
    try:
        converted_temperature = fahrenheit_to_celsius(temperature_fahrenheit)
        print(f"The temperature in Celsius is: {converted_temperature:.2f}°C")
    finally:
        print("Thank you for using the weather forecast application.")

if script_name == "main":
    main()
