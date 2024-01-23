def is_palindrome(num):
    # Convert the number to a string and check if it reads the same backward
    return str(num) == str(num)[::-1]

def display_palindromes_in_interval(m, n):
    palindromes = [num for num in range(m, n+1) if is_palindrome(num)]
    return palindromes

def main():
    # Input two integers, ensuring m < n
    while True:
        try:
            m = int(input("Enter the lower bound (m): "))
            n = int(input("Enter the upper bound (n): "))
            if m < n:
                break
            else:
                print("Error: m should be less than n. Please try again.")
        except ValueError:
            print("Invalid input. Please enter valid integers.")

    # Display palindrome numbers in the interval [m, n]
    palindromes = display_palindromes_in_interval(m, n)
    
    if palindromes:
        print(f"Palindromes in the interval [{m}, {n}]: {palindromes}")
    else:
        print(f"No palindromes found in the interval [{m}, {n}].")

if __name__ == "__main__":
    main()
