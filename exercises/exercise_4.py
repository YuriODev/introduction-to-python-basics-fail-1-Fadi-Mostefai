# Exercise 4
# Your solution comes here
def sym(num):
    num_str = str(num)
    digit_1 = num_str[:2]
    return int((digit_1[-1] + digit_1[-2]) == (num_str[2] + num_str[3]))
    
num = int(input(""))
print(sym(num))