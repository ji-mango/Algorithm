'''
'큰 수의 법칙'
문제 : 큰 수의 법칙은 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번
      더하여 가장 큰 수를 만드는 법칙이다. 단, 배열의 특정한 인덱스에 해당하는
      수가 연속해서 K번 초과하여 더해질 수 없다.
      배열의 크기 N, 숫자가 더해지는 횟수 M, 그리고 K가 주어질 때 큰 수의 법칙에
      따른 결과를 출력하시오

배운 점 : 주어지는 숫자가 커짐에 따라 시간초과가 뜰 수 있으므로
         for문을 사용하지 않고 코드를 작성할 수 있는 방법이 있는지 고려해야한다.
'''

N, M, K = map(int, input().split())
li = list(map(int, input().split()))

li.sort()
max=li[N-1]
second_max=li[N-2]

big=0
for i in range(1,M+1):
    if i%(K+1)==0:
        big += second_max
    else:
        big += max

print(big)

# 답안 예시
'''
N, M, K = map(int, input().split())
li = list(map(int, input().split()))

li.sort()
max=li[N-1]
second_max=li[N-2]

#가장 큰 수가 더해지는 횟수
count=int(M/(K+1))*K + M%(K+1)
result=0
result += count * max
result += (M-count) * second_max

print(result)
'''