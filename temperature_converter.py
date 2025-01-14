


def user_input_temperature_type():
    while True:
        temperature_type = input("Pick either Fehrenheit or Celsius to convert (F, C): ").strip().upper()
        if temperature_type in ("F", "C"):
            return temperature_type
        print(f"{temperature_type} is not a valid input. Please enter either 'F' or 'C'.")
# Converstion from celsius to fehrenheit
def convert_to_fehrenheit(c):
    return round((5 / 9) * (c - 32))
# Converstion from fehrenheit to celsius
def convert_to_celsius(f): 
    return round(32 + (f * 9 / 5))

# Main program
def main():
    temperature_type = user_input_temperature_type()
    temperature = int(input(f"Input Temperature in {temperature_type}: "))
    if temperature_type == "F":
        print(convert_to_fehrenheit(temperature))
    elif temperature_type == "C":
        print(round(convert_to_celsius(temperature)))