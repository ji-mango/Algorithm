'''
'원판 돌리기'
'''
from queue import deque

N, M, T = map(int, input().split())
score = [[0]]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

sum_score = 0         # 점수의 합
num_score = N*M       # 점수의 개수

for i in range(N):
    score.append(list(map(int, input().split())))
    sum_score += sum(score[i+1])
    
for i in range(T):
    x, d, k = map(int, input().split())

    # x의 배수 원판 회전
    if x <= N:
        for _ in range(k):                                      # k번 돌기때문에 k번 반복(시간초과뜨면 반복문 도는게 아니라 인덱스를 조절하려 했는데 안뜬다 대박)
            for j in range(x, N+1, x):
                if d == 0:                                      # 시계 방향 회전
                    before = score[j][-1]
                    for k in range(M):
                        before, score[j][k] = score[j][k], before
                else:                                           # 반시계 방향 회전
                    before = score[j][0]
                    for k in range(M-1, -1, -1):
                        before, score[j][k] = score[j][k], before


    del_cnt = 0                                                 # 원판에 인접한 수가 아예 없을 경우를 구분하기 위한 변수
    for j in range(1, N+1):
        for k in range(M):
            temp = score[j][k]
            if temp != 'x':
                q = deque()
                for z in range(4):
                    mx = j + dx[z]
                    my = k + dy[z]
                    if mx < 1 or mx >= N+1:
                        continue
                    elif my >= M:
                        my = 0
                    if score[mx][my] == score[j][k]:            # 인접한 수가 있다면 q에 집어넣음
                        q.append([mx, my])
                        del_cnt += 1
                if len(q) == 0:                                 # 해당 좌표에서 인접한 수가 없으면 continue
                    continue
                else:                                           # 인접한 수가 있을 경우 bfs방식으로 인접한 수 확인하여 제거
                    sum_score -= score[j][k]
                    num_score -= 1
                    score[j][k] = 'x'
                    while q:
                        a, b = q.popleft()
                        if score[a][b] != 'x':                  # 방문처리를 따로 하지 않으므로 큐에 좌표가 중복하여 들어갈 수 있기 때문에 'x'인지 체크
                            sum_score -= score[a][b]
                            num_score -= 1
                            score[a][b] = 'x'
                            for z in range(4):
                                mx = a + dx[z]
                                my = b + dy[z]
                                if mx < 1 or mx >= N+1:
                                    continue
                                elif my >= M:
                                    my = 0
                                if score[mx][my] == temp:
                                    q.append([mx, my])
        
    if del_cnt == 0:                                            # 원판에 인접한 수가 아예 없는 경우 문제 조건 2-2 수행
        if num_score == 0:
            avg = 0
        else:
            avg = sum_score / num_score
        for j in range(1, N+1):
            for k in range(M):
                if score[j][k] != 'x':
                    if score[j][k] > avg:
                        score[j][k] -= 1
                        sum_score -= 1
                    elif score[j][k] < avg:
                        score[j][k] += 1
                        sum_score += 1

print(sum_score)
