'''
'시각'
문제 : 정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서
      3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하시오.

배운 점 : 문자열에 특정 문자가 들어있는지를 알고싶을 때 '문자' in '문자열'을 사용한다
'''
n=int(input())

cnt=0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                cnt+=1
print(cnt)