

numberNisit = int(input("Nisit : "))

Dict_nisit = {}

def Cal_grade(List_scr):
    return sum(List_scr) / 7


for i in range(numberNisit):
    name = input("Name Nisit : ")
    list_score = []
    for work in range(0,7):
        try:
            x = float(input())
            list_score.append(x)
        except ValueError:
            list_score.append("error")
    result = []
    if "error" not in list_score:
        result.append(list_score)
        result.append(Cal_grade(list_score))
        Dict_nisit[name] = result
    else:
        result.append(list_score)
        result.append("error")
        Dict_nisit[name] = result


print(Dict_nisit)
