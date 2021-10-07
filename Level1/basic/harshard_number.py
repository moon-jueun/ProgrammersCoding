# 하샤드 수
# x = 11
def solution(x):
    arr_lst = list(map(int, str(x)))
    sum = 0
    for i in range(len(arr_lst)):
        sum += arr_lst[i]
    if x % sum == 0:
        answer = True
    else:
        answer = False

    return answer

