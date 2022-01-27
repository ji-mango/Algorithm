'''
'부품 찾기'

문제 : 동빈이네 전자 매장에는 부품이 N개 있다. 각 부품은 정수 형태의 고유한 번호가 있다. 어느 날 손님이
M개 종류의 부품을 대량으로 구매하겠다며 당일 날 견적서를 요청했다. 동빈이는 때를 놓치지 않고 손님이 문의한
부품 M개 종류를 모두 확인해서 견적서를 작성해야 한다. 이때 가게 안에 부품이 모두 있는지 확인하는 프로그램을
작성해보자.
'''
import sys

N = int(input())
arrayN = list(map(int, sys.stdin.readline().split()))
M = int(input())
arrayM = list(map(int, sys.stdin.readline().split()))

arrayN.sort()

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return "yes"
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return "no"

for i in arrayM:
    num = i
    print(binary_search(arrayN, num, 0, N-1), end = ' ')



