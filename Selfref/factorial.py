def solution1(A):
    f = 1
    for i in range(1, A + 1):
        f = f * i
    return f

## 재귀를 통한 팩토리얼 구하기
def solution2(A):
    if A <= 1 :
        return 1
    return A * solution2(A-1)

print(solution1(5))
print(solution2(5))