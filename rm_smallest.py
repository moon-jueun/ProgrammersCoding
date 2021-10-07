# 제일 작은 수 제거하기
arr = [4,3,2,1]
# return [4,3,2]
smallest = arr[0]
answer = []
if len(arr) > 1:
    for i in range(len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
    arr.remove(smallest)
    answer = arr
else:
    answer = [-1]

print(answer)