import sys
input = sys.stdin.readline

N,M,Y,X,K = map(int,input().split())
board = []

for _ in range(N):
    board.append(list(map(int,input().split())))

simulation = list(map(int,input().split()))

# 1 = 동, 2 = 서, 3 = 북, 4 = 남 
dx = [0, 1, -1, 0, 0]
dy = [0, 0, 0, -1, 1]

class Dice():

    def __init__(self):
        self.upside = 0 
        self.downside = 0
        self.side = [0,0,0,0,0] # 무시, 동, 서, 남, 북 순.

    def go_west(self, board_num): # 왼쪽으로 구르기 
        tmpUpside = self.upside
        tmpDownside = self.downside

        self.downside = self.side[2]
        self.upside = self.side[1]

        self.side[2] = tmpUpside
        self.side[1] = tmpDownside

        if board_num == 0:
            return self.downside
        else :
            self.downside = board_num
            return 0

    def go_east(self, board_num):
        tmpUpside = self.upside
        tmpDownside = self.downside

        self.downside = self.side[1]
        self.upside = self.side[2]

        self.side[2] = tmpDownside
        self.side[1] = tmpUpside

        if board_num == 0:
            return self.downside
        else :
            self.downside = board_num
            return 0

    def go_north(self, board_num):
        tmpUpside = self.upside
        tmpDownside = self.downside

        self.downside = self.side[4]
        self.upside = self.side[3]

        self.side[3] = tmpDownside
        self.side[4] = tmpUpside

        if board_num == 0:
            return self.downside
        else :
            self.downside = board_num
            return 0

    def go_south(self, board_num):
        tmpUpside = self.upside
        tmpDownside = self.downside

        self.downside = self.side[3]
        self.upside = self.side[4]

        self.side[3] = tmpUpside
        self.side[4] = tmpDownside

        if board_num == 0:
            return self.downside
        else :
            self.downside = board_num
            return 0

dice = Dice()

for sim in simulation:
    # 범위검사
    if (X + dx[sim] >= M) or (X + dx[sim] < 0) or (Y + dy[sim] >= N) or (Y + dy[sim] < 0):
        continue

    # 이동
    X = X + dx[sim]
    Y = Y + dy[sim]

    # 주사위 굴리기
    if sim == 1:
        board[Y][X] = dice.go_east(board[Y][X])
    elif sim == 2:
        board[Y][X] = dice.go_west(board[Y][X])
    elif sim == 3:
        board[Y][X] = dice.go_north(board[Y][X])
    elif sim == 4:
        board[Y][X] = dice.go_south(board[Y][X])

    print(dice.upside)
