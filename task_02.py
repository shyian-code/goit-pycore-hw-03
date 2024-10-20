import random

def get_numbers_ticket(min_val, max_val, quantity):
    # Parameter validation check
    if min_val < 1 or max_val > 1000 or quantity > (max_val - min_val + 1):
        return []
    
    # Generating unique random numbers
    result = random.sample(range(min_val, max_val + 1), quantity)
    
    # Sorting the result
    return sorted(result)

# Example of usage
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
