#!/usr/bin/env python3

#This code uses While and If statements to checks if a number is power of two.
#It returns True if it is power of two or returns False if it is not

def is_power_of_two(n):
  # Check if the number can be divided by two without a remainder
  while n != 0 and n % 2 == 0:
    n = n / 2
  # If after dividing by two the number is 1, it's a power of two
  if n == 1:
    return True
  return False


print(is_power_of_two(0)) # Should be False
print(is_power_of_two(1)) # Should be True
print(is_power_of_two(8)) # Should be True
print(is_power_of_two(9)) # Should be False
