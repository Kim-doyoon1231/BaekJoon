# ATM
n=int(input())
line = list(map(int, input().split()))
line.sort()
answer = 0
sum = 0
for i in line:
    sum += i
    answer += sum
print(answer)