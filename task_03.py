import re

def normalize_phone(phone_number: str) -> str:
    # Remove all characters except digits and the '+' symbol
    phone_number = re.sub(r'[^\d+]', '', phone_number.strip())

    # Check if the number is international, i.e., starts with '+'
    if phone_number.startswith('+'):
        if not phone_number.startswith('+38'):
            phone_number = '+38' + phone_number[1:]
    elif phone_number.startswith('380'):
        phone_number = '+' + phone_number
    else:
        # If the international code is missing, add '+38' for Ukraine
        phone_number = '+38' + phone_number

    return phone_number

# Приклад використання
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
