'''
'녹색 옷 입은 애가 젤다지?'

풀이 : 1. N이 0이 아닐 때까지 while문을 반복한다.(0이 나오면 종료)
      2. 2차원 배열로 입력되는 도둑루피들의 정보를 graph에 일차원배열로 넣는다.(첫번째 테스트케이스의 경우 [1,0] 좌표 정보를 graph[4]에 넣음)
      3. 다익스트라 알고리즘을 수행한다.
      4. distance마지막 값과 맨 처음의 도둑 루피값을 더하여 출력한다.

'''
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
problem = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def d(start):
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = i[1] + dist
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

while True:
    N = int(input())
    if N == 0:
        break
    problem += 1
    graph = [[] for i in range(N*N + 1)]
    distance = [INF] * (N*N + 1)

    for i in range(N):
        data = list(map(int, input().split()))
        if i == 0:
            first = data[0]
        for j in range(N):
            for k in range(4):
                mx = i + dx[k]
                my = j + dy[k]
                if mx < 0 or mx >= N or my < 0 or my >= N:
                    continue
                graph[mx*N+my+1].append((i*N+j+1, data[j]))
    d(1)    
    answer = distance[N*N] + first
    print("Problem %d: %d" %(problem, answer))