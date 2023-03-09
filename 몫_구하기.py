def solution(num1,num2):
    answer = num1 // num2
    return answer
def otherSolution(num1,num2):
    answer = divmod(num1,num2)[0]
    return answer
print(solution(10,3))
print(otherSolution(10,3))
