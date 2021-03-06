def is_prime(num):
    """Return True if num is prime."""
    if isinstance(num, int):      #Check if the arg num is an integer.
        if num <= 1:              #prime numbers are considered >1.
            return False

        for element in range(2,num):  #Return True if *number* is prime.
            if num % element == 0:
                return False

    else :                         #Return False if the arg is not an integer.
        return false


    return True

def print_prime(num):             #A function to print the results from is_prime function.
    """Print the closest prime number smaller than num."""
    index = num

    while True:
        index -= 1                #print the prime numbers on a descending order.
        if is_prime(index):
            print(index)
        elif index < 2:
            break

print_prime(5)
