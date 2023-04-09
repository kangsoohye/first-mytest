N, M = map(int, read().split())

A = list(map(int, read().split()))
B = list(map(int, read().split()))
answer = []

answer = A + B
answer.sort()

print("", join*(map(str,answer)))