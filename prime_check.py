# this function checks if a number is prime
def prime_checker(num):
    flag = True
    for divisor in range(2, num / 2):
        if num % divisor ==0:
            flag = False
            return flag
    return flag

number_to_check = int(raw_input("Enter number to check "))
print prime_checker(number_to_check)
