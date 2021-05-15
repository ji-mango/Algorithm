'''
'별 찍기 - 10'
문제 : 재귀적인 패턴으로 별을 찍어 보자. N이 3의 거듭제곱(3, 9, 27, ...)이라고 할 때,
크기 N의 패턴은 N×N 정사각형 모양이다.
크기 3의 패턴은 가운데에 공백이 있고, 가운데를 제외한 모든 칸에 별이 하나씩 있는 패턴이다.
***
* *
***
N이 3보다 클 경우, 크기 N의 패턴은 공백으로 채워진 가운데의 (N/3)×(N/3) 정사각형을 크기
N/3의 패턴으로 둘러싼 형태이다.

comment : 규칙을 완벽히 파악하는게 중요했고, 재귀를 쓸 수 있을 것 같은데 그것을 적용하는 것이
너무 어려웠다. 결국 내 힘으로 온전히 풀지 못하고 다른 사람의 코드를 참고했다.
'''

'''
#내 틀린 풀이
n=int(input())
li=[]

for _ in range(n):
    li.append(['*' for _ in range(n)])

for i in range(n):
    for j in range(n):
        if (i % 3 == 1) and (j % 3 == 1):
            li[i][j] = ' '

def stars(N):
    if N == 3:
        return li
    
    for i in range(int(N/3),int(2*(N/3))):
        for j in range(int(N/3),int(2*(N/3))):
            li[i][j]=' '
    N=int(N/3)
    stars(N)

stars(n)

for i in range(n):
    for j in range(n):
        print(li[i][j],end='')
    print()
'''
n=int(input())
v=n
cnt=0
while v!=1:
    v=v/3
    cnt+=1

arr = [["*"]*n for _ in range(n)]

def stars(i):
    idx=[i for i in range(n) if (i // (3 ** cnt_)) % 3 == 1]
    for i in idx:
        for j in idx:
            arr[i][j]=' '


for cnt_ in range(cnt):
    stars(cnt_)

print("\n".join([''.join([str(i) for i in row]) for row in arr]))
