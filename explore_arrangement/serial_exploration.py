A = [17, 92, 18, 33, 58, 7, 33, 42]

def serial(a, x):
    for i in range(0, len(a)):
        if a[i] == x:
            return i
    return -1

print(serial(A, 18))