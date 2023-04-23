#백준 10156번 - 과자
K, M, N = map(int, input().split())
result = (K*N)-M

if result > M:
    print(result)
else:
    print(0)

