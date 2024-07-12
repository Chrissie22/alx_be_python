from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()  # Function datetime.now() is assigned to this variable in other to get the current live date and time
    datetime_format = current_date.strftime("%Y-%m-%d %H:%M:%S") # this formats the current date and time into a readable string, output will be 2024-07-10 15:30:45
    print(f"Current date and time: {datetime_format}")
    return current_date

def calculate_future_date(current_date, days_to_add):
    future_date = current_date + timedelta(days=days_to_add) #calculate the future date  and time by adding a specific number of days to the current date
    format_futureDate = future_date.strftime("%Y-%m-%d") # format future date into a readable format
    print(f"future date: {format_futureDate}")
    return future_date

def main():
    current_date = display_current_datetime() #display cuurent date and time
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(current_date, days_to_add)
    except ValueError:
        print("Please enter a valid integer for the number of days.")
        
if __name__=="__main__":
    main()