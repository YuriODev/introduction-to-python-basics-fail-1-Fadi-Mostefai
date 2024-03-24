# Exercise 7
# Your solution comes here
def answer(num):
    sum = 0
    str_num = str(num)
    for number in str_num:
        sum += int(number)
    return sum

num = int(input(""))
print(answer(num))