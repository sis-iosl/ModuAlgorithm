A = ["Tom", "Jerry", "Mike", "Tom"]

def solution(A):
    n = len(A)
    result = set()
    for i in range(0, n-1):
        for j in range(i+1, n):
            if A[i] == A[j]:
                result.add(A[i])
    return result

print(solution(A))