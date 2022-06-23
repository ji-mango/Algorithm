'''
'게리맨더링 2'

comment : 좀 많이 비효율적으로 푼 것 같아서 다른 사람들 코드를 봤는데 중복순열을 쓰지 않아도 되는 문제였다.
진짜 비효율적으로 풀었다.. 다음에 다시 풀어야겠다.
'''
from collections import deque
from itertools import product

n = int(input())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))

select_list = [i for i in range(1, n)]
result = []
visited = [False] * len(select_list)
answer = 9999999

def solu(perm):
    global n, answer
    x, y, d1, d2 = perm
    
    if (x < x+d1+d2) and (x+d1+d2 <= n) and (1 <= y-d1) and (y-d1 < y) and (y < y+d2) and (y+d2 <= n):
        # 5구역에 해당하는 좌표 저장하는 집합자료형 선언
        people5_list = set()

        # 조건 2에 따라 설정
        for i in range(d1+1):
            people5_list.add((x+i, y-i))
            people5_list.add((x+d2+i, y+d2-i))
        for i in range(d2+1):
            people5_list.add((x+i, y+i))
            people5_list.add((x+d1+i, y-d1+i))

        people5_list = sorted(people5_list)

        people1 = 0             # 구역당 인구 수 저장
        people2 = 0
        people3 = 0
        people4 = 0
        people5 = 0

        for i in range(n):
            for j in range(n):
                end = 0
                length = len(people5_list)

                # 해당 좌표가 5구역인지 여부 판단
                for k in range(length):
                    if k == 0 or k == length-1:
                        if i+1 == people5_list[k][0] and j+1 == people5_list[k][1]:
                            end = 1
                            break
                    elif k % 2 == 1:
                        if i+1 == people5_list[k][0] and j+1 >= people5_list[k][1] and j+1 <= people5_list[k+1][1]:
                            end = 1
                            break
                
                # 조건 4에 따라 설정
                if end == 1:
                    people5 += board[i][j]
                elif (i+1 < x+d1) and (j+1 <= y):
                    people1 += board[i][j]
                elif (i+1 <= x+d2) and (j+1 > y) and (j+1 <= n):
                    people2 += board[i][j]
                elif (x+d1 <= i+1) and (i+1 <= n) and (j+1 < y-d1+d2):
                    people3 += board[i][j]
                elif (x+d2 < i+1) and (i+1 <= n) and (j+1 >= y-d1+d2) and (j+1 <= n):
                    people4 += board[i][j]
        
        temp = max(people1, people2, people3, people4, people5) - min(people1, people2, people3, people4, people5)
        if temp < answer:
            answer = temp

perm = product(select_list, repeat=4)
for i in perm:
    solu(i)

print(answer)
