# Exercise 7
# Your solution comes here
def answer(num):
    str_num = str(num)
    return int(str_num[0]) + int(str_num[1]) + int(str_num[2]) + int(str_num[3])

num = int(input(""))
print(answer(num))