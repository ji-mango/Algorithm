'''
'수 정렬하기'
문제 : N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

comment : 시간복잡도가 O(n^2)인 버블정렬을 이용해 정렬했다.
'''
N = int(input())
array = []
for i in range(N):
    array.append(int(input()))

for i in range(N):
    for j in range(i+1, N):
        if array[i] > array[j]:
            temp = array[i]
            array[i] = array[j]
            array[j] = temp

for i in range(N):
    print(array[i])