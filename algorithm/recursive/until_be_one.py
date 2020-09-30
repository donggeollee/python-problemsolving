# 문제: 정수 4를 1, 2, 3의 조합으로 나타내는 방법은 다음과 같이 총 7가지가 있음
# 1+1+1+1
# 1+1+2
# 1+2+1
# 2+1+1
# 2+2
# 1+3
# 3+1
# 정수 n이 입력으로 주어졌을 때, n을 1, 2, 3의 합으로 나타낼 수 있는 방법의 수를 구하시오

def case_count(num):
    if num == 1 :
        return 1
    elif num == 2 :
        return 2
    elif num == 3  :
        return 4
    return case_count(num-1) + case_count(num-2) + case_count(num-3)

print(case_count(5))

