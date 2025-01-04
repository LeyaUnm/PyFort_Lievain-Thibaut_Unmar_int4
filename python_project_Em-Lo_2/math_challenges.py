# Fort Boyard Simulation : Lola Lievain-Thibaut ; Emeline Unmar
# implementation of math functions

import random

# Function to calculate the factorial of a number
# Parameter: n (int) - the number to calculate the factorial for
# Returns: f (int) - the factorial of n
def factorial(n):
    f = 1
    if n == 0:
        return 1
    else:
        for i in range(1, n + 1):
            f *= i
    return f

# Math challenge to find the factorial of a random number between 0 and 10
# Prompts the user for input and compares it to the correct factorial
# Returns: True if the user provides the correct answer, False otherwise
def math_challenge_factorial():
    n = random.randint(0, 11)  # Generate a random number
    try:
        a = int(input(f"Math Challenge: Find the factorial of {n} : "))
    except ValueError:
        print("Error: Please enter a valid integer")  # Error handling for invalid input
        return False
    m = factorial(n)
    if a == m:
        return True
    else:
        return False

# Function to check if a number is prime
# Parameter: n (int) - the number to check
# Returns: True if n is prime, False otherwise
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Function to find the nearest prime numbers to n (both lower and upper)
# Parameter: n (int) - the number to find the nearest primes to
# Returns: primes (list) - a list of the closest prime numbers to n
def nearest_prime(n):
    if is_prime(n):
        return [n]  # If n is prime, return it as the closest prime
    lower = n - 1
    upper = n + 1
    primes = []
    while len(primes) < 2:  # We are looking for both the lower and upper primes
        if is_prime(lower):
            primes.append(lower)
        if is_prime(upper):
            primes.append(upper)
        lower -= 1
        upper += 1
    return primes

# Math challenge to find the prime number closest to a random number between 10 and 20
# Prompts the user for input and compares it to the nearest prime number(s)
# Returns: True if the user provides the correct answer, False otherwise
def math_challenge_prime():
    n = random.randint(10, 20)  # Generate a random number
    try:
        a = int(input(f"Find the prime number closest to {n}: "))
    except ValueError:
        print("Error: Please enter a valid integer")  # Error handling for invalid input
        return False
    b = nearest_prime(n)
    if a in b:
        print("Correct!")
        return True
    else:
        print(f"Incorrect. The closest prime numbers are {', '.join(map(str, b))}.")
        return False

# Math challenge to solve a random mathematical operation (addition, subtraction, or multiplication)
# Prompts the user for input and compares it to the correct result
# Returns: True if the user provides the correct answer, False otherwise
def math_roulette_challenge():
    m = [random.randint(1, 20) for _ in range(5)]  # Generate 5 random numbers
    opp = random.choice(['+', '-', '*'])  # Randomly choose an operation

    if opp == '+':
        res = sum(m)
        expr = f"{m[0]}"
        for i in m[1:]:
            expr += f" + {i}"
        print(f"Solve the following operation: {expr}")
    
    elif opp == '-':
        res = m[0]
        expr = f"{m[0]}"
        for i in m[1:]:
            res -= i
            expr += f" - {i}"
        print(f"Solve the following operation: {expr}")
    elif opp == '*':
        res = m[0]
        expr = f"{m[0]}"
        for i in m[1:]:
            res *= i
            expr += f" * {i}"
        print(f"Solve the following operation: {expr}")
    
    try:
        user_answer = float(input("Your answer: ").strip())
    except ValueError:
        print("Error: Please enter a valid float")  # Error handling for invalid input
        return False
    
    if user_answer == res:
        print("Correct! Well done.")
        return True
    else:
        print(f"Incorrect. The correct answer was {res}.")
        return False

# Main function to randomly choose one of the math challenges and call the corresponding function
# Returns: True if the user completes the challenge correctly, False otherwise
def math_challenge():
    result = random.randint(1, 3)  # Randomly select one of the challenges
    sucess = False
    if result == 1:
        print("The master has chosen the factorial challenge")
        sucess = math_challenge_factorial()
    elif result == 2:
        print("The master has chosen the prime challenge")
        sucess = math_challenge_prime()
    elif result == :
        print("The master has chosen the roulette challenge")
        sucess = math_roulette_challenge()
    return sucess
