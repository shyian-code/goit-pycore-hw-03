from datetime import datetime

def get_days_from_today(date):
    try:
        # Convert the date String into datetime object
        target_date = datetime.strptime(date, '%Y-%m-%d').date()
        
        # Getting the current date
        current_date = datetime.today().date()
        
        # Math difference beetween current date and target date
        difference_beetwen_dates = target_date - current_date
        
        # Return the number of days 
        return difference_beetwen_dates.days
    
    except ValueError:
        # Error handling if the date format is incorrect
        return "Wrong date format. Recomend to use next format YYYY-MM-DD."

# Call the function for use case example
print(get_days_from_today("2024-12-31"))  
