'''
'여행 가자'
문제 : 동혁이는 친구들과 함께 여행을 가려고 한다. 한국에는 도시가 N개 있고 임의의 두 도시 사이에 길이 있을 수도, 없을 수도 있다. 
동혁이의 여행 일정이 주어졌을 때, 이 여행 경로가 가능한 것인지 알아보자. 물론 중간에 다른 도시를 경유해서 여행을 할 수도 있다. 
예를 들어 도시가 5개 있고, A-B, B-C, A-D, B-D, E-A의 길이 있고, 동혁이의 여행 계획이 E C B C D 라면 E-A-B-C-B-C-B-D라는 
여행경로를 통해 목적을 달성할 수 있다. 도시들의 개수와 도시들 간의 연결 여부가 주어져 있고, 동혁이의 여행 계획에 속한 도시들이 순서대로 
주어졌을 때 가능한지 여부를 판별하는 프로그램을 작성하시오. 같은 도시를 여러 번 방문하는 것도 가능하다.

입력 : 첫 줄에 도시의 수 N이 주어진다. N은 200이하이다. 둘째 줄에 여행 계획에 속한 도시들의 수 M이 주어진다. M은 1000이하이다. 
다음 N개의 줄에는 N개의 정수가 주어진다. i번째 줄의 j번째 수는 i번 도시와 j번 도시의 연결 정보를 의미한다. 1이면 연결된 것이고 0이면 연결이 되지 않은 것이다. 
A와 B가 연결되었으면 B와 A도 연결되어 있다. 마지막 줄에는 여행 계획이 주어진다. 도시의 번호는 1부터 N까지 차례대로 매겨져 있다.

출력 : 첫 줄에 가능하면 YES 불가능하면 NO를 출력한다.

풀이과정 : 1) go함수는 bfs를 이용하여 출발지와 목적지가 같으면 무조건 YES로 반환한다. 
        2) 아니라면 출발지를 queue에 넣어주고 출발지에서 갈 수 있는 경로를 탐색하여 만약 목적지가 갈 수 있는 경로에 포함된다면 YES를 반환, 그렇지 않다면 queue에 넣어주고 방문했다는 표시로 값을 0으로 바꿔준다.
        3) queue에 값이 없을 때까지 반복한다.
        4) 계획한 도시 수만큼 for문을 돌며 함수를 이용하여 다음 도시에 갈 수 있는지 확인한다.
        5) for문을 모두 돌아 result를 출력해준다.

comment : 다른 사람들의 답을 보니 union find알고리즘으로 많이 풀었는데, 나는 아직 union find알고리즘을 공부하지 않아서 bfs로 풀었다. 다른 bfs로 푼 사람의 답을 봤는데,
        나는 많이 비효율적으로 풀었다는 것을 알았다. 그냥 해당 도시에 방문했는지 여부를 체크하는 visit함수를 만들어서 bfs로 방문하지 않은 도시인 동시에 갈 수 있는 도시일 경우
        방문하는 식으로 풀면 되는 것이었다. 반복되는 도시는 어떡하나 싶었는데, 반복되는 도시일 경우 무조건 갈 수 있는 경로라서 괜찮은 것 같다.
        효율적으로 푸는 노력을 많이 해야되겠다.
'''
import sys

from copy import deepcopy
from collections import deque

n = int(input())
m = int(input())
array = []
for i in range(n):
      array.append(list(map(int, sys.stdin.readline().split())))

city = list(map(int, sys.stdin.readline().split()))

def go(start, end):
    global result
    if start == end:
        result="YES"
        return
    queue = deque([start])
    while queue:
        start = queue.popleft()
        for i in range(len(array[start])):
            if arrayCopy[start][i] == 1:
                if i == end:
                    result = "YES"
                    return
                queue.append(i)
                arrayCopy[start][i] = 0         # 방문했다는 표시를 해준다. 얘를 넣지 않으면 무한 반복하게 됨

result = "YES"
for i in range(len(city)-1):
    arrayCopy = deepcopy(array)
    result = "NO"
    go(city[i]-1, city[i+1]-1)
    if result == "YES":
        continue
    else:
        break
if len(city) == 1 or 0:
    result = "YES"

print(result)