N = int(input("테스트 케이스의 개수 입력: "))

for i in range(N):
    OX = input()
    Score = 0
    sum_Score = 0
    for j in OX:
        if j == 'O':
            Score = Score + 1
        else:
            Score = 0
        sum_Score = sum_Score + Score
    print(sum_Score)