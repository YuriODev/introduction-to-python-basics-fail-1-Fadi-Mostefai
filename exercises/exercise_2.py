# Exercise 2
# Your solution comes here
def next_even(num):
    return (num + 2) * (num % 2 == 0) + (num + 1) * (num % 2 != 0)

num = int(input(""))
print(next_even(num))