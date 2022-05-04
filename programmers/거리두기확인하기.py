def dfs(array, cnt, x, y):                                  # 맨해튼 거리 2안에 사람이 있는지 체크하는 함수  
    global result
    if cnt > 2:                                             # 맨해튼 거리가 2초과일 경우 result값을 변경하지 않고 return
        return
    if array[x][y] == 'X':                                  # 캐비닛이 쳐져있을 경우 result값을 변경하지 않고 return
        return                                               # (없어도 되는 조건문 but 실행시간을 조금 줄일 수 있음)
    if cnt != 0 and array[x][y] == 'P':                     # 거리가 2를 초과하기 전에 P(사람)가 있을 경우 result를 0으로 변경
        result = 0
        return
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        mx = x + dx[i]
        my = y + dy[i]
        if mx < 0 or mx >= 5 or my < 0 or my >= 5:
            continue   
        elif array[mx][my] == 'X' or array[mx][my] == 'V':
            continue
        else:
            # 문자열을 바꿔주기 위해(방문 표시를 위해) 리스트로 변환해서 값 변경하고 다시 문자열로 리스트에 삽입
            temp = list(array[x])                           
            temp[y] = 'V'                                 
            array[x] = ''.join(temp)                         
            dfs(array, cnt+1, mx, my)
                
def solution(places):
    answer = []
    
    for i in range(5):
        global result
        result = 1
        array = places[i]
        for j in range(5):
            for k in range(5):
                if array[j][k] == 'P':      # 사람이 앉아있을 때만 함수 실행
                    dfs(array, 0, j, k)
                if result == 0:
                    break
            if result == 0:
                break
        answer.append(result)
                
    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))