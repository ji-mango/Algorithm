'''
'소수 사이 수열'
문제 : 연속한 소수 p와 p+n이 있을 때, 그 사이에 있는 n-1개의 합성수(소수나 1이 아닌 양의 정수)는 길이가 n인 소수 사이 수열라고 부른다.
양의 정수 k가 주어졌을 때, k를 포함하는 소수 사이 수열의 길이를 구하는 프로그램을 작성하시오. k를 포함하는 소수 사이 수열이 없을 때는 길이가 0이다.
예를 들어, 소수 23과 29의 소수 사이 수열은 {24, 25, 26, 27, 28}이고, 길이는 6이다.

입력 : 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 테스트 케이스는 한 줄로 이루어져 있고, 한 줄에 정수 k가 주어진다. 각각의 정수는 1보다 크고,
100000번째 소수(1299709)와 작거나 같다.

출력 : 각각의 테스트 케이스에 대해서 k가 합성수라면 k를 포함하는 소수 사이 수열의 길이를 출력한다. 그렇지 않으면 0을 출력한다.

comment : 에라스토테네스의 체 알고리즘을 처음 써봤다. 스터디에서 한번 짚고 넘어가기만 해서 잘 감이 안왔었는데, 이렇게 문제로 직접 푸니까
어떤 원리인지 제대로 알게되었다.
'''
import math

T = int(input())
array = []
result = []
for i in range(T):
    array.append(int(input()))

num = 1299709                               # 에라스토테네스의 체 알고리즘 이용
prime = [True for i in range(num+1)]

for i in range(2, int(math.sqrt(num)) + 1): # 2부터 num의 제곱근까지의 수 확인
    if prime[i] == True:                    # i가 소수인 경우(남은 수인 경우)
        j = 2
        while i * j <= num:
            prime[i*j] = False
            j += 1

for i in range(0, T):
    x = array[i]
    if prime[x] is True:
        result.append(0)
    else:
        cnt = 0
        for j in range(x, 0, -1):
            cnt += 1
            if prime[j] == True:
                break
        for j in range(x, num+1):
            cnt += 1
            if prime[j] == True:
                break
        result.append(cnt-2)
for i in range(T):
    print(result[i])