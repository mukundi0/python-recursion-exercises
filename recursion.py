"""#1.Define a recursive function that takes two integers as input and returns their product using
repeated addition, without employing the multiplication operator."""
def multiply(a, b):
    if b == 0:
        return 0
    elif b > 0:
        return a + multiply(a, b -  1)
    else: # b < 0
        return -multiply(a, -b)

# print(multiply(2, 1))

"""#2.Define a recursive function that computes the result of raising a given base to a specified 
exponent, without using the exponentiation operator(**)"""
def power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent > 0:
        return base * power(base, exponent - 1)
    else: # exponent < 0
        return 1 or power(base, -exponent)
# print(power(2,3))

"""#3.Implement a recursive function that prints all integers from a given number n down to 0. """
def countdown(n):
    if n == 0:
        print(0)
        return
    print(n)
    countdown(n - 1)
# countdown(6)

"""#4. Implement a recursive function that prints all integers from 0 up to a given number n by modifying 
the previous countdown function."""
def countup(n):
    if n == 0:
        print(0)
    else:
        countup(n - 1)
        print(n)
# countup(3)

"""#5.Write a recursive function that takes a string as input and returns a reversed copy of the string, 
using only string concatenation. """
def reverse_string(s):
    if s == "":
        return ""
    else:
        return reverse_string(s[1:]) + s[0]

# print(reverse_string("dsa"))

"""#6.Write a recursive function that determines whether a given integer n is a prime number by 
checking for divisibility by integers less than n. """
def prime(n, divisor = 2):
    if n<=1:
        return False
    if divisor >= n:
        return True
    if n % divisor == 0:
        return False

    return prime(n, divisor + 1)

# print(prime(5))

"""#7.Write a recursive function that takes in one argument n and computes Fn, the nth value of the 
Fibonacci sequence. Recall that the Fibonacci sequence is defined by the relation Fn = Fn−1 + Fn−2 
where F0 = 0 and F1 =1"""
def fibonnaci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonnaci(n - 1) + fibonnaci(n - 2)

# print(fibonnaci(5))

#tower of hanoi
#Recursive function to solve the tower of Hanoi
def towerOfHanoi(n,source,target,auxiliary):
    if n==1:
        print(f"Move disk 1 from {source} to {target}")
        return
    else:
        towerOfHanoi(n-1,source,auxiliary,target)
        print(f"Move disk {n} from {source} to {target}")
        towerOfHanoi(n-1,auxiliary,target,source)

towerOfHanoi(6,'A','C','B')


"""SUM OF HARMONIC SERIES """
# Define a function named harmonic_sum that calculates the harmonic sum up to 'n' terms
def harmonicSum(n):
    if n<1:
        return 0
    else:
        return 1/n + harmonicSum(n-1)

# print(harmonicSum(4))

#Finding the sum of nested lists using recursion
def sumOfNestedList(listOfData):
    total=0
    for i in listOfData:
        if type(i)==type([]):
            total+=sumOfNestedList(i)
        else:
            total+=i
    return total
# print(sumOfNestedList([1,2,[3,4],[5,6]]))

#Finding the sum of a list using recursion
def sumOfList(listOfNumbers:list[int]):
    if len(listOfNumbers)==1:
        return listOfNumbers[0];
    else:
        return listOfNumbers[0]+sumOfList(listOfNumbers[1:])
# print(sumOfList([1,2,3,4,5,6,7,8,9,10]))

f_cache = {} #using dictionary key, value
value = 0
def fib2(number):
    if number in f_cache:
        return f_cache[number]
    if number == 1:
        value = 1
    elif number == 2:
        value = 1
    elif number > 2:
        value = fib2(number - 1) + fib2(number - 2)


    f_cache[number]= value
    return value

# for number in range(1,500):
#     print(n, "i", fib2(n))
#     print(f"{number} : {fib2(number)}")