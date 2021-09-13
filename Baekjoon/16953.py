'''
'A->B'
문제 : 정수 A를 B로 바꾸려고 한다. 가능한 연산은 다음과 같은 두가지이다.
- 2를 곱한다.
- 1을 수의 가장 오른쪽에 추가한다.
A를 B로 바꾸는데 필요한 연산의 최솟값을 구해보자.

comment : 처음에 끝자리가 1이 아닐 경우를 생각하지 못해서 틀렸다. 매번 풀때마다 드는 생각인데
그리디 문제는 응용문제 같은 느낌이 들어서 어려운 것 같다.
'''
a, b = map(int,(input().split()))
count = 0

while True:
    if b < a:       #A를 B로 바꿀 수 없는 경우
        count = 0
        break
    elif b == a:
        break
    if b % 2 != 0:
        temp = str(b)
        idx = len(temp)-1
        if temp[idx] != '1':    #2로 나눠지지 않는데 끝자리가 1이 아닐 경우 A->B 바꾸는 것이 불가능
            count = 0
            break
        b = int(temp[:idx])
        count += 1
    elif b % 2 == 0:
        b = b // 2
        count += 1
if count == 0:
    print(-1)
else:
    print(count+1)
