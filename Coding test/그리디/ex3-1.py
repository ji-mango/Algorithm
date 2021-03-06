'''
'거스름돈'
문제 : 카운터에 거스름돈으로 사용할 500원, 100원, 50원, 10원짜리 동전이 무한히 ㅈ
      존재한다고 가정한다. 손님에게 거슬러 줘야 할 돈이 N원일 때 거슬러 줘야 할
      동전의 최소 개수를 구하라. 단, 거슬러 줘야 할 돈 N은 항상 10의 배수이다.

배운 점 : 가지고 있는 동전 중에 큰 단위가 항상 작은 단위의 배수이기 때문에
         그리디 알고리즘 방법을 사용할 수 있다.
'''
m = 1260
a = [500, 100, 50, 10]
cnt = 0
for i in a:
    cnt += m // i
    m = m % i

print("%d개"%cnt)