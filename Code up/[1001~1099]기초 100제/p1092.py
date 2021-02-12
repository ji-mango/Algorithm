'''
같은 날 동시에 가입한 인원 3명이 규칙적으로 방문하는,
방문 주기가 공백을 두고 입력된다. (단, 입력값은 100이하의 자연수이다.)

3명이 다시 모두 함께 방문해 문제를 풀어보는 날(동시 가입/등업 후 며칠 후?)을 출력한다.
'''
a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
i=0
while True:
    i+=1
    if i%a==0 and i%b==0 and i%c==0:
        print(i)
        break
