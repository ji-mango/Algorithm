'''
'회의실 배정'
문제 : 한 개의 회의실이 있는데 이를 사용하고자 하는 N개의 회의에 대하여 회의실 사용표를
만들려고 한다. 각 회의 I에 대해 시작시간과 끝나는 시간이 주어져 있고, 각 회의가 겹치지 않게 하면서
회의실을 사용할 수 있는 회의의 최대 개수를 찾아보자. 단, 회의는 한번 시작하면 중간에
중단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다.
회의의 시작시간과 끝나는 시간이 같을 수도 있다. 이 경우에는 시작하자마자 끝나는 것으로
생각하면 된다.
첫째 줄에 회의의 수 N(1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N+1 줄까지 각 회의의 정보가
주어지는데 이것은 공백을 사이에 두고 회의의 시작시간과 끝나는 시간이 주어진다. 시작 시간과
끝나는 시간은 2^31-1보다 작거나 같은 자연수 또는 0이다

comment : 이중포문을 사용하지 않는 방법을 생각해내는게 정말 어려운 것 같다.
'''
import sys
N = int(sys.stdin.readline())
array = []
for i in range(N):
    array.append(tuple(map(int, sys.stdin.readline().split())))

array = sorted(array, key=lambda a: a[0])   #시작시간과 끝시간이 같을 경우(ex(5,5))를 위해
array = sorted(array, key=lambda a: a[1])
last = 0
count = 0
for i, j in array:
    if i >= last:
        count += 1
        last = j
print(count)

##시간초과 코드
# array.sort()
# count = 1
# idx = 0     #다음 회의를 발견하면 그 회의부터 for문 돌리기 위한 변수
#
# for i in range(1, N):
#     for j in range(idx, i):
#         if array[i][0] >= array[j][1]:
#             count += 1
#             idx = i
#             break