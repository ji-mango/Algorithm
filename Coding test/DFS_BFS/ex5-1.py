'''
'음료수 얼려 먹기'
문제 : N * M 크기의 얼음 틀이 있다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다.
구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주한다.
이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하시오.

입력 : - 첫 번째 줄에 얼음 틀의 세로 길이 N과 가로 길이 M이 주어진다.(1<=N, M<=1000)
      - 두 번째 줄부터 N+1번째 줄까지 얼음 틀의 형태가 주어진다.
      - 이때 구멍이 뚫려있는 부분은 0, 그렇지 않은 부분은 1이다.
출력 : 한번에 만들 수 있는 아이스크림의 개수를 출력한다.

comment : 처음 푸는 탐색알고리즘 문제라 어떻게 풀어야될지 감이 안와서 답을 참고했다. 재귀함수를 사용하는 것에
좀 더 익숙해질 필요가 있는 것 같다.
'''
N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input())))

def dfs(x, y):
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

result = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j) == True:
            result += 1

print(result)
