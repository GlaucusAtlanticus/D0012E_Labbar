# Edvin Petterson
# Jonatan Trefil
# Rasmus Jacobsen

# Lab 2
# 2021.12.XX

import random

# Function that creates a list so that
# size n = 3 * 2^(k-1)
def GenListPart1(k):
   list = []

   size = 3 * 2**(k-1)

   for x in range(0, size):                       # Iterates size times meaning amount of elements is size
      number = random.randint(-size,size)         # range of numbers
      list.append(number)                         # Adds numbers to list

   return list

# Function that creates a list so that
# size n = 2^k. And elements are non 0
def GenListPart2(k):
   list = []

   size = 2**k

   for x in range(0, size):                       # Iterates size times meaning amount of elements is size
      number = random.randint(1,size)             # range of numbers, non zero so lowest is 1
      list.append(number)           

   return list