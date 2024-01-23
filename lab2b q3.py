def input_integer():
    while True:
        try:
            n = int(input("Enter an integer number: "))
            return n
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def decimal_to_binary(n):
    return bin(n)[2:]

def sum_of_digits(n):
    return sum(int(digit) for digit in str(abs(n)))

def reverse_number(n):
    sign = -1 if n < 0 else 1
    reversed_n = int(str(abs(n))[::-1]) * sign
    return reversed_n

def main():
    # Task 1
    n = input_integer()

    # Task 2
    binary_n = decimal_to_binary(n)
    print(f"{n} in binary: {binary_n}")

    # Task 3
    print(f"Sum of digits of {n}: {sum_of_digits(n)}")

    # Task 4
    reversed_n = reverse_number(n)
    print(f"Reverse of {n}: {reversed_n}")

if __name__ == "__main__":
    main()
