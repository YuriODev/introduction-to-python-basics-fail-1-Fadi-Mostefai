# Exercise 8
# Your solution comes here
def sort(a, b, c):
    minimum = min(a, b, c)
    maximum = max(a, b, c)
    middle = (a + b + c) - minimum - maximum
    return minimum, middle, maximum
    

num1 = int(input(""))
num2 = int(input(""))
num3 = int(input(""))
min, mid, max = sort(num1, num2, num3)
print(min)
print(mid)
print(max)