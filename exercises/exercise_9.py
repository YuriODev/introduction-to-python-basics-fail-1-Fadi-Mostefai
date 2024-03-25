# Exercise 9
# Your solution comes here
def convert(h,m,s):
    return (30 * h) + (0.5 * m) + ((0.5 / 60) * s)

h = int(input(""))
m = int(input(""))
s = int(input(""))

print(convert(h,m,s))