resultTime = []
timetable = [1700, 1820, 1830, 1950, 2000, 2120]

def function(start, end):

    if start < 1200 or 2200 < start or end < 1200 or 2300 < end or start >= end:
        resultTime.append(-1)
        return 0
    
    s = 0
    if 1630 <= start <= 1645:
        resultTime.append(1645)

    elif 1800 <= start <= 1815:
        resultTime.append(1815)
        s = 2
        
    elif 1930 <= start <= 1945:
        resultTime.append(1945)
        s = 4
    else:
        resultTime.append(-1)
        return
        
    e = 5
    while end <= timetable[e]:
            e -= 2

    while s <= e:
        resultTime.append(timetable[s])
        s += 1

    resultTime.append(end)

x = int(input())
y = int(input())
function(x, y)
print(resultTime)