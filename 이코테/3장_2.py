import sys

n, m, k = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

lst.sort()
num1 = lst[n-1]
num2 = lst[n-2]

cnt = (m//k+1) * k
cnt += m % (k+1)

result = cnt * num1 + (m-cnt) * num2

print(result)
