'''
'소형기관차'
문제 : 기차는 맨 앞에 있는 기관차 1대가 손님이 탄 객차 여러 칸을 끌고 간다. 기관차가 고장나면 기차를 운행할 수 없게 되므로 최근 철도청은 
기관차 고장에 대비하여 몇몇 역에 소형 기관차 3대를 배치하기로 결정하였다. 소형 기관차는 평소에 이용하는 기관차보다 훨씬 적은 수의 객차만을 끌 수 있다.
기관차가 고장났을 때 끌고 가던 객차 모두를 소형 기관차 3대가 나누어 끌 수 없기 때문에, 소형 기관차들이 어떤 객차들을 끌고 가는 것이 좋을까하는 
문제를 고민하다가 다음과 같이 하기로 결정하였다.
1. 소형 기관차가 최대로 끌 수 있는 객차의 수를 미리 정해 놓고, 그보다 많은 수의 객차를 절대로 끌게 하지 않는다. 3대의 소형 기관차가 최대로 끌 수 있는 객차의 수는 서로 같다.
2. 소형 기관차 3대를 이용하여 최대한 많은 손님을 목적지까지 운송하도록 한다. 각 객차 마다 타고 있는 손님의 수는 미리 알고 있고, 다른 객차로 손님들이 이동하는 것은 허용하지 않는다.
3. 각 소형 기관차는 번호가 연속적으로 이어진 객차를 끌게 한다. 객차는 기관차 바로 뒤에 있는 객차부터 시작하여 1번 부터 차례로 번호가 붙어있다.

예를 들어 기관차가 끌고 가던 객차가 7칸이고, 소형 기관차 1대가 최대로 끌 수 있는 객차 수는 2칸이라고 하자. 그리고 1번 부터 7번까지 각 객차에 타고 있는 
손님의 수가 아래 표와 같다고 하자. 괄호속에 있는 숫자는 객차 번호를 나타낸다.
(1)	(2)	(3)	(4)	(5)	(6)	(7)
35	40	50	10	30	45	60
소형 기관차 3대는 각각 1-2번, 3-4번, 그리고 6-7번 객차를 끌고 가면 손님 240명을 운송할 수 있고, 이보다 많은 수의 손님을 운송할 수 없다.
기관차가 끌고 가던 객차의 수와 각 객차에 타고 있던 손님의 수, 그리고 소형 기관차가 최대로 끌수 있는 객차의 수가 주어질 때, 소형 기관차 3대를 이용하여 
최대로 운송할 수 있는 손님 수를 구하는 프로그램을 작성하시오.

입력 : 첫째 줄에 기관차가 끌고 가던 객차의 수가 입력된다. 그 수는 50,000 이하이다. 둘째 줄에는 기관차가 끌고 가던 객차에 타고 있는 손님의 수가 1번 객차부터 차례로 입력된다. 
한 객차에 타고 있는 손님의 수는 100명 이하이고, 입력되는 숫자들 사이에 빈칸이 하나씩 있다. 셋째 줄에는 소형 기관차가 최대로 끌 수 있는 객차의 수가 입력된다. 
그 수는 기관차가 끌고 가던 객차 수의 1/3보다 적다.

출력 : 한 줄에 소형 기관차 3대를 이용하여 최대로 운송할 수 있는 손님 수를 출력한다.

풀이 : dp테이블은 dp[기관차 인덱스][객차 인덱스] 2차배열로 만들어야 한다. 
      최대로 끌 수 있는 객차수를 b라 할 때,
      첫번 째 기관차 점화식 - max(dp[0][현재 객차 idx-1], (현재 객차 idx - b)부터 (현재 객차 idx)까지의 손님수)
      2,3번 째 기관차 점화식 - max(dp[현재 기관차 idx][현재 객차 idx-1], dp[현재기관차-1][현재 객차 idx-b] + (현재 객차 idx - b)부터 (현재 객차 idx)까지의 손님수)
      s배열은 해당 인덱스 까지의 객차의 손님 수를 누적한 배열로, '(현재 객차 idx - b)부터 (현재 객차 idx)까지의 손님수'를 쉽게 구하기 위해 만들었다.

comment : dp로 풀어야할 것 같다는 생각은 들었는데, 점화식을 도출해내는 것이 어려워서 결국 답을 참고했다. dp는 역시 점화식을 뽑아내는 것이
정말 어려운 알고리즘 같다. 그래도 dp로 풀어야 한다는 것을 떠올렸기 때문에 많이 발전했다고 생각한다.
'''
import sys

a = int(input())
array = list(map(int, sys.stdin.readline().split()))
b = int(input())

d = [[0 for i in range(a)] for i in range(3)]
s = [0 for i in range(a+1)]

sum = 0
for i in range(a):
    sum += array[i]
    s[i] = sum

for i in range(3):
    for j in range(b+i*b-1, a):
        if i == 0:                  # 첫 번째 객차일 경우
            d[i][j] = max(d[i][j-1], s[j]-s[j-b])
        else:
            d[i][j] = max(d[i][j-1], d[i-1][j-b] + s[j]-s[j-b])

print(d[2][a-1])