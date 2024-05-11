from datetime import datetime, timedelta
import calendar

def next_wednesday():
    today = datetime.today()
    # Calculate the number of days until the next Wednesday (0=Monday, 1=Tuesday, ..., 6=Sunday)
    days_until_wednesday = (2 - today.weekday() + 7) % 7
    # Add the number of days until Wednesday to the current date
    next_wednesday_date = today + timedelta(days=days_until_wednesday)
    
    # Get month name from month number
    month_name = calendar.month_name[next_wednesday_date.month]
    
    return f" {next_wednesday_date.day} {month_name} {next_wednesday_date.year}"

# Example usage
print("Next Wednesday:", next_wednesday())