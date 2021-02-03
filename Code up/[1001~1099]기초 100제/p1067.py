'''
정수 1개가 입력되었을 때, 음(minus)/양(plus)과 짝(even)/홀(odd)을 출력해보자.
'''
a=input()
a=int(a)
if(a<0):
    print("minus")
    b=a+(a*2)
    if(b%2==0):
        print("even")
    else:
        print("odd")
else:
    print("plus")
    if(a%2==0):
        print("even")
    else:
        print("odd")