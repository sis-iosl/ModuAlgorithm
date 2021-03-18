
A = [17, 92, 18, 33, 58, 7, 33, 42]

## 최대값을 찾는 함수
def solution1(A):
    max_value = A[0]
    for i in range(0, len(A)):
        if A[i] > max_value:
            max_value = A[i]
    return max_value

## 최소값을 찾는 함수
def solution2(A):
    min_value = A[0]
    for i in range(0, len(A)):
        if A[i] < min_value:
            min_value = A[i]
    return min_value

## 최대값의 자리를 찾는 함수
def solution3(A):
    ## max_value = A[0]
    max_value_p = 0
    for i in range(0, len(A)):
        if A[i] > A[max_value_p]:
            ## max_value = A[i]
            max_value_p = i
    return max_value_p

print(solution1(A))
print(solution2(A))
print(solution3(A))