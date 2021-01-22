'''
년월일(yyyy.mm.dd)를 입력받아,
일월년(dd-mm-yyyy)로 출력해보자.
'''
a,b,c=input().split(".")
a=int(a)
b=int(b)
c=int(c)
print("%02d-%02d-%04d" %(c,b,a))