from datetime import datetime

def days_until_date(month_name, day):
    # Convert the month name to a month number
    try: # The try and except statements in Python are part of error handling, try and except are not functions; they are control flow statements
        month = datetime.strptime(month_name, "%B").month
    except ValueError:
        return "Invalid month name. Please use the full month name, like 'January'."
    
    # Get the current date
    current_date = datetime.now()
    
    # Determine the target date, using the current year
    target_date = datetime(current_date.year, month, day)
    
    # If the target date is already past in this year, set it to next year
    if target_date < current_date:
        target_date = datetime(current_date.year + 1, month, day)
    
    # Calculate the difference in days
    days_difference = (target_date - current_date).days
    
    return f"Days until {target_date.strftime('%B %d')}: {days_difference} days."

# Get user input
user_input = input("Enter Your birthday (e.g., 'January 25'): ")

# Split the input into month and day
try:
    month_name, day = user_input.split()
    day = int(day)  # Convert day to an integer
except ValueError:
    print("Invalid input. Please enter in the format 'Month Day'.")
else:
    # Call the function and print the result
    result = days_until_date(month_name, day)
    print(result)
