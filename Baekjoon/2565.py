'''
'전깃줄'
문제 : 두 전봇대 A와 B 사이에 하나 둘씩 전깃줄을 추가하다 보니 전깃줄이 서로 교차하는 경우가 발생하였다. 합선의 위험이 있어 이들 중 몇 개의 전깃줄을 없애 전깃줄이 교차하지 않도록 
만들려고 한다. 전깃줄이 전봇대에 연결되는 위치는 전봇대 위에서부터 차례대로 번호가 매겨진다. 전깃줄의 개수와 전깃줄들이 두 전봇대에 연결되는 위치의 번호가 주어질 때, 
남아있는 모든 전깃줄이 서로 교차하지 않게 하기 위해 없애야 하는 전깃줄의 최소 개수를 구하는 프로그램을 작성하시오.

입력 : 첫째 줄에는 두 전봇대 사이의 전깃줄의 개수가 주어진다. 전깃줄의 개수는 100 이하의 자연수이다. 둘째 줄부터 한 줄에 하나씩 전깃줄이 A전봇대와 연결되는 위치의 번호와 
B전봇대와 연결되는 위치의 번호가 차례로 주어진다. 위치의 번호는 500 이하의 자연수이고, 같은 위치에 두 개 이상의 전깃줄이 연결될 수 없다.

출력 : 첫째 줄에 남아있는 모든 전깃줄이 서로 교차하지 않게 하기 위해 없애야 하는 전깃줄의 최소 개수를 출력한다.

comment : 등비수열 문제와 비슷하게 A전봇대의 수를 기준으로 정렬하고 B전봇대에서 가장 긴 증가하는 수열의 길이를 찾았다. 그리고 그 길이를 전깃줄 길이에서 빼주었다.
'''
a = int(input())
array = []
for i in range(a):
    array.append(list(map(int, input().split())))

array.sort()

d = [0 for i in range(a)]
d[0] = 1
for i in range(a):
    maximum = 0
    for j in range(i):
        if array[i][1] > array[j][1]:
            if d[j] > maximum:
                maximum = d[j]
    d[i] = maximum + 1

print(a-max(d))
