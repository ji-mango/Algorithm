'''
'트리의 부모 찾기'
문제 : 루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를
구하는 프로그램을 작성하시오.

입력 : 첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N-1개의 줄에
트리 상에서 연결된 두 정점이 주어진다.

출력 : 첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.

comment : 처음에 dfs로 풀다가 각 정점의 자식노드를 모두 확인해야 하기 때문에 bfs가 더 좋을 것이라
판단했다. 그리고 visited를 방문한 노드를 넣은 후 bfs함수에서 for문을
돌릴 때 'i not in visited'로 사용했더니 시간초과가 발생했다. 검색해보니 시간복잡도가 O(n)이여서
쓸데없이 시간을 잡아먹는다고 했다. 이후 False로 모두 초기화해준 후 비교하는 방식을 사용했다.
'''
from collections import deque
import sys

N = int(sys.stdin.readline())
root = [0] * (N+1)
visited = [False] * (N+1)
graph = [[] for i in range(N+1)]
for i in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(array, x):
    visited[x] = True
    queue = deque([x])
    while queue:
        n = queue.popleft()
        for i in graph[n]:
            if visited[i] != True:
                queue.append(i)
                visited[i] = True
                root[i] = n
    return root

result = bfs(graph, 1)
for i in range(2, len(result)):
    print(root[i])