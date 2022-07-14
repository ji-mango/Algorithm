'''
'극장 좌석'

풀이 : 1. vip 좌석 외의 좌석 간격에 대한 리스트를 구한다.(예시의 경우 vip좌석이 4, 7번이므로 vip좌석이 아닌 좌석의 간격 리스트는 [3, 2, 2] 이다.)
      2. 간격 수에 따른 경우의 수를 dp테이블로 잡는다. 
         길이는 좌석의 간격 리스트에서 가장 큰 값으로 한다.(예시의 경우 3이 가장 큰 값이므로 길이를 3+1(좌석 번호와 인덱스를 맞추기 위해) 으로 한다.)
      3. 자리를 옮기지 않는 경우와 옮기는 경우를 생각해야하기 때문에 점화식은 d[i] = d[i-1] + d[i-2] 이다.
      4. 경우의 수이므로 좌석 값에 해당하는 d[i]값을 반복문을 돌며 곱해준다.
'''
n = int(input())
m = int(input())
seat = [0]
new_seat = []

temp = 0
for i in range(m):
    seat.append(int(input()))
seat.append(n+1)

for i in range(1, len(seat)):
    new_seat.append(seat[i]-seat[i-1]-1)

if max(new_seat) <= 3:
    d = [0 for i in range(4)]  
else:
    d = [0 for i in range(max(new_seat)+1)]

d[1] = 1
d[2] = 2
for i in range(3, len(d)):
    d[i] = d[i-1]+d[i-2]

result = 1
for i in new_seat:
    if i == 0:
        continue
    result = result * d[i]

print(result)