'''
'수 정렬하기 3'
문제 : N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

comment : 범위가 작을 때는 계수정렬(카운팅정렬)이 좋다는 것을 알았다. 처음에 count를 10000까지만
만들어서 인덱스 에러가 떴다. 이런 문제에서 항상 +1을 해야된다는 것을 잊지 말자
'''
import sys
N = int(input())

count = [0] * 10001

for i in range(N):
    num = int(sys.stdin.readline())
    count[num] += 1

for i in range(10001):
    for j in range(count[i]):
        print(i)