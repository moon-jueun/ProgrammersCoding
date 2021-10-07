phone_number = "01033334444"

def solution(phone_number):
    num_list = list(phone_number)
    num_split_1 = num_list[:-4]
    for i in range(len(num_split_1)):
            num_list[i] = '*'
    answer = "".join(num_list)
    return answer

ans = solution(phone_number)
print(ans)