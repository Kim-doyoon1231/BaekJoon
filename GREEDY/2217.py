# 로프
# n개의 로프
# k개의 로프를 이용하여 무게가 w인 물체를 들어올릴 때 각각의 로프는 w/k만큼 들게 된다.
# 해당 로프들을 이용하여 들어올릴 수 있는 물체의 최대 중량을 구해보자
# n개의 로프를 모두 사용할 필요는 없다.

n = int(input())
answer = []
for i in range(n):
    answer.append(int(input()))
answer.sort(reverse=True)
answer2 = [0]*n
for i in range(n):
    answer2[i] = (i+1)*answer[i]
answer2.sort()
print(answer2[-1])

