'''
큰 수의 법칙 - 그리디
배운 점 : 주어지는 숫자가 커짐에 따라 시간초과가 뜰 수 있으므로
         for문을 사용하지 않고 코드를 작성할 수 있는 방법이 있는지 생각해봐야 한다
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