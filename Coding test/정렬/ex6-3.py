'''
'두 배열의 원소 교체'

문제 : 동빈이는 두 개의 배열 A와 B를 가지고 있다. 두 배열은 N개의 원소로 구성되어 있으며, 배열의
원소는 모두 자연수이다. 동빈이는 최대 K번의 바꿔치기 연산을 수행할 수 있는데, 바꿔치기 연산이란
배열 A에 있는 원소 하나와 배열 B 원소 하나를 골라 서로 바꾸는 것이다. 동빈이의 최종 목표는 배열 A의 모든 원소의 합이
최대가 되도록 하는 것이다.
N, K, 배열 A, 배열 B가 주어졌을 때, 최대 K번의 바꿔치기 연산을 수행해 만들 수 있는 배열 A의 모든 원소의 합의
최댓값을 출력하는 프로그램을 작성하시오.
'''
N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

for i in range(K):
    if A[i] < B[i]:
        A[i], B[i] = B[i], A[i]
    else:
        break

print(sum(A))