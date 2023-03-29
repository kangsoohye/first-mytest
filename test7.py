N = int(input("정수입력: ")) 
s=2 
while N!=1: 
    if N%s == 0: 
        print(s) 
        N = N//s 
    else: 
        s = s+1 