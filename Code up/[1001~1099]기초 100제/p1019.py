'''
연, 월, 일이 ".(닷)"으로 구분되어 입력된다.
입력받은 연, 월, 일을 yyyy.mm.dd 형식으로 출력한다.
'''
a,b,c=input().split(".")
print("%04d" % int(a), end=".")
print("%02d" % int(b), end=".")
print("%02d" % int(c))
