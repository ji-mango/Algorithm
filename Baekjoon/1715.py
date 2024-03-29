'''
'카드 정렬하기'
문제 : 정렬된 두 묶음의 숫자 카드가 있다고 하자. 각 묶음의 카드의 수를 A, B라 하면 보통 두 묶음을 합쳐서 하나로 만드는 데에는 A+B 번의 비교를 해야 한다. 
이를테면, 20장의 숫자 카드 묶음과 30장의 숫자 카드 묶음을 합치려면 50번의 비교가 필요하다.
매우 많은 숫자 카드 묶음이 책상 위에 놓여 있다. 이들을 두 묶음씩 골라 서로 합쳐나간다면, 고르는 순서에 따라서 비교 횟수가 매우 달라진다. 
예를 들어 10장, 20장, 40장의 묶음이 있다면 10장과 20장을 합친 뒤, 합친 30장 묶음과 40장을 합친다면 (10 + 20) + (30 + 40) = 100번의 비교가 필요하다. 
그러나 10장과 40장을 합친 뒤, 합친 50장 묶음과 20장을 합친다면 (10 + 40) + (50 + 20) = 120 번의 비교가 필요하므로 덜 효율적인 방법이다.
N개의 숫자 카드 묶음의 각각의 크기가 주어질 때, 최소한 몇 번의 비교가 필요한지를 구하는 프로그램을 작성하시오.

입력 : 첫째 줄에 N이 주어진다. (1 ≤ N ≤ 100,000) 이어서 N개의 줄에 걸쳐 숫자 카드 묶음의 각각의 크기가 주어진다. 
숫자 카드 묶음의 크기는 1,000보다 작거나 같은 양의 정수이다.

출력 : 첫째 줄에 최소 비교 횟수를 출력한다.

풀이 : 1. 입력받는 카드 묶음의 크기 배열을 빠르게 정렬하기 위해 우선순위 큐로 선언한다.
      2. 비교횟수를 저장할 배열 result를 선언한다.
      3. 입력받은 array의 크기가 2이상일 동안 앞의 두 카드 묶음을 합쳐 비교횟수를 저장하고 합친 카드는 result와 array(합친카드는 다시 비교해야 하므로)에 넣어준다.
      4. 입력받은 카드가 한묶음일 때 비교할 필요가 없으므로 0을 출력하고, 그렇지 않은 경우에는 result의 합을 출력한다.

comment : 처음에는 array를 배열로 선언하고 while문에서 sort와 pop함수를 사용하여 정렬, 삭제하는 바람에 시간복잡도가 n^2이 되었고, 데이터 수가 100,000개이기 때문에 
당연히 시간초과가 떴다. 
우선순위 큐는 입력 순서에 상관없이 우선순위에 따라 작동하는 자료구조이다. 삽입과 삭제 시간 복잡도가 O(logN)이고, 정렬할 필요가 없기 때문에 우선순위 큐를 사용했을 때, 
시간초과가 나지 않을 수 있었다.
'''
import sys
from queue import PriorityQueue

n = int(input())
array = PriorityQueue()
for i in range(n):
    array.put(int(sys.stdin.readline()))

result = []
while array.qsize() >= 2:
    temp = array.get(0) + array.get(1)
    result.append(temp)
    array.put(temp)

if n == 1:
    print(0)
else:
    print(sum(result))