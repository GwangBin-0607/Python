def solution(dot):
    if dot[0] > 0 and dot[1]>0:
        return 1
    elif dot[0] < 0 and dot[1] < 0:
        return 3
    elif dot[0] < 0 and dot[1] > 0:
        return 2
    else: return 4
print(solution((1,-5)))
