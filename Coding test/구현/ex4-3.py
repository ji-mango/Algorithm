'''
'왕실의 나이트'
문제 : 체스판에서 말은 다음과 같은 두가지 경우로 이동할 수 있다.
1. 수평으로 두 칸 이동 후 수직으로 한 칸 이동
2. 수직으로 두 칸 이동 후 수평으로 한 칸 이동
이처럼 8*8 좌표 평면상에서 나이트의 위치가 주어졌을 때 나이트가 이동할 수 있는 경우의 수를 출력하는 프로그램을
작성하시오. 이때 체스판의 행 위치는 1부터 8, 열 위치는 a부터 h로 표현한다.

comment : 이동할 수 있는 방향을 정의하는 것이 관건인 문제였던 것 같다.
'''
location = input()
array = ['a','b','c','d','e','f','g','h']
for i in range(8):
    if array[i] == location[0]:
        x = i+1
y = int(location[1])

count = 0

move = [(-2, -1), (-1, -2), (1, -2), (2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1)]
moveLocation = []
for i in range(8):
    moveLocation.append((x+(move[i][0]), y+(move[i][1])))

for i in range(8):
    if moveLocation[i][0]>=1 and moveLocation[i][0] <= 8 and moveLocation[i][1]>=1 and moveLocation[i][1]<=8:
        count += 1
print(count)