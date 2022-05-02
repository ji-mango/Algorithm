'''
'이차원 배열과 연산'
문제 : 크기가 3×3인 배열 A가 있다. 배열의 인덱스는 1부터 시작한다. 1초가 지날때마다 배열에 연산이 적용된다.
R 연산: 배열 A의 모든 행에 대해서 정렬을 수행한다. 행의 개수 ≥ 열의 개수인 경우에 적용된다.
C 연산: 배열 A의 모든 열에 대해서 정렬을 수행한다. 행의 개수 < 열의 개수인 경우에 적용된다.
한 행 또는 열에 있는 수를 정렬하려면, 각각의 수가 몇 번 나왔는지 알아야 한다. 그 다음, 수의 등장 횟수가 커지는 순으로, 그러한 것이 여러가지면 수가 커지는 순으로 정렬한다. 
그 다음에는 배열 A에 정렬된 결과를 다시 넣어야 한다. 정렬된 결과를 배열에 넣을 때는, 수와 등장 횟수를 모두 넣으며, 순서는 수가 먼저이다.
예를 들어, [3, 1, 1]에는 3이 1번, 1가 2번 등장한다. 따라서, 정렬된 결과는 [3, 1, 1, 2]가 된다. 다시 이 배열에는 3이 1번, 1이 2번, 2가 1번 등장한다. 
다시 정렬하면 [2, 1, 3, 1, 1, 2]가 된다.
정렬된 결과를 배열에 다시 넣으면 행 또는 열의 크기가 달라질 수 있다. R 연산이 적용된 경우에는 가장 큰 행을 기준으로 모든 행의 크기가 변하고, 
C 연산이 적용된 경우에는 가장 큰 열을 기준으로 모든 열의 크기가 변한다. 행 또는 열의 크기가 커진 곳에는 0이 채워진다. 수를 정렬할 때 0은 무시해야 한다. 
예를 들어, [3, 2, 0, 0]을 정렬한 결과는 [3, 2]를 정렬한 결과와 같다.
행 또는 열의 크기가 100을 넘어가는 경우에는 처음 100개를 제외한 나머지는 버린다.
배열 A에 들어있는 수와 r, c, k가 주어졌을 때, A[r][c]에 들어있는 값이 k가 되기 위한 최소 시간을 구해보자.

입력 : 첫째 줄에 r, c, k가 주어진다. (1 ≤ r, c, k ≤ 100)
둘째 줄부터 3개의 줄에 배열 A에 들어있는 수가 주어진다. 배열 A에 들어있는 수는 100보다 작거나 같은 자연수이다.

출력 : A[r][c]에 들어있는 값이 k가 되기 위한 연산의 최소 시간을 출력한다. 100초가 지나도 A[r][c] = k가 되지 않으면 -1을 출력한다.

comment : 구현문제는 머리를 너무 많이써야해서 힘들다. 이 코드는 python3으로 제출하면 시간초과가 뜨고 pypy3으로 제출해야 시간초과가 뜨지 않는다.
내 코드는 효율성이 조금 떨어지는 것 같아서 다 풀고나서 블로그를 몇개 찾아봤는데, zip함수를 사용하여 열이 행이 되도록 만들어주는 것을 보고 충격먹었다.
다음에는 zip써야지..
'''
import operator
from copy import deepcopy

r, c, k = map(int, input().split())
a = []
for i in range(3):          
    a.append(list(map(int, input().split())))

result = 0
while True:
    if len(a) >= r and len(a[0]) >= c and a[r-1][c-1] == k:
        break
    if result > 100:
        result = -1
        break
    result += 1
    if len(a) >= len(a[0]):     # R연산 수행
        lenA = len(a)
        if lenA > 100:          # 처음 100개를 제외한 나머지는 버린다.(행)
            lenA = 100
        changeA = []            # 바꿀 배열
        max = 0
        for i in range(lenA):   
            lenAA = len(a[i])
            if lenAA > 100:
                lenAA = 100     # 처음 100개를 제외한 나머지는 버린다.(열)
            changeA.append([])
            dic = {}            # 각 숫자의 개수를 담을 dictonary
            for j in range(lenAA):
                temp = a[i][j]  
                if temp not in dic: # dic에 키로 없는 숫자 추가
                    dic[temp] = 0
                dic[temp] += 1
            dic = sorted(dic.items())                       # key값 기준 오름차순 정렬
            dic = sorted(dic, key=operator.itemgetter(1))   # value값 기준 오름차순 정렬
           
            cnt = 0                                         # 배열에서 가장 긴 값을 찾기 위해 count
            for j in range(len(dic)):
                if dic[j][1] != 0 and dic[j][0] != 0:       # 키가 0인 값은 무시
                    changeA[i].append(dic[j][0])
                    changeA[i].append(dic[j][1])
                    cnt += 2
            if cnt > max:
                max = cnt
        
        a = deepcopy(changeA)
        for i in range(lenA):
            if len(a[i]) < max:                             # 길이가 max보다 작다면 그만큼 0으로 채움
                for j in range(len(a[i]), max):
                    a[i].append(0)

    else:                       # C연산 수행
        lenA = len(a)
        lenAA = len(a[0])
        changeA = [[0 for i in range(200)] for i in range(200)] # 0으로 최대 길이까지 채워준다.
        max = 0
        for j in range(lenAA):
            dic = {}
            for i in range(lenA):
                temp = a[i][j]
                if temp not in dic:
                    dic[temp] = 0
                dic[temp] += 1
            dic = sorted(dic.items())                       # key값 기준 오름차순 정렬
            dic = sorted(dic, key=operator.itemgetter(1))   # value값 기준 오름차순 정렬
            cnt = 0
            t = 0
            for i in range(len(dic)):                       
                if dic[i][1] != 0 and dic[i][0] != 0:       # key가 0인 값은 무시 
                    changeA[t][j] = dic[i][0]                           
                    t += 1
                    changeA[t][j] = dic[i][1]
                    t += 1
                    cnt += 2
            if cnt > max:
                max = cnt
        a = deepcopy(changeA)
        a = a[:max]                                         # 배열 행을 max값 만큼 자름                                   
        for j in range(len(a)):
            a[j] = a[j][:lenAA]                             # 열을 max값 만큼 자름

print(result)
