__author__ = 'jean'

#==============Question 1====================================================


#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.


n = 0
for i in range(1,1000):
    if not i % 5 or not i % 3:
     n = n + i
print(n)



#Euler Project Question2=========================================================

#Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#Find the sum of all the even-valued terms in the sequence which do not exceed four million.


def sum_even_fib(n):
    sumfib = 0
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
        if b % 2 == 0:
            sumfib = sumfib + b
    return sumfib

print(sum_even_fib(4000000))

#================Question3 for Euler Project====================================

#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?
# the solution ia 6857.0

n = 600851475143
i = 2
while i * i < n:
     while n % i == 0:
         n = n / i
     i = i + 1
print(n)

#==============================Question 4 Euler Project===============================================


#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

#Find the largest palindrome made from the product of two 3-digit numbers.

n = 0
for a in range(999, 100, -1):
    for b in range(a, 100, -1):
        x = a * b
        if x > n:
            s = str(a * b)
            if s == s[::-1]:
                n = a * b
print(n)

#=========================================Question 5 Euler Project=========================================

#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest number that is evenly divisible by all of the numbers from 1 to 20?


def gcd(a, b):
    return b and gcd(b, a % b) or a

def lcm(a, b):
    return a * b / gcd(a, b)

n = 1
for i in range(1, 21):
    n = lcm(n, i)

print(n)

#=========================Question 6 Euler Project====================================================


#The sum of the squares of the first ten natural numbers is,
#1^2 + 2^2 + ... + 10^2 = 385
#The square of the sum of the first ten natural numbers is,
#(1 + 2 + ... + 10)^2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


r = range(1, 101)
a = sum(r)
print(a * a - sum(i*i for i in r))


#========================Question 7 Euler Project=============================================================


# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10001st prime number?

import prime
print(prime.prime(10000))