# 강의실 배정
# 최소의 강의실 사용 -> 시작 시간이 빠를 수록 종료 시간이 빠를 수록 적게 사용 가능 -> sort이용
# 수업이 끝난 직후에 다음 수업을 시작 할 수 있다 - 3에 끝나고 3에 시작 가능
# 우선 우리는 정렬 상태를 유지 해야 하므로 우선순위 큐를 사용해야한다. 크기가 작은 것부터 정렬된다.
# 답지를 보고서야 이해를 하였다. 다시 한번 더 유의해서 봐야할 듯
# 이런 유형은 참 많이 나오는 것 같다.
import heapq
import sys
input = sys.stdin.readline
cnt = 1
n = int(input())
time_table = []
for i in range(n):
    s, t = map(int, input().split())
    time_table.append([s,t])
time_table.sort(key = lambda x:x[0])
answer = []
heapq.heappush(answer, time_table[0][1])
for i in range(1,n):
    if time_table[i][0]>=answer[0]:
        heapq.heappop(answer)
    heapq.heappush(answer, time_table[i][1])
print(len(answer))