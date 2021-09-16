'''
'단지번호붙이기'
문제 : 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 철수는
이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 여기서
연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 대각선상에 집이
있는 경우는 연결된 것이 아니다. 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를
오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.

입력 : 첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고,
그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.

출력 : 첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지내 집의 수를 오름차순으로 정렬하여
한 줄에 하나씩 출력하시오.

comment : 처음엔 탐색 알고리즘이 되게 어려웠는데 한번 손에 익으니까 어떻게 푸는지 살짝 감이 오는 것 같다.
'''
N = int(input())
d = 0
graph = []
for i in range(N):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    global count
    if graph[x][y] == 1:
        graph[x][y] = 2
        count += 1
    for i in range(4):
        mx = x+dx[i]
        my = y+dy[i]
        if mx < 0 or my < 0 or mx >= N or my >= N:
            continue
        elif graph[mx][my] == 1:
            dfs(mx, my)

cnt = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            d += 1
            cnt.append(0)
            count = cnt[d-1]
            dfs(i, j)
            cnt[d-1] = count

print(d)
cnt.sort()
for i in cnt:
    print(i)
