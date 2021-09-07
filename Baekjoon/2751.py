'''
'수 정렬하기 2'
문제 : N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

comment : 버블정렬은 너무 오래걸리는 알고리즘이라 에러가 떴다. 계수 정렬을 사용해봤지만
이것도 시간초과가 떠서 합병정렬을 사용했다.(python은 너무 느려서 pypy3으로 제출했다.)
'''
## 내장 함수(sort) - pypy3으로 해야 시간초과 x
# N=int(input())
# list=[]
#
# for _ in range(N):
#     x = int(input())
#     list.append(x)
#
# for i in sorted(list):
#     print(i)

## 계수 정렬 - 시간 초과
# N = int(input())
# array = []
# for i in range(N):
#     array.append(int(input()))
#
# count = [0 for i in range(1000000)]
# for i in range(N):
#     count[array[i]-1] += 1
#
# for i in range(len(count)):
#     for j in range(count[i]):
#         print(i+1)

## 합병 정렬 - pypy3으로 해야 시간초과 x
def merge_sort(list):
    if len(list) <= 1:
        return list
    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]
    left = merge_sort(left)
    right = merge_sort(right)

    i, j, k = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            list[k] = left[i]
            i += 1
        else:
            list[k] = right[j]
            j += 1
        k += 1
    if i == len(left):
        while j < len(right):
            list[k] = right[j]
            j += 1
            k += 1
    elif j == len(right):
        while i < len(left):
            list[k] = left[i]
            i += 1
            k += 1
    return list

N = int(input())
list = []
for i in range(N):
    list.append(int(input()))

list = merge_sort(list)
for i in list:
    print(i)
