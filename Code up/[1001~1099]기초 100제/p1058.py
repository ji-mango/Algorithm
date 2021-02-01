'''
두 개의 참(1) 또는 거짓(0)이 입력될 때,
모두 거짓일 때에만 참이 계산되는 프로그램을 작성해보자.
'''
a,b=input().split()
a=int(a); a=bool(a)
b=int(b); b=bool(b)
if(not a and not b):
    print(1)
else:
    print(0)