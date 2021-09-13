'''
'소트인사이드'
문제 : 수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자.
첫째 줄에 정렬하고자하는 수 N이 주어진다. N은 1,000,000,000보다 작거나 같은 자연수이다.

comment : 파이썬에 내장되어있는 함수를 사용할 수 있어서 비교적 쉬운 문제였다.
'''

N = input()
array = []
for i in range(len(N)):
    array.append(int(N[i]))

array.sort()
array.reverse()

for i in array:
    print(i, end='')