import sys

input = sys.stdin.readline

while True:
    n = int(input())
    if n == -1:
        break
    
    A_list = []
    sum = 0

    for i in range(1, n):
        if n % i == 0:
            A_list.append(str(i))
            sum += i
            
    if sum == n:
        print(f"{n} = " + "+".join(A_list))
    else:
        print(f"{n} is NOT perfect")