import sys
input = sys.stdin.readline
n, k = map(int, input().split())
coin = []
answer = 0
for i in range(n):
    coin.append(int(input()))
for i in range(n-1, -1,-1):
    if coin[i] <= k:
        answer += k//coin[i]
        k = k%coin[i]
print(answer)
