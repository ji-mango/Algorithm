'''
'멀티탭 스케줄링'
문제 : 기숙사에서 살고 있는 준규는 한 개의 멀티탭을 이용하고 있다. 준규는 키보드, 헤어드라이기, 핸드폰 충전기, 
디지털 카메라 충전기 등 여러 개의 전기용품을 사용하면서 어쩔 수 없이 각종 전기용품의 플러그를 뺐다 꽂았다 하는 불편함을 겪고 있다. 
그래서 준규는 자신의 생활 패턴을 분석하여, 자기가 사용하고 있는 전기용품의 사용순서를 알아내었고, 
이를 기반으로 플러그를 빼는 횟수를 최소화하는 방법을 고안하여 보다 쾌적한 생활환경을 만들려고 한다.
예를 들어 3 구(구멍이 세 개 달린) 멀티탭을 쓸 때, 전기용품의 사용 순서가 아래와 같이 주어진다면, 

키보드
헤어드라이기
핸드폰 충전기
디지털 카메라 충전기
키보드
헤어드라이기

키보드, 헤어드라이기, 핸드폰 충전기의 플러그를 순서대로 멀티탭에 꽂은 다음 디지털 카메라 충전기 플러그를 꽂기 전에 
핸드폰충전기 플러그를 빼는 것이 최적일 것이므로 플러그는 한 번만 빼면 된다. 

입력 : 첫 줄에는 멀티탭 구멍의 개수 N (1 ≤ N ≤ 100)과 전기 용품의 총 사용횟수 K (1 ≤ K ≤ 100)가 정수로 주어진다. 
두 번째 줄에는 전기용품의 이름이 K 이하의 자연수로 사용 순서대로 주어진다. 각 줄의 모든 정수 사이는 공백문자로 구분되어 있다. 

출력 : 하나씩 플러그를 빼는 최소의 횟수를 출력하시오. 

풀이 : 1. 처음 for문을 통해 멀티탭 구멍을 모두 채워준다.
      2. 채운 후 다음 사용하는 전기용품부터 마지막 전기용품까지 모두 살펴보며 전기용품이 멀티탭에 존재할 경우 indexList에 넣어준다.
      3-1. for문을 n번 돌며 indexList에 없는 구멍일 경우(후에 쓰지 않을 전기용품인 경우) 현재 사용하는 전기용품으로 교체한다.
      3-2. j가 n-1까지 돌았는데 indexList에 모두 있다면 indexList에서 가장 마지막에 넣은 것의 전기용품과 현재 전기용품을 교체한다.

comment : 처음에는 n개씩 나눠서 생각했는데, 맨 뒤에 나오는 것까지 고려해줘야 되는 것을 반례를 통해 알았다. 반례를 스스로 찾는 연습이 필요할 것 같다.
'''
n, k = map(int, input().split())
array = list(map(int, input().split()))

flug = [0 for i in range(n)]
idx = 0
for i in range(k):              # 구멍 채우기
    if 0 not in flug:
        break
    if array[i] in flug:
        continue
    else:
        flug[idx] = array[i]
        idx += 1

cnt = 0
for i in range(idx, k):
    if array[i] in flug:
        continue
    else:
        indexList = []
        for j in range(i, k):
            for x in range(n):
                if array[j] == flug[x]:
                    if x not in indexList:
                        indexList.append(x)

        for j in range(n):
            if j not in indexList:
                flug[j] = array[i]
                cnt += 1
                break
            elif j in indexList and j == n-1:
                flug[indexList[-1]] = array[i]
                cnt += 1
                break

print(cnt)