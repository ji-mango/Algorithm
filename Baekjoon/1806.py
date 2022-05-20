'''
'부분합'
문제 : 10,000 이하의 자연수로 이루어진 길이 N짜리 수열이 주어진다. 이 수열에서 연속된 수들의 부분합 중에 그 합이 S 이상이 되는 것 중, 
가장 짧은 것의 길이를 구하는 프로그램을 작성하시오.

입력 : 첫째 줄에 N (10 ≤ N < 100,000)과 S (0 < S ≤ 100,000,000)가 주어진다. 둘째 줄에는 수열이 주어진다. 
수열의 각 원소는 공백으로 구분되어져 있으며, 10,000이하의 자연수이다.

출력 : 첫째 줄에 구하고자 하는 최소의 길이를 출력한다. 만일 그러한 합을 만드는 것이 불가능하다면 0을 출력하면 된다.

comment : 투포인터 알고리즘을 처음 사용했다. 투포인터는 리스트에 순차적으로 접근해야 할 때 두 개의 점의 위치를 기록하며 처리하는 알고리즘인데, 생각보다 쉬웠다.
          시간복잡도가 for문을 2번 도는 것보다 적게 들어서 코드를 짤 때 뭔가 기분이 좋았다.
'''
n, s = map(int, input().split())
array = list(map(int, input().split()))

start, end = 0, 0
sum = array[0]
min = 9999999                       # 합이 s 이상 되는 것 중 가장 짧은 것의 길이
while end < n:
    if sum < s:
        end += 1
        # end는 끝에 있고 start는 증가시켜주어야 할 때 end의 index 범위가 초과됐다는 에러를 발생시키지 않기 위해 조건문을 걸어준다.
        if end < n:                
            sum += array[end]
    else:
        length = end - start + 1
        if length < min:
            min = length
        sum -= array[start]
        start += 1

if min == 9999999:
    print(0)
else:
    print(min)