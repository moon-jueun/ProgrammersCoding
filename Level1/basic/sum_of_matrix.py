# 행렬의 덧셈
## 코드 추가 ## 
def solution(arr1, arr2):
    arr1 = [[1,2],[2,3]]
    arr2 = [[3,4],[5,6]]
    answer = []


    for i in range(len(arr1)):
        answer_1 = []
        for j in range(len(arr1[i])):
            answer_1.append(arr1[i][j] + arr2[i][j])
        answer.append(answer_1)
    return answer
