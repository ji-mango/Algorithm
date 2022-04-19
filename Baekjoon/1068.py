'''
'트리'
문제 : 
문제
트리에서 리프 노드란, 자식의 개수가 0인 노드를 말한다.
트리가 주어졌을 때, 노드 하나를 지울 것이다. 그 때, 남은 트리에서 리프 노드의 개수를 구하는 프로그램을 작성하시오. 노드를 지우면 그 노드와 노드의 모든 자손이 트리에서 제거된다.

입력 : 첫째 줄에 트리의 노드의 개수 N이 주어진다. N은 50보다 작거나 같은 자연수이다. 둘째 줄에는 0번 노드부터 N-1번 노드까지, 각 노드의 부모가 주어진다. 
만약 부모가 없다면 (루트) -1이 주어진다. 셋째 줄에는 지울 노드의 번호가 주어진다.

출력 : 첫째 줄에 입력으로 주어진 트리에서 입력으로 주어진 노드를 지웠을 때, 리프 노드의 개수를 출력한다.

comment : 노드의 개수가 50개밖에 주어지지 않아서 부모 인덱스에 자식 노드 번호를 넣는 배열을 만들어주었다. dfs를 돌면서 만약 삭제한 노드를 만날 경우에는
아예 그 경로로 가지 않게 해주었다. 처음에 지우려는 노드 부모의 자식이 지우려는 노드밖에 없을 경우를 생각해주지 않아서 오답처리가 됐는데, 질문 게시판에서 힌트를
얻어 이 경우를 생각해야한다는 것을 알게되었고, 삭제하려는 노드를 만날 경우에 부모 노드의 자식 개수를 세서 1일 경우 리프노드 개수를 +1 해주었다.

'''
n = int(input())
temp = list(map(int, input().split()))
a = int(input())
root = 0

array = [[]for i in range(50)]
for i in range(len(temp)):
    if temp[i] == -1:
        root = i
    else:
        array[temp[i]].append(i)

def dfs(t, parent):
    global a
    global cnt
    if t == a:
        if len(array[parent])==1:              # 지우려는 노드의 부모의 자식이 지우려는 노드 하나밖에 없을 경우
            cnt += 1
        return cnt
    elif len(array[t]) == 0:
        cnt += 1
        return cnt 
    else:
        for i in range(len(array[t])):
            dfs(array[t][i], t)

cnt = 0
dfs(root, -1)
print(cnt)