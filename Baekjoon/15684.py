'''
'사다리 조작'
문제 : 사다리 게임은 N개의 세로선과 M개의 가로선으로 이루어져 있다. 인접한 세로선 사이에는 가로선을 놓을 수 있는데, 각각의 세로선마다 가로선을 놓을 수 있는 위치의 개수는 H이고, 모든 세로선이 같은 위치를 갖는다.
초록선은 세로선을 나타내고, 초록선과 점선이 교차하는 점은 가로선을 놓을 수 있는 점이다. 가로선은 인접한 두 세로선을 연결해야 한다. 단, 두 가로선이 연속하거나 서로 접하면 안 된다. 또, 가로선은 점선 위에 있어야 한다.
사다리 게임은 각각의 세로선마다 게임을 진행하고, 세로선의 가장 위에서부터 아래 방향으로 내려가야 한다. 이때, 가로선을 만나면 가로선을 이용해 옆 세로선으로 이동한 다음, 이동한 세로선에서 아래 방향으로 이동해야 한다.
사다리에 가로선을 추가해서, 사다리 게임의 결과를 조작하려고 한다. 이때, i번 세로선의 결과가 i번이 나와야 한다. 그렇게 하기 위해서 추가해야 하는 가로선 개수의 최솟값을 구하는 프로그램을 작성하시오.

입력 : 첫째 줄에 세로선의 개수 N, 가로선의 개수 M, 세로선마다 가로선을 놓을 수 있는 위치의 개수 H가 주어진다. (2 ≤ N ≤ 10, 1 ≤ H ≤ 30, 0 ≤ M ≤ (N-1)×H)
둘째 줄부터 M개의 줄에는 가로선의 정보가 한 줄에 하나씩 주어진다.
가로선의 정보는 두 정수 a과 b로 나타낸다. (1 ≤ a ≤ H, 1 ≤ b ≤ N-1) b번 세로선과 b+1번 세로선을 a번 점선 위치에서 연결했다는 의미이다.
가장 위에 있는 점선의 번호는 1번이고, 아래로 내려갈 때마다 1이 증가한다. 세로선은 가장 왼쪽에 있는 것의 번호가 1번이고, 오른쪽으로 갈 때마다 1이 증가한다.
입력으로 주어지는 가로선이 서로 연속하는 경우는 없다.

출력 : i번 세로선의 결과가 i번이 나오도록 사다리 게임을 조작하려면, 추가해야 하는 가로선 개수의 최솟값을 출력한다. 만약, 정답이 3보다 큰 값이면 -1을 출력한다. 또, 불가능한 경우에도 -1을 출력한다.

comment : 마의 9%를 뚫을 수 없었다.... 꿈에 시간초과가 나올거같다....... 다음에 다시풀자..
'''
from itertools import product, combinations
import copy

n, m, h = map(int, input().split())
array = [[]]
for i in range(m):
    array.append(list(map(int,input().split())))

def check(i):                          # 사다리가 자기자신에게 가는지 체크하는 함수
    which = i
    for j in range(1, h+1):
        for k in range(1, len(arrayCopy)):
            if j == arrayCopy[k][0]:
                line = arrayCopy[k][1]
                if which == line:
                    which = line+1
                    break
                elif which-1 == line:
                    which = line
                    break
    if which == i:
        return True
    else:
        return False

answerList = [i for i in range(n+1)]            # 최종결과가 answerList와 같아야함

list1 = [i for i in range(1, n)]
list2 = [i for i in range(1, h+1)]
two_li = [list2, list1]
com = list(product(*two_li))                    # 가로선이 나올 수 있는 모든 경우의 수

for i in range(1, m+1):                         # 모든 가로선 중 원래 있는 가로선, 원래있는 가로선과 일직선으로 놓여지는 가로선 제거
    k = array[i]
    if tuple(k) in com:
        com.remove(tuple(k))
    a = array[i][0]
    b = array[i][1]
    if b-1 > 0:
        if (a,b-1) in com:
            com.remove((a, b-1))
    if b+1 < n:
        if (a,b+1) in com:
            com.remove((a, b+1))

for i in range(0, 4):                       # 가로선 3개까지 조작 가능
    com2 = list(combinations(com, i))   
    for z in range(len(com2)):
        arrayCopy = copy.deepcopy(array)
        for x in com2[z]:
            arrayCopy.append(list(x))
        for y in range(1, n+1):
            result = check(y)
            if result == False:
                break
        if result == True:
            print(i)
            break
    if result == True:
        break
if result == False:
    print(-1)