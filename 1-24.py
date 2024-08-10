def generate_fibonacci_up_to(limit):
    fibonacci_numbers = []
    a, b = 0, 1
    while a <= limit:
        fibonacci_numbers.append(a)
        a, b = b, a + b
    return fibonacci_numbers

limit = 100


fibonacci_numbers = generate_fibonacci_up_to(limit)
print(fibonacci_numbers)  
