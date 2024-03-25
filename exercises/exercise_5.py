# Exercise 5
# Your solution comes here
def answer(num1, num2):
    return num1 * (num1 > num2) + num2 * (num2 > num1) + (num1 or num2) * (num1 == num2)

num1 = int(input(""))
num2 = int(input(""))
print(answer(num1, num2))
