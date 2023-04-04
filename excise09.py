def factorial(N):
    if N == 0:
        return 1
    return N * factorial(N-1)

N = int(input("정수입력: "))
print(factorial(N))