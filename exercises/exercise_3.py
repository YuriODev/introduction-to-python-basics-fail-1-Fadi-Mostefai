# Exercise 3
# Your solution comes here
def time(sec):
    minutes = 0
    hours = 0
    minutes = sec // 60
    sec -= (minutes * 60)
    hours = minutes // 60
    minutes -= (hours * 60)
    hours -= (hours % 24) * (hours > 24)
    return (f"{hours}:0{minutes}:0{sec}") * (minutes < 10 and sec < 10) + (f"{hours}:{minutes}:0{sec}") * (sec < 10 and minutes > 10) + (f"{hours}:0{minutes}:{sec}") * (minutes < 10 and sec > 10) + (f"{hours}:{minutes}:{sec}") * (minutes > 10 and sec > 10)

sec = int(input(""))
print(time(sec))