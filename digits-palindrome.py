# Write a program that checks whether an integer is a palindrome. 
# For example, 121 is a palindrome, as well as 888. 
# 678 is not a palindrome. 
# Do not convert the integer into a string.

def is_palindrome(num):
    if num < 0:
        return False

    original_num = num
    reverse_num = 0

    while num > 0:
        digit = num % 10
        reverse_num = reverse_num * 10 + digit
        num //= 10

    return original_num == reverse_num
