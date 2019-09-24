#Rajeev Giri
#COMS 103
#Lab 04

##For centimers and inches.
#For converting inches to centimeters.
def inches_to_centimeters(inches): # signature of the function
    """ Convert inches to centimeters

    The function prompts the user for a number of inches and prints out
    the equivalent number of centimeters. 

    2.54 centimers = 1 inches"""
    centimeters = inches * 2.54
    return centimeters
    
#For converting centimers to inches.
def centimeters_to_inches(centimeters):
    """ Convert centimeters to inches

    The function prompts the user for a number of centimeters and prints out
    the equivalent number of inches."""
    inches = centimeters / 2.54
    return inches


##For liters and gallons.
#For converting liters to gallons.
def liters_to_gallons(liters): 
    """Convert liters to gallons

    The function prompts the user for a number of liters and prints out
    the equivalent number of gallons.

    1 liter = 0.264172 gallons"""
    gallons = liters * 0.264172
    return gallons
    
#For converting gallons to liters.
def gallons_to_liters(gallons):
    """Convert gallons to liters.

    The function prompts the user for a number of gallons and prints out
    the equivalent number of liters."""
    liters = gallons / 0.264172
    return liters

  

##For meters and yards.
#For converting meters to yards.
def meters_to_yards(meters): 
    """Convert meters to yards

    The function prompts the user for a number of meters and prints out
    the equivalent number of yards.

    1 meters = 1.09361 yards"""
    yards = meters * 1.09361
    return yards
    
#For converting yards to meters.
def yards_to_meters(yards):
    """Convert yards to meters.

    The function prompts the user for a number of yards and prints out
    the equivalent number of meters."""
    meters = yards / 1.09361
    return meters


##For kilograms ang pound.
#For converting kilograms to pound.
def kilograms_to_pounds(kilograms): 
    """Convert kilograms to pounds

    The function prompts the user for a number of pounds and prints out
    the equivalent number of kilograms.

    1 kilograms = pound 2.20462"""
    pounds = kilograms * 2.20462
    return pounds

#For converting pound to kilograms.
def pounds_to_kilograms(pounds):
    """Convert pounds to kilograms.

    The function prompts the user for a number of kilograms and prints out
    the equivalent number of pounds."""
    kilograms = pounds / 2.20462
    return kilograms


##For Fahrenhite to Celsius.
#For converting fahrenhite celsius.
def fahrenhite_to_celsius(fahrenhite): 
    """Convert fahrenhite to celsius

    The function prompts the user for a number in fahrenhite and prints out
    the equivalent number in celsius.

    32 degree fahrenhite = 0 degree celsius
    Formula is (0°C × 9/5) + 32 = 32°F"""
    celsius = (fahrenhite - 32) * 5/9 
    return celsius
    
    
#For converting celsius fahrenhite.
def celsius_to_fahrenhite(celsius):
    """Convert celsius to fahrenhite.

    The function prompts the user for a number in celsius and prints out
    the equivalent number in fahrenhite."""
    fahrenhite = (celsius * 9/5) + 32
    return fahrenhite

   

def main():
    print("*****Welcome to the converters program!******")
    print()

    while True:
        print("""List of Conversions:
""")#For line spacing.
        print("[inches]in to (centimeters)cm")
        print("[centimeters]cm to (inches)in")
        print("[iters]l to (gallons)gal")
        print("[gallons]gal to (litersl)")
        print("[meters]m to (yards)yd")
        print("[yards]yd to (meters)m")
        print("[kilograms]kg to (pounds)lb")
        print("[pounds]lb to (kilograms)kg")
        print("[fahrenhite]f to (celsius)c")
        print("""[celsius]c to (fahrenhite)f
""")#For line spacing.
        print("*****You can go with short or full name of converters as displayed.*****")
        print()
        starting_unit = input("Enter the type of value you want to convert: ")

        value = float(input("""
How many """ + starting_unit + " to convert? "))#For line spacing.
        

        if starting_unit == "inches" or starting_unit == "in":
            result = inches_to_centimeters(value)
            unit_name = "Centimeters"#For displaying converted unit.
        elif starting_unit == "centimeters" or starting_unit == "cm":
            result = centimeters_to_inches(value)
            unit_name = "Inches"
        elif starting_unit == "gallons" or starting_unit == "gal":
            result = gallons_to_liters(value)
            unit_name = "Liters"
        elif starting_unit == "liters" or starting_unit == "l":
            result = liters_to_gallons(value)
            unit_name = "Gallons"
        elif starting_unit == "meters" or starting_unit == "m":
            result = meters_to_yards(value)
            unit_name = "Yards"
        elif starting_unit == "yards" or starting_unit == "yd":
            result = yards_to_meters(value)
            unit_name = "Meters"
        elif starting_unit == "kilograms" or starting_unit == "kg":
            result = kilograms_to_pounds(value)
            unit_name = "Pounds"
        elif starting_unit == "pounds" or starting_unit == "lb":
            result = pounds_to_kilograms(value)
            unit_name = "Kilograms"
        elif starting_unit == "fahrenhite" or starting_unit == "f":
            result = fahrenhite_to_celsius (value)
            unit_name = "Degree Celsius"
        elif starting_unit == "celsius" or starting_unit == "c":
            result = celsius_to_fahrenhite(value)
            unit_name = "Degree Fahrenhite"
        print(result, unit_name)#To display reasult and convertes unit.
        print("""
""")#For line spacing in between next progran.


if __name__ == "__main__":
    main()

