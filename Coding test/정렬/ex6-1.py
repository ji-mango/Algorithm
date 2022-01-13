'''
'위에서 아래로'

문제 : 하나의 수열에는 다양한 수가 존재한다. 이러한 수는 크기에 상관없이 나열되어 있다. 이수를 큰 수부터 작은 수의 순서로 정렬해야 한다.
수열을 내림차순으로 정렬하는 프로그램을 만드시오.
'''
N = int(input())
array = []
for i in range(N):
    array.append(int(input()))

array.sort()
array.reverse()
for i in range(N):
    print(array[i], end = ' ')