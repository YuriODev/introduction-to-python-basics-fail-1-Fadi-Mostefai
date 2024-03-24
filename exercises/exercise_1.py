# Exercise 1
# Your solution comes here
def sum_coversion(num):
  digit1 = 0
  digit2 = 0
  str_num = str(num)
  for i in range(1, len(str_num) + 1):
    if i % 2 == 0:
      digit2 += int(str_num[i-1])
    else:
      digit1 += int(str_num[i-1])
  sum = str(digit1) + str(digit2)
  return sum

number = int(input("Enter a number "))
print(sum_coversion(number))