# Exercise 6
# Your solution comes here
def check(num1, num2):
    return "YES" * (num1 % num2 == 0) + "NO" * (num1 % num2 != 0)

num1 = int(input(""))
num2 = int(input(""))
print(check(num1, num2))