'''
'골드바흐의 추측'
문제 : 1742년, 독일의 아마추어 수학가 크리스티안 골드바흐는 레온하르트 오일러에게 다음과 같은 추측을 제안하는 편지를 보냈다.
4보다 큰 모든 짝수는 두 홀수 소수의 합으로 나타낼 수 있다.
예를 들어 8은 3 + 5로 나타낼 수 있고, 3과 5는 모두 홀수인 소수이다. 또, 20 = 3 + 17 = 7 + 13, 42 = 5 + 37 = 11 + 31 = 13 + 29 = 19 + 23 이다.
이 추측은 아직도 해결되지 않은 문제이다.
백만 이하의 모든 짝수에 대해서, 이 추측을 검증하는 프로그램을 작성하시오.

입력 : 입력은 하나 또는 그 이상의 테스트 케이스로 이루어져 있다. 테스트 케이스의 개수는 100,000개를 넘지 않는다.
각 테스트 케이스는 짝수 정수 n 하나로 이루어져 있다. (6 ≤ n ≤ 1000000)
입력의 마지막 줄에는 0이 하나 주어진다.

출력 : 각 테스트 케이스에 대해서, n = a + b 형태로 출력한다. 이때, a와 b는 홀수 소수이다. 숫자와 연산자는 공백 하나로 구분되어져 있다.
만약, n을 만들 수 있는 방법이 여러 가지라면, b-a가 가장 큰 것을 출력한다. 또, 두 홀수 소수의 합으로 n을 나타낼 수 없는 경우에는
"Goldbach's conjecture is wrong."을 출력한다.

comment : 처음에는 prime 배열을 두번 돌아서 합이 입력받은 수와 같을 때 b-a차가 가장 큰 것을 정답으로 출력하는 식으로 코드를 짜서 시간초과가 떴다.
그 다음에는 prime을 한 번은 앞에서 한번은 뒤에서 돌아서 입력받은 수와 합이 같으면 출력했는데, 그래도 시간초과가 떴다. 고민하다가 입력받은 수에서
prime의 소수를 뺀 값이 소수인지 확인하면 for문을 한 번만 돌아도 된다는 것을 알았다.
'''
import sys
import math

array = []
i = 1
while i != 0:
  i = int(sys.stdin.readline())
  array.append(i)

array.pop(-1)
length = len(array)
n = 1000000
prime = [True for i in range(n+1)]
for i in range(2, int(math.sqrt(n)) + 1):
    if prime[i] == True:
        p = 2
        while p * i <= n:
            prime[p*i] = False
            p += 1

a = []
b = []
for i in range(length):
    for j in range(3, array[i]):
        if prime[j] == True:
            if prime[array[i]-j] == True:
                a.append(j)
                b.append(array[i]-j)
                break

for i in range(length):
    print(str(array[i]) + " = " + str(a[i]) + " + " + str(b[i]))

