# 평균구하기
# arr[1,2,3,4,5] -> answer=2.5

def solution(arr):
    answer = 0
    for i in range(len(arr)):
        answer += arr[i]
    return answer/len(arr)

