from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    end_date = today + timedelta(days=7)
    upcoming_birthdays = []

    for user in users:
        # Convert the birthday to a datetime.date object
        birthday = datetime.strptime(user['birthday'], '%Y.%m.%d').date()
         # Update the birthday to the current year
        birthday_this_year = birthday.replace(year=today.year)
        
        # If the birthday has already passed this year, look at the next year
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        
        # Check if the birthday falls within the next 7 days
        if today <= birthday_this_year <= end_date:
            # Check for weekends
            if birthday_this_year.weekday() in (5, 6):  # 5 - Saturday, 6 - Sunday
                # If it's Saturday or Sunday, move it to Monday
                birthday_this_year += timedelta(days=(7 - birthday_this_year.weekday()))

            # Add the user and congratulation date to the result
            upcoming_birthdays.append({
                'name': user['name'],
                'congratulation_date': birthday_this_year.strftime('%Y.%m.%d')
            })

    return upcoming_birthdays

# Example of usage
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Max Payne", "birthday": "1987.10.21"},
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
