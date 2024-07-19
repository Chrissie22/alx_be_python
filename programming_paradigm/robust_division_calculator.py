def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
    except ValueError:
        print("Error: Please enter numeric values only.")
    else:
        try:
            difference = numerator / denominator
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")
        else:
            return "The result of the division is {}".format(difference)