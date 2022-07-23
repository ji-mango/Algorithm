'''
'동전 2'

comment : 동전 1 문제와 비슷하기 때문에 동전 1때의 풀이를 생각하며 풀었더니 비교적 쉽게 풀 수 있었다.
'''
INF = int(1e9)

n, k = map(int, input().split())
coin = []
d = [INF for i in range(k+1)]
d[0] = 0

for i in range(n):
    temp = int(input())
    if temp <= k:
        coin.append(temp)

for i in coin:
    for j in range(i, k+1):
        d[j] = min(d[j], d[j-i] + 1)     # 합이 j인 동전의 개수는 j-i 동전 개수 + 1과 같기 때문에 d[j]와 d[j-i] 중 더 작은 값을 고르면 된다.

if d[k] == INF:
    print(-1)
else:
    print(d[k])
