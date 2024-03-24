# Exercise 3
# Your solution comes here
def time(sec):
    minutes = 0
    hours = 0
    minutes = sec // 60
    sec -= (minutes * 60)
    if minutes >= 60:
            hours = minutes // 60
            minutes -= (hours * 60)
    if minutes < 10 and sec < 10:
        return f"{hours}:0{minutes}:0{sec}"
    elif sec < 10:
        return f"{hours}:{minutes}:0{sec}"
    elif minutes < 10:
        return f"{hours}:0{minutes}:{sec}"
    else:
        return f"{hours}:{minutes}:{sec}"

sec = int(input(""))
print(time(sec))