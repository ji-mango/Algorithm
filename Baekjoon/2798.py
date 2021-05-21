'''
'블랙잭'
문제 : 각 카드에는 양의 정수가 쓰여 있다. 그 다음, 딜러는 N장의 카드를 모두 숫자가 보이도록
바닥에 놓는다. 그런 후에 딜러는 숫자 M을 크게 외친다. 이제 플레이어는 제한된 시간 안에 N장의
카드 중에서 3장의 카드를 골라야 한다. 블랙잭 변형 게임이기 때문에, 플레이어가 고른 카드의 합은
M을 넘지 않으면서 M과 최대한 가깝게 만들어야 한다. N장의 카드에 써져 있는 숫자가 주어졌을 때,
M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 구해 출력하시오.

comment : 처음에 M에 가깝기만 하면 되는 줄 알고 헤맸다. 다른 코드에서는 combinations 모듈을
사용하던데 모듈들도 많이 배워놔야겠다.
'''
N,M = map(int, input().split())
li = list(map(int, input().split()))  # 카드에 쓰여있는 수 리스트
add_list = []

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            if li[i]+li[j]+li[k] > M:
                continue
            add_list.append(li[i]+li[j]+li[k])

sub = 1000000                         # M과의 차(절대값) 계산
result=0
for i in add_list:
    if M-i<sub:
        result = i
        sub=M-i

print(result)







