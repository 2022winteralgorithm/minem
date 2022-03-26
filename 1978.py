N = int(input())

number = map(int, input().split())

decimal = 0
for num in number:
    error = 0
    if num > 1:
        for i in range (2, num):
            if num % i == 0:
                error += 1
        if error == 0:
                decimal += 1

print(decimal)
