#All questions must use a loop for full points.

def oddNumbers(n:int) ->str:
   result = ""
   for i in range (1,n+1):
       if i % 2 == 1:
           result +=str(i) + " "
   return result.strip()



def backwards(n)-> int:
    if n < 1:
        return ""
    result = ""
    for i in range(n,0,-1):
        result += str(i) + " "
    return result.strip()




def randomRepeating():
    tries = 0
    num = 0
    while num != 10:
        num = random.randint(1,100)
        tries += 1
    print(f"it took {tries} tries to get a 10")

import random

def randomRange(n):
    highest = 0
    lowest = 101
    for i in range(n):
       num = random.randint(1,100)

       if num > highest:
           highest = num
       if num < lowest:
            lowest = num
    print("highest:", highest)
    print("lowest:", lowest)

def reverse(word:str)->str:
    result = ""
    index = len(word) -1

    while index >= 0:
       result += word[index]
       index -= 1

    return result

def fizzBuzzContinuous(n):
    """
    Modify the function such that it does the fizzbuzz operation on all numbers
    from 1 to n(inclusive).
    Fizz buzz is defined as
    if the number is divisble by 3 print fizz
    if the number is divisible by 5 print buzz
    if the number is divisible by both 3 and 5 print fizzbuzz
    if none of the above apply print the number.

    As with above questions add each anseer to a string and return the final string.
    :param n:
    :return:
    """
    out = ""
    for i in range(1,n+1):
        if i % 3 == 0 and i % 5 == 0:
            out = out +"fizzbuzz "
        elif i % 3 ==0:
            out = out +"fizz "
        elif i % 5 ==0:
            out = out +"buzz "
        else:
            out = out + str(i) + " "
    return out[0:len(out)-1]
    return out[:-1]
fizzBuzzContinuous(15)
def collatz(n):
    """
    Modify this function such that it mimics the collatz conjecture starting at n
    and prints out each number.
    The collatz conjecture is that if n is an even number divide it by 2. if n is
    an odd number multiply it by 3 and add 1.
    Repeat this process until n == 1.
    :param n:
    :return:
    """
    out = ""
    while n!= 1:
        out += str(n)+ " "
        if n % 2 ==0:
            n = n//2
        elif n % 1 ==0:
            n = n * 3 +1
    return out +"1"

print(collatz(16))
def fibonacci(n):
    """
    for the given argument n print out the first n numbers of the fibonacci
    sequence in a single string sperated by spaces.
    The fibonacci sequence is defined as a sequence that starts with 0 then 1 as
    the first two numbers. Every subsequent number is the prior two numbers added together.
    Example fibonacci(6) -> "0 1 1 2 3 5"
    Example fibonacci(10) -> "0 1 1 2 3 5 8 13 21 34"
    Example fibonacci(1) -> "0"
    :param n:
    :return:
    """
    if n <= 0:
        return ""
    if n == 1:
        return "0"
    result = "0 1"
    a = 0
    b = 1
    count = 2
    while count < n:
        c = a + b
        result += " " + str(c)
        a = b
        b = c
        count += 1
    return result

print(fibonacci(300))