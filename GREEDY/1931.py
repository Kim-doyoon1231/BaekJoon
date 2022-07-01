# 회의실 배정
# n개의 회의, 각 회의가 겹치지 않게 하며 회의실을 사용할 수 있는 회의의 최대 개수를 찾아보자
# 회의실은 한개
# 최대한 빨리 시작, 빨리 끝나면 좋겠다.
# 그렇다고 먼저 시작하기만 한다고 최대로 할 수 있는 것은 아니다. -> 빠른 시간에 끝나는 순으로 정렬을 해보자
import sys
input = sys.stdin.readline

n = int(input())
time_table = []
for i in range(n):
    s,t = map(int, input().split())
    time_table.append([s,t])
time_table.sort(key = lambda x: (x[1], x[0]))
start_time = time_table[0][0]
end_time = time_table[0][1]
cnt = 1
for i in range(1,n):
    if end_time<=time_table[i][0]:
        start_time = time_table[i][0]
        end_time = time_table[i][1]
        cnt+=1
print(cnt)