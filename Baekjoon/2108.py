'''
'통계학'
문제 :   산술평균 : N개의 수들의 합을 N으로 나눈 값
        중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
        최빈값 : N개의 수들 중 가장 많이 나타나는 값
        범위 : N개의 수들 중 최댓값과 최솟값의 차이
        N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.
        N은 홀수라고 가정한다.

comment : 처음에는 이중포문을 사용하는 바람에 시간초과가 떴다.
 이후 collections모듈의 Counter함수가 데이터의 개수가 많은 순으로 정렬된 배열을 리턴하는
  most_common이라는 메서드를 제공하고 있다는 것을 알았고, 이것을 이용해 최빈값을 구했다.
'''
import sys
from collections import Counter

N = int(sys.stdin.readline())
array = []
for i in range(N):
    array.append(int(sys.stdin.readline()))

array.sort()
print(round(sum(array)/N))
print(array[N//2])

##시간초과가 뜬 for문
# max = 0
# idx1 = -1
# idx2 = -1
# for i in range(N):
#     count = 1
#     for j in range(i+1, N):
#         if array[i] == array[j]:
#             count += 1
#     if count > max:
#         idx1 = i
#         idx2 = i
#         max = count
#     elif count == max:
#         if idx1 == idx2:
#             if array[idx1] > array[i]:
#                 idx1 = i
#             else:
#                 idx2 = i
#         else:
#             if array[idx1] > array[i]:
#                 idx1 = i
#             elif array[idx2] > array[i]:
#                 idx2 = i

most = Counter(array).most_common()
if len(most) > 1:
    if most[0][1] == most[1][1]:
        print(most[1][0])
    else:
        print(most[0][0])
else:
    print(most[0][0])


print(array[N-1]-array[0])


