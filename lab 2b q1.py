def calculate_s1(n):
    # Calculate S1: 1 + 2 + 3 + ... + n
    s1 = sum(range(1, n + 1))
    return s1

def calculate_s2(n):
    # Calculate S2: n!
    s2 = 1
    for i in range(1, n + 1):
        s2 *= i
    return s2

def calculate_s3(n):
    # Calculate S3: 1^2 + 2^2 + 3^2 + ... + n^2
    s3 = sum(i ** 2 for i in range(1, n + 1))
    return s3

def is_prime(num):
    # Check if a number is prime
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Input an integer number n > 5
while True:
    try:
        n = int(input("Enter an integer number greater than 5 (n): "))
        if n <= 5:
            print("Please re-enter. n must be greater than 5.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Calculate and display S1, S2, and S3
s1_result = calculate_s1(n)
s2_result = calculate_s2(n)
s3_result = calculate_s3(n)

print(f"S1 = {s1_result}")
print(f"S2 = {s2_result}")
print(f"S3 = {s3_result}")

# Re-input n and check if it is a prime number
while True:
    try:
        n_prime = int(input("Re-enter n to check if it's a prime number: "))
        if n_prime <= 1:
            print("Please re-enter. n must be greater than 1.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if is_prime(n_prime):
    print(f"{n_prime} is a prime number.")
else:
    print(f"{n_prime} is not a prime number.")
