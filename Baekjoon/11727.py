'''
'2×n 타일링 2'
'''
n = int(input())
d = [0 for i in range(n+1)]
d[0] = 1
d[1] = 1

for i in range(2, n+1):
    d[i] = d[i-2] * 2 + d[i-1] * 1

print(d[n] % 10007)
