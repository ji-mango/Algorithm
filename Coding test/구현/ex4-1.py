'''
'상하좌우'
문제 : 여행가 A는 N X N 크기의 공간 위에 서 있다. 여행가 A는
       상(U), 하(D), 좌(L), 우(R) 방향으로 이동할 수 있으며 시작 좌표는 항상
       (1,1)이다. 우리 앞에는 A가 이동할 계획이 적힌 계획서가 놓여있다.
       이때 A가 공간을 벗어나는 움직임은 무시된다.
       첫째 줄에 공간의 크기를 나타내는 N이 입력된다.
       둘째 줄에 A가 이동할 계획서 내용이 주어진다.

       여행가 A가 최종적으로 도착할 지점의 좌표 (X,Y)를 공백으로 구분하여 출력한다.

배운 점 : 리스트를 효율적으로 사용하면 코드의 길이가 짧아질 수 있다는 것과,
         이 코드에서 continue문을 사용하려면 nx,ny라는 변수를 만들어놓고 써야한다는 것을 알았다.
'''
N = int(input())
plan = list(input().split())
x,y = 1,1
for i in plan:
    if i=='L':
        y=y-1
    elif i=='R':
        y=y+1
    elif i=='U':
        x=x-1
    elif i=='D':
        x=x+1
    if x<1:
        x=x+1
    if x>N:
        x=x-1
    if y<1:
        y=y+1
    if y>N:
        y=y-1

print("%s %s" % (x, y))

#답안 예시
'''
N=int(input())
x,y=1,1
plans=input().split()
dx=[0,0,-1,1]
dy=[-1,1,0,0]
move_types=['L','R','U','D]

for plan in plans:
    for i in range(len(move_types()):
    if plan==move_types[i]:
        nx=x+dx[i]
        ny=y+dy[i]
    if nx<1 or ny<1 or nx<N or ny<N:
        continue
    x,y=nx,ny

print(x, y)
'''


