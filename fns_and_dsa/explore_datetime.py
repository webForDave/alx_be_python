from datetime import datetime, timedelta

date_format = "%Y-%m-%d %H:%M:%S"

def display_current_datetime():
    current_date = datetime.now()
    return current_date.strftime(date_format)

print(f"Current date and time: {display_current_datetime()}")

number_of_days = int(input("Enter the number of days to add to the current date: "))

if number_of_days:
    def calculate_future_date():
        original_datetime = datetime.strptime(display_current_datetime(), date_format)
        time_delta = timedelta(days=number_of_days)
        new_datetime = original_datetime + time_delta
        future_date = new_datetime.strftime(date_format)
        return future_date
    
print(f"Future date: {calculate_future_date()}")
