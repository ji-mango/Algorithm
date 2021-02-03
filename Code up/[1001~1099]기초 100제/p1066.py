'''
세 정수 a, b, c가 입력되었을 때, 짝(even)/홀(odd)을 출력해보자.
'''
a=input().split()
b=map(int,a)
for i in b:
    if(i%2==0):
        print("even")
    else:
        print("odd")