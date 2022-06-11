'''
'카드 구매하기'

입력 : 첫째 줄에 민규가 구매하려고 하는 카드의 개수 N이 주어진다. (1 ≤ N ≤ 1,000)
둘째 줄에는 Pi가 P1부터 PN까지 순서대로 주어진다. (1 ≤ Pi ≤ 10,000)

출력 : 첫째 줄에 민규가 카드 N개를 갖기 위해 지불해야 하는 금액의 최댓값을 출력한다.

풀이 : 1. 자기자신이 max인 경우도 있기 때문에 d를 array로 초기화해준다.
      2. 앞에서부터 자기자신까지 모든 경우의 수를 살펴보며 max인 것을 찾는다.

comment : 코드는 굉장히 단순한데 이해하기가 너무 어려웠다. 별거 아닌거같았는데 dp문제는 항상 내 뒤통수를 친다.
그리고 dp문제는 이해한 것을 말로 풀이하는 것이 정말 어렵다. 말로 적어야 더 이해가 가고 오래 기억에 남을 것 같아서 계속 연습하고 있는데,
쉽지가 않다.

'''
n = int(input())
array = [0] + list(map(int, input().split()))

d = [0 for i in range(n+1)]
for i in range(n+1):
    d[i] = array[i]

for i in range(n+1):
    for j in range(i+1):
        d[i] = max(d[i], d[i-j] + d[j])

print(d[n])

    