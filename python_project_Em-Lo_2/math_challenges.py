import random
from random import randint

def factorial(n):
    f = 1
    if n == 0:
        return 1
    else:
        for i in range(1, n + 1):
            f *= i
    return f


def math_challenge_factorial():
    print("yes")
    n = random.randint(0, 11)
    a = int(input(f"Math Challenge: Find the factorial of {n} : "))
    m = factorial(n)
    if a == m:
        return True
    else:
        return False


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def nearest_prime(n):
    if is_prime(n):
        return [n]  
    lower = n - 1
    upper = n + 1
    primes = []
    while len(primes) < 2:  
        if is_prime(lower):
            primes.append(lower)
        if is_prime(upper):
            primes.append(upper)
        lower -= 1
        upper += 1
    return primes

def math_challenge_prime():
    n = random.randint(10, 20)
    a = int(input(f"Find the prime number closest to {n}: "))
    b = nearest_prime(n)
    if a in b:
        print("Correct!")
        return True
    else:
        print(f"Incorrect. The closest prime numbers are {', '.join(map(str, b))}.")
        return False


def math_roulette_challenge():
    m = []
    for i in range(5):
        m.append(random.randint(1, 20))
    opp = random.choice(['+', '-', '*'])

    if opp == '+':
        res = 0
        for i in m:
            res = res + i
        expr = f"{m[0]}"
        for i in m[1:]:
            expr += f" + {i}"
        print(f"Solve the following operation: {expr}")
    
    elif opp == '-':
        res = m[0]
        expr = f"{m[0]}"
        for i in m[1:]:
            res = res - i
            expr += f" - {i}"
        print(f"Solve the following operation: {expr}")

    elif opp == '*':
        res = m[0]
        expr = f"{m[0]}"
        for i in m[1:]:
            res *= i
            expr += f" * {i}"
        print(f"Solve the following operation: {expr}")
    
    user_answer = input("Your answer: ").strip()
    
    if int(user_answer) == res:
        print("Correct! Well done.")
        return True
    else:
        print(f"Incorrect. The correct answer was {res}.")
        return False
    



def math_challenge():
    result = random.randint(1, 3)
    sucess = False
    if result == 1:
        print("The master has chosen the factorial challenge")
        sucess = math_challenge_factorial()
    if result == 2:
        print("The master has chosen the prime challenge")
        sucess = math_challenge_prime()
    if result == 3:
        print("The master has chosen the roulette challenge")
        sucess = math_roulette_challenge()
    return sucess






