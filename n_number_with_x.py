# x만큼 간격이 있는 n개의 숫자
def solution(x, n):
    answer = []
    sum = x
    for i in range(n):
        answer.append(sum)
        sum += x
    return print(answer)

x = int(input())
n = int(input())

solution(x,n)