# Exercise 1
# Your solution comes here
def sum_coversion(num):
  str_num = str(num)
  return str(int(str_num[0]) + int(str_num[2]) + int(str_num[4])) + str(int(str_num[1]) + int(str_num[3]))
number = int(input(""))
print(sum_coversion(number))