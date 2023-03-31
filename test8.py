n = int(input("숫자입력: ")) 
Fibo = [0, 1] 

for i in range(2, n+1): 
    Fibo.append(Fibo[i-1] + Fibo[i-2])

print(Fibo[n])