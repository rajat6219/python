def user_input():
    num = int(input("Enter a number to check whether it is a prime number or not: "))
    return num

import math

def prime(num):
    prime_flag = True
    for i in range(2, int(math.sqrt(num))+1):
        if(num%i==0):
            prime_flag = False
            break
    return(prime_flag)

def display(prime_flag, num):
    if(prime_flag==True):
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")

def main():
    num = user_input()
    prime_flag = prime(num)
    display(prime_flag, num)
main()
