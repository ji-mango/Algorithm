'''
'팩토리얼'
문제 : 0보다 크거나 같은 정수 N이 주어진다. 이때 N!을 출력하는 프로그램을 작성하시오
(재귀함수 이용)

comment : if N<=1이 아닌 if N==1이라고 하면 runtime 에러가 뜬다.
'''
def fac(N):
    if N<=1:
        return 1
    else:
        return N*fac(N-1)

n=int(input())
print(fac(n))
