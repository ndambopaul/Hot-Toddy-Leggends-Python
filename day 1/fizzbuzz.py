def check_if_number_is_prime(n):
    """
    This function checks if a number is prime.
    
    args:
        - n: The number to check

    returns:
        - True if the number is prime, False otherwise
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def prime_and_fizz_buzz():
    """
    Prints out numbers from 1 to 100 with the following rules:
    - If the number is prime, print "Prime"
    - If the number is divisible by 3, print "Fizz"
    - If the number is divisible by 5, print "Buzz"
    - If the number is divisible by both 3 and 5, print "FizzBuzz"

    The function prints out the numbers with the appropriate label
    """
    
    ## Getting numbers from 1 to 100
    for number in range(1, 101):
        output = f"{number}: "  # Labelling for clarity

        # Checking if the number is prime
        if check_if_number_is_prime(number):
            output += "Prime "

        # Check for Fizz, Buzz, and FizzBuzz
        if number % 3 == 0 and number % 5 == 0:
            output += "FizzBuzz"
        elif number % 3 == 0:
            output += "Fizz"
        elif number % 5 == 0:
            output += "Buzz"

        print(output.strip())

# Running the function
prime_and_fizz_buzz()
