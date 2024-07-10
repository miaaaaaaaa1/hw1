#1

def text():
 string1 = '''\033[90m"Don't compare yourself with anyone in this world…\033[0m
\033[31mif\033[0m you \033[31mdo so\033[0m, you are insulting yourself.\033[90m"\033[0m'''
 print(string1)
 print("Bill Gates" + '\033[0m')

text()

#2

def numbers(start, end):
    for m in range(start, end):
        if m % 2 == 0:
            print(m)

numbers(2,20)

#3

def square(side, symbol, filled):
    if side < 1:
        print("Side length should be greater than 0.")
        return
    
    for i in range(side):
        if filled or i == 0 or i == side - 1:
            print(symbol * side)
        else:
            print(symbol + ' ' * (side - 2) + symbol)

square(5, '*', True)

#4

def num(a, b, c, d, e):
    return min(a, b, c, d, e)

print(num(4, 7, 1, 3, 8))

#5

def product(start, end):
    if start > end:
        start, end = end, start
    
    product = 1
    for i in range(start, end + 1):
        product *= i
    
    return product

print(product(1, 5))

#6

def count(number):
    return len(str(number))

print(count(45687))

#7

def is_palindrome(number):
    str_number = str(number)
    
    return str_number == str_number[::-1]

print(is_palindrome(123321))