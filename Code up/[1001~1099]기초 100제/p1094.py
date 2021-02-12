'''
번호를 부른 횟수(n, 1 ~ 10000)가 첫 줄에 입력된다.
n개의 랜덤 번호(k, 1 ~ 23)가 두 번째 줄에 공백을 사이에 두고 순서대로 입력된다.

출석을 부른 번호 순서를 바꾸어 공백을 두고 출력한다.
'''
a=int(input())
b=map(int,input().split())
b=list(b)
i=a-1
for j in range(a):
    print(b[i])
    i-=1
