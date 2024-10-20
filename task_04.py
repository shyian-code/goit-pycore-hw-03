from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    end_date = today + timedelta(days=7)
    upcoming_birthdays = []

    for user in users:
        # Перетворення дня народження на об'єкт datetime.date
        birthday = datetime.strptime(user['birthday'], '%Y.%m.%d').date()
        # Оновлення дня народження на поточний рік
        birthday_this_year = birthday.replace(year=today.year)
        
        # Якщо день народження вже минув цього року, дивимось на наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        
        # Перевірка, чи день народження знаходиться в межах наступних 7 днів
        if today <= birthday_this_year <= end_date:
            # Перевірка на вихідні
            if birthday_this_year.weekday() in (5, 6):  # 5 - субота, 6 - неділя
                # Якщо це субота або неділя, переносимо на понеділок
                birthday_this_year += timedelta(days=(7 - birthday_this_year.weekday()))

            # Додаємо користувача і дату привітання до результату
            upcoming_birthdays.append({
                'name': user['name'],
                'congratulation_date': birthday_this_year.strftime('%Y.%m.%d')
            })

    return upcoming_birthdays

# Приклад використання
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Max Payne", "birthday": "1987.10.21"},
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
