'''
N명의 학생 정보가 있다. 학생 정보는 학생의 이름과 학생의 성적으로 구분된다. 각 학생의 이름과
성적 정보가 주어졌을 때 성적이 낮은 순서대로 학생의 이름을 출력하는 프로그램을 작성하시오.
'''
N = int(input())
dic = {}
for i in range(N):
    name, score = input().split()
    dic[name] = score

dic = sorted(dic.items(), key = lambda item: item[1])
for i in range(N):
    print(dic[i][0], end = ' ')

