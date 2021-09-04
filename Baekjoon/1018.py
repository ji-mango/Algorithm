'''
'체스판 다시 칠하기'
문제 : 지민이는 자신의 저택에서 MN개의 단위 정사각형으로 나누어져 있는 M*N 크기의 보드를
찾았다. 어떤 정사각형은 검은색으로 칠해져 있고, 나머지는 흰색으로 칠해져 있다. 지민이는 이
보드를 잘라서 8*8 크기의 체스판으로 만들려고 한다.

체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다. 구체적으로, 각 칸이 검은색과 흰색 중
하나로 색칠되어 있고, 변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 한다. 따라서
이 정의를 따르면 체스판을 색칠하는 경우는 두 가지뿐이다. 하나는 맨 왼쪽 위 칸이 흰색인 경우,
하나는 검은색인 경우이다.

보드가 체스판처럼 칠해져 있다는 보장이 없어서, 지민이는 8*8 크기의 체스판으로 잘라낸 후에
몇 개의 정사각형을 다시 칠해야겠다고 생각했다. 당연히 8*8 크기는 아무데서나 골라도 된다.
지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.

comment : 처음에는 경우의 수를 맨왼쪽 위의 색이 'B'일 때와 'W'일 때만으로 나눠서 푸는 바람에 틀렸다. 백준 게시판의 반례를
 통해 맨왼쪽 위의 색을 바꿔야하는 경우도 있다는 것을 알았다. 그래서 샘플 두개를 모두 비교해준 후 제일 작은 수를 출력해주는
방식으로 구현했다. 경우의 수를 모두 생각해줘야 하는 것이 어려운 문제였다.
'''
N, M = map(int, input().split())
board = [list(map(str,input())) for row in range(N)]

boardW = [[0 for col in range(8)] for row in range(8)]
boardB = [[0 for col in range(8)] for row in range(8)]

for i in range(8):
    for j in range(8):
        if i % 2 == 0:
            if j % 2 == 0:
                boardW[i][j] = 'W'
                boardB[i][j] = 'B'
            else:
                boardW[i][j] = 'B'
                boardB[i][j] = 'W'
        else:
            if j % 2 == 0:
                boardW[i][j] = 'B'
                boardB[i][j] = 'W'
            else:
                boardW[i][j] = 'W'
                boardB[i][j] = 'B'

#8*8로 나눌수 있는 경우 다 확인 -> 샘플이랑 비교해서 다른거 count -> 제일 적은 count 출력
min = 9999999999

for i in range(N-7):
    for j in range(M-7):
        countW = 0
        countB = 0
        for x in range(i, i+8):
            for y in range(j, j+8):
                if board[x][y] != boardW[x-i][y-j]:
                        countW += 1
                if board[x][y] != boardB[x-i][y-j]:
                        countB += 1
        if countW < countB:
            if countW < min:
                min = countW
        else:
            if countB < min:
                min = countB
print(min)
