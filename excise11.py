import sys

N = input()
F = int(input())

A = int(N[:-2]+'00')

while True :
    if A % F == 0:
        break
    A += 1
    
print(str(A)[-2:])