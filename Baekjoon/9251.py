'''
'LCS'
'''
A = input()
B = input()

lenA = len(A)
lenB = len(B)

d2 = [0] * lenB

for i in range(lenA):
    previous = 0                          # 이전 위치까지의 최댓값 저장
    for j in range(lenB):
        if previous < d2[j]:              # 현재 문자의 누적 값이 최댓값(previous)보다 큰 경우 해당 값으로 최댓값을 교체
                previous = d2[j]
        elif A[i] == B[j]:                # 처음에는 elif가 아닌 if로 해서 틀렸다. if로 할 경우 지나친 문자에도 중복으로 +1이 되는 경우가 있어
                                          # 반례인 BBAAAA, BABAAB의 경우 6이 나온다.
                d2[j] = previous + 1

print(max(d2))