def fahrenheit_convertion(celsius):
    try:
        fahrenheit = celsius * 1.8 + 32
        return round(fahrenheit, 2)
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")