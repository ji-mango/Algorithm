'''
'동전 1'

comment : 1부터 k까지의 dp테이블로 잡아야 한다는 것은 알겠는데, 점화식을 세우기가 어려워서 답을 참고했다. 다음에 다시 풀어야지
'''
n, k = map(int, input().split())
value = []
for i in range(n):
    data = int(input())
    if k >= data:
        value.append(data)
d = [0] * (k+1)
d[0] = 1

for i in value:
    for j in range(i, k+1):
        d[j] = d[j] + d[j-i]

print(d[k])
