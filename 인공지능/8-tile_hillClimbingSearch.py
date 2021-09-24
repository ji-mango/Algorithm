# 상태를 나타내는 클래스, f(n) 값을 저장한다.
class State:
    def __init__(self, board, goal, moves=0):
        self.board = board
        self.moves = moves
        self.goal = goal

    # i1과 i2를 교환하여서 새로운 상태를 반환한다.
    def get_new_board(self, i1, i2):
        new_board = self.board[:]
        new_board[i1], new_board[i2] = new_board[i2], new_board[i1]
        return State(new_board, self.goal)

    # 자식 노드를 확장하여서 리스트에 저장하여서 반환한다.
    def expand(self):
        result = []
        i = self.board.index(0)  # 숫자 0(빈칸)의 위치를 찾는다.
        if not i in [0, 1, 2]:  # UP 연산자
            result.append(self.get_new_board(i, i - 3))
        if not i in [0, 3, 6]:  # LEFT 연산자
            result.append(self.get_new_board(i, i - 1))
        if not i in [2, 5, 8]:  # DOWN 연산자
            result.append(self.get_new_board(i, i + 1))
        if not i in [6, 7, 8]:  # RIGHT 연산자
            result.append(self.get_new_board(i, i + 3))
        return result

    # 휴리스틱 함수 값인 h(n)을 계산하여 반환한다.
    # 현재 제 위치에 있지 않은 타일의 개수를 리스트 함축으로 계산한다.
    def h(self):
        return sum([1 if self.board[i] != self.goal[i] else 0 for i in range(8)])

    # 상태와 상태를 비교하기 위하여 less than 연산자를 정의한다.
    def __lt__(self, other):
        return self.f() < other.f()

    # 객체를 출력할 때 사용한다.
    def __str__(self):
        return "---------- h(n)=" + str(self.h()) + "\n" + \
               str(self.board[:3]) + "\n" + \
               str(self.board[3:6]) + "\n" + \
               str(self.board[6:]) + "\n" + \
               "----------"


# 초기 상태
puzzle = [2, 4, 3,
          1, 0, 6,
          7, 5, 8]
# 목표 상태
goal = [1, 2, 3,
        4, 5, 6,
        7, 8, 0]

result = State(puzzle, goal)
closed_queue = []
temp_break = True
h = 9999

while True:
    min = 999
    if temp_break == False:
        print("탐색 실패")
        break
    if result.board == goal:
        print("탐색 성공")
        break
    print(result)
    h = result.h()
    for state in result.expand():
        if state not in closed_queue:
            if state.h() < min:
                min = state.h()
                result = state
        closed_queue.append(result)
    if result.h() > h:
        temp_break = False
