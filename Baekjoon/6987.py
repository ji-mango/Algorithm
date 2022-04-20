'''
'월드컵'
문제 : 월드컵 조별 최종 예선에서는 6개국으로 구성된 각 조별로 동일한 조에 소속된 국가들과 한 번씩, 각 국가별로 총 5번의 경기를 치른다.
조별리그가 끝난 후, 기자가 보내온 각 나라의 승, 무승부, 패의 수가 가능한 결과인지를 판별하려고 한다. 
네 가지의 결과가 주어질 때 각각의 결과에 대하여 가능하면 1, 불가능하면 0을 출력하는 프로그램을 작성하시오.

입력 : 첫째 줄부터 넷째 줄까지 각 줄마다 6개국의 결과가 나라별로 승, 무승부, 패의 순서로 빈칸을 하나 사이에 두고 18개의 숫자로 주어진다. 
승, 무, 패의 수는 6보다 작거나 같은 자연수 또는 0이다.

출력 : 입력에서 주어진 네 가지 결과에 대하여 가능한 결과는 1, 불가능한 결과는 0을 빈칸을 하나 사이에 두고 출력한다.

comment : 처음에는 승과 패를 비교하여 같은지 확인하고, 무승부를 빼고 더해서 0이 되는지 확인하는 방식으로 풀었는데, 15%에서 틀렸다. 결국 답을 참고하여
조합과 재귀를 통해 풀었다. 풀이방법은 다음과 같다.
1) 조합으로 팀들의 모든 경기할 수 있는 조합을 구한다.
2) 해당 팀에 해당하는 게임 결과의 승패 또는 무승부인 곳에 -1을 한다.
3) 재귀로 반복하여 round가 15때 남은 게임결과 수가 모두 0이 아닐 경우 result를 0, 모두 0일 경우 1로 만든다.
4) 함수에서 나올 경우 데이터를 원래대로 되돌려놓기 위해 +1을 해준다.

'''
from itertools import combinations
result = []     # 결과 담는 배열

def check(round):
    global r
    if round == 15:
        r = 1
        for i in range(len(array)):
            if array[i].count(0) != 3:
                r = 0
                break
        return
    
    t1, t2 = com[round]
    for x, y in ((0,2), (1,1), (2,0)):
        if array[t1][x] > 0 and array[t2][y] > 0:
            array[t1][x] -= 1
            array[t2][y] -= 1
            check(round+1)
            array[t1][x] += 1
            array[t2][y] += 1

com = list(combinations(range(6), 2))

for i in range(4):
    array = list(map(int, input().split()))
    array = [array[i:i+3] for i in range(0, 16, 3)]
    r = 0
    check(0)
    result.append(r)

for i in result:
    print(i, end=' ')