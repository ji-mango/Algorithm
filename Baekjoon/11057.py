'''
'오르막 수'
문제 : 오르막 수는 수의 자리가 오름차순을 이루는 수를 말한다. 이때, 인접한 수가 같아도 오름차순으로 친다.
예를 들어, 2234와 3678, 11119는 오르막 수이지만, 2232, 3676, 91111은 오르막 수가 아니다.
수의 길이 N이 주어졌을 때, 오르막 수의 개수를 구하는 프로그램을 작성하시오. 수는 0으로 시작할 수 있다.

입력 : 첫째 줄에 N (1 ≤ N ≤ 1,000)이 주어진다.

출력 : 첫째 줄에 길이가 N인 오르막 수의 개수를 10,007로 나눈 나머지를 출력한다.

'''
# n = int(input())
# d = [[0 for i in range(10)] for i in range(n+1)]
# d[1] = [1 for i in range(10)]
# if n > 1:
#     d[2] = [i for i in range(10, -1, -1)]

#     for i in range(3, n+1):
#         for j in range(10):
#             temp = 0
#             for k in range(j):
#                 temp += d[i-1][k]
#             d[i][j] = sum(d[i-1]) - temp

# print(sum(d[n]) % 10007)

n = int(input())
d = [[0 for i in range(10)] for i in range(n+1)]
d[1] = [1 for i in range(10)]
if n > 1:
    d[2] = [i for i in range(10, -1, -1)]

    for i in range(3, n+1):
        for j in range(10):
            if j == 0:
                d[i][j] = sum(d[i-1])
            else:
                d[i][j] = d[i][j-1] - d[i-1][j-1]

print(sum(d[n]) % 10007)