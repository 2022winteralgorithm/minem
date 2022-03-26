N = int(input())   #68

n = N
cnt = 0

while True:
    a = n // 10   #6
    b = n % 10   #8
    c = a + b   #14
    num = (b * 10) + (c % 10)   #84
    cnt += 1
    if num == N:
        break
    n = num

print(cnt)
