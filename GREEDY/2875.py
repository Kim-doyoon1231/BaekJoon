n,m,k = map(int, input().split())
# n명의 여학생 m명의 남학생 k명은 인턴쉽 참여해야한다
# 여학생 2명과 남학생 1명이 팀을 결성하여 대회에 나간다.
# 만들 수 있는 팀의 최대 개수를 출력하자
for i in range(k):
    if n//2>=m:
        n -=1
    else:
        m -= 1
print(min(n//2, m))