'''
'피보나치 함수'
문제 : fibonacci(3)을 호출하면 다음과 같은 일이 일어난다.
        -fibonacci(3)은 fibonacci(2)와 fibonacci(1) (첫 번째 호출)을 호출한다.
        -fibonacci(2)는 fibonacci(1) (두 번째 호출)과 fibonacci(0)을 호출한다.
        -두 번째 호출한 fibonacci(1)은 1을 출력하고 1을 리턴한다.
        -fibonacci(0)은 0을 출력하고, 0을 리턴한다.
        -fibonacci(2)는 fibonacci(1)과 fibonacci(0)의 결과를 얻고, 1을 리턴한다.
        -첫 번째 호출한 fibonacci(1)은 1을 출력하고, 1을 리턴한다.
        -fibonacci(3)은 fibonacci(2)와 fibonacci(1)의 결과를 얻고, 2를 리턴한다.
      1은 2번 출력되고, 0은 1번 출력된다. N이 주어졌을 때, fibonacci(N)을 호출했을 때, 0과 1이 각각 몇 번 출력되는지 구하는 프로그램을 작성하시오.

입력 : 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
각 테스트 케이스는 한 줄로 이루어져 있고, N이 주어진다. N은 40보다 작거나 같은 자연수 또는 0이다.

출력 : 각 테스트 케이스마다 0이 출력되는 횟수와 1이 출력되는 횟수를 공백으로 구분해서 출력한다.

comment : f(0)과 f(1)의 갯수를 저장하는 이중 DP테이블 c를 만들고 한번 돌 때마다 x-1, x-2의 값을 더해주는 방식으로 구현했다.
다른사람들의 풀이를 보니까 재귀를 사용하지 않고 규칙찾아서 푼 코드도 많았다.
풀고나니까 이렇게 간단한걸 2시간 반동안 풀었다.. DP문제를 좀 많이 풀어야할 것 같다.
'''
t = int(input())
array = []
for i in range(t):
    array.append(int(input()))

def fibo(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    if d[x] != -1:
        return d[x]
    d[x] = fibo(x-1) + fibo(x-2)
    c[x][0] = c[x-1][0] + c[x-2][0]
    c[x][1] = c[x-1][1] + c[x-2][1]
    return d[x]

for i in range(t):
    temp = array[i]
    d = [-1] * 41
    d[0], d[1] = 0, 0
    c = [[0,0] for i in range(41)]
    c[0] = [1, 0]
    c[1] = [0, 1]
    fibo(temp)
    print(c[temp][0], c[temp][1])