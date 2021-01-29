'''
두 개의 참(1) 또는 거짓(0)이 입력될 때,
모두 참일 때에만 참을 출력하는 프로그램을 작성해보자.
'''
a,b=input().split()
a=int(a); a=bool(a)
b=int(b); b=bool(b)
if(a and b):
    print(1)
else:
    print(0)