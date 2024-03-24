# Exercise 2
# Your solution comes here
def next_even(num):
    if num % 2 == 0:
        return num + 2
    else:
        return num + 1

num = int(input(""))
print(next_even(num))