def solution(angle):
    if angle == 180:
        return 4
    elif 90 < angle < 180:
        return 3
    elif angle == 90:
        return 2
    else:
        return 1

print(solution(100))
