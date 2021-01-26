def find_time(badge_records ):
    badge_records.sort(key=lambda x: int(x[1]))
    first = []
    max_set = set()
    current_person = []
    for person, time, action in badge_records:
        if action == "enter":
            if not current_person:
                current_person.append({person})
            else:
                new = [{person}]
                for s in current_person:
                    news = set(s)
                    news.add(person)
                    new.append(news)
                current_person.extend(new)
        else:
            remove_list = []
            for s in current_person:
                if person in s:
                    if s not in first:
                        first.append(s)
                    else:
                        if len(s) > len(max_set):
                            max_set = s
                    remove_list.append(s)
            for s in remove_list:
                current_person.remove(s)
        print(current_person)
    print(max_set)

    # find interval
    current_p = set()
    interval = []
    for person, time, action in badge_records:
        if person not in max_set:
            continue
        if action == "enter":
            current_p.add(person)
            if current_p == max_set:
                interval.append([time])
        else:
            if current_p == max_set:
                interval[-1].append(time)
            current_p.remove(person)
    print(interval)

    print(','.join(max_set) + ':')


def main():
    badge_records = [
        ["Paul", "1214", "enter"],
        ["Paul", "830", "enter"],
        ["Curtis", "1100", "enter"],
        ["Paul", "903", "exit"],
        ["John", "908", "exit"],
        ["Paul", "1235", "exit"],
        ["Jennifer", "900", "exit"],
        ["Curtis", "1330", "exit"],
        ["John", "815", "enter"],
        ["Jennifer", "1217", "enter"],
        ["Curtis", "745", "enter"],
        ["John", "1230", "enter"],
        ["Jennifer", "800", "enter"],
        ["John", "1235", "exit"],
        ["Curtis", "810", "exit"],
        ["Jennifer", "1240", "exit"],
    ]
    find_time(badge_records)
main()





