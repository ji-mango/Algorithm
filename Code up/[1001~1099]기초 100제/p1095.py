'''
번호를 부른 횟수(n, 1 ~ 10000)가 첫 줄에 입력된다.
n개의 랜덤 번호(k, 1 ~ 23)가 두 번째 줄에 공백을 사이에 두고 순서대로 입력된다.

출석을 부른 번호 중에 가장 빠른 번호를 1개만 출력한다.
'''
a=int(input())
b=map(int,input().split())
b=list(b)
m=999
for i in range(a):
    if m>b[i]:
        m=b[i]
print(m)
