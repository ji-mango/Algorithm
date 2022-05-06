'''
처음에 배열로 풀었는데, 효율성에서 모두 실패가 뜨는 것을 보고 다른 자료구조로 풀어야겠다고 생각했다.
그런데 어떻게 해야할지 몰라서 답을 참고해 연결 리스트를 사용하여 풀었다. 연결리스트는 파이썬으로 처음 구현해보는데, 
생각보다 어려워서 많이 헤맸다. 머릿속에 그림을 그려가면서 하니까 그래도 조금 쉽게 이해할 수 있었다.
'''

def solution(n, k, cmd):
    cur = k
    linkedList = {i:[i-1, i+1] for i in range(n)}
    linkedList[0] = [None, 1]
    linkedList[n-1] = [n-2, None]
    result = ['O'] * n
    deleteList = []
    
    for i in cmd:
        '''
        # 이 코드는 2자리수 이상 이동할 경우를 생각하지 않았다. 
        if i[0] == 'U':
            print(int(i[2]))
            for j in range(int(i[2])):
                cur = linkedList[cur][0]

        elif i[0] == 'D':
            print(int(i[2]))
            for j in range(int(i[2])):
                cur = linkedList[cur][1]
        '''
        
        if i[0] == 'C':
            before, after = linkedList[cur]
            deleteList.append([cur, before, after])
            result[cur] = 'X'
            if after == None:
                cur = before
            else:
                cur = after
            if before == None:
                linkedList[after][0] = None
            elif after == None:
                linkedList[before][1] = None
            else:
                linkedList[before][1] = after
                linkedList[after][0] = before

        elif i[0] == 'Z':
            now, prev, nxt = deleteList.pop()
            result[now] = 'O'
            if prev == None:
                linkedList[nxt][0] = now
            elif nxt == None:
                linkedList[prev][1] = now
            else:
                linkedList[nxt][0] = now
                linkedList[prev][1] = now
        
        else:
            # 커서 이동
            c1, c2 = i.split(' ')
            c2 = int(c2)
            if c1 == 'D':
                for _ in range(c2):
                    cur = linkedList[cur][1]
            else:
                for _ in range(c2):
                    cur = linkedList[cur][0]
        
    return ''.join(result)

print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))