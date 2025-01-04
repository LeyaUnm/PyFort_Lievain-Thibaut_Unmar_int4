import random


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
    a = int(input("Math Challenge: Find the factorial of ", n))
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
    a = is_prime(n)
    while a == False:
        n += 1
        a = is_prime(n)
    return n


def math_challenge_prime():
    n = random.randint(10, 20)
    a = int(input("Find the prime number closest to {} :".format(n)))
    b = nearest_prime(n)
    if a == b:
        return True
    else:
        return False


def solve_linear_equation():
    a, b = random.randint(1, 11), random.randint(1, 11)
    x = -b / a
    return a, b, x


def math_challenge_equation():
    c = solve_linear_equation()
    guess = float(input("Solve this equation : {}x + {}".format(a, b)))
    if guess == x:
        return True
    else:
        return False


def math_roulette_challenge():
    m = []
    for i in range(4):
        m.append(random.randint(1, 20))
    opp = random.choice(['+', '-', '*'])

    if opp == '+':
        res = 0
        for i in m:
            res += i
        return res

    if opp == '-':
        res = m[0]
        for i in range(m[1], m[4]):
            res -= i
        return res

    if opp == '*':
        res = 1
        for i in m:
            res *= i
        return res


def math_challenge():
    challenges = ["math_challenge_factorial", "math_challenge_prime", "math_roulette_challenge", "math_challenge_equation"]
    challenge = random.choices(challenges)
    return challenge




