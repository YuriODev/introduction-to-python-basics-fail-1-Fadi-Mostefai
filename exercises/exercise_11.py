# Exercise 11
# Your solution comes here

def demo(s):
  f = s // 500
  s -= f * 500
  h = s // 100
  s -= h * 100
  t = s // 10
  s -= t * 10
  v = s // 5
  s -= v * 5
  s1 = s
  
  
  return f"{f}(500), {h}(100), {t}(10), {v}(5), {s1}(1)"

s = int(input(""))
print(demo(s))