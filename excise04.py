n, d = map(int, input().split())

count = 0

for i in range(1, n+1):
    i = str(i)
    count += i.count(str(d))

print(count)
