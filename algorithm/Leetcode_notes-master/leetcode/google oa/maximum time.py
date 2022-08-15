

def max_time(time):
    miss = set()
    for i in range(len(time)):
        if time[i] == "?":
            miss.add(i)
    if len(miss) == 4:
        return 2
    if len(miss) == 3:
        if 0 in miss:
            return 2
        elif time[0] == "2":
            return 4
        else:
            return 5
    if len(miss) == 2:
        if 0 in miss:
            return 2
        if 3 in miss and time[0] == "2":
            return 4
        elif 3 in miss:
            return 5
        else:
            return 9
    if len(miss) == 1:
        if 0 in miss:
            return 2
        elif 3 in miss:
            return 5
        else:
            return 9

def main():
    time = "2?:?2"
    result = max_time(time)
    print(result)
main()

