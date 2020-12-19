#2048 has 4 lines
#0 0 0 0
#0 0 0 0
#0 0 0 0
#0 0 0 0
# 0 = left, 1 = up, 2 = right, 3 = down
import random
import datetime

class Board:
    def __init__(self, size):
        self.score = 0
        self.size = size
        self.board = self.createboard()
        self.fill_ran_num(2)

    def createboard(self):
        board = []
        for row in range(self.size):
            board.append([])
            for col in range(self.size):
                board[row].append(0)
        return board

    def dis_board(self):
        for row in range(self.size):
            for col in range(self.size):
                print(f"{self.board[row][col]:<7d}", end="")
            print("")

    def swap_ver(self):
        new_board = []
        for row in range(self.size):
            temp = []
            for col in range(self.size):
                temp.append(self.board[col][row])
            new_board.append(temp)
        self.board = new_board

    def pre_move(self, direction):
        check = 0
        if direction == "left":
            self.swap_zero("left")
            for row in range(self.size):
                for col in range(self.size-1):
                    if self.board[row][col] > 0 and self.board[row][col + 1] == self.board[row][col]:
                        check += 1
                        self.board[row][col] *= 2
                        self.score += self.board[row][col]
                        print(f"{self.board[row][col]} has been add to the score")
                        self.board[row][col + 1] = 0
                        self.swap_zero("left")

        elif direction == "right":
            self.swap_zero("right")
            for row in range(self.size):
                for col in range(1, self.size):
                    if self.board[row][-col] > 0 and self.board[row][-(col + 1)] == self.board[row][-col]:
                        check += 1
                        self.board[row][-col] *= 2
                        self.score += self.board[row][-col]
                        print(f"{self.board[row][-col]} has been add to the score")
                        self.board[row][-(col + 1)] = 0
                        self.swap_zero("right")
        if check == 0:
            return False
        elif check > 0:
            return True
        else:
            print("ERROR CHECK")

    def fill_ran_num(self, amount):
        possible_pos = []
        # Check if there is any space to fill random number
        for row in range(self.size):
            for column in range(self.size):
                if self.board[row][column] == 0:
                    possible_pos.append([row, column])
        if possible_pos == [] or (len(possible_pos) < amount):
            return False
        else:
            possible_am = len(possible_pos) - 1
            for i in range(amount):
                ran_num = random.randint(0, possible_am)
                ran_num2 = random.choice([2, 4])
                select_pos = possible_pos[ran_num]
                self.board[select_pos[0]][select_pos[1]] = ran_num2
                del possible_pos[ran_num]
                possible_am -= 1
            return True

    def swap_zero(self, direction):
        if direction == "left":
            for row in range(self.size):
                if 0 in self.board[row]:
                    for col in range(self.size):
                        if self.board[row][col] == 0:
                            self.board[row].remove(0)
                            self.board[row].append(0)
        elif direction == "right":
            for row in range(self.size):
                if 0 in self.board[row]:
                    temp_list =[]
                    for item in self.board[row]:
                        if item != 0:
                            temp_list.append(item)
                    for item in temp_list:
                        self.board[row].remove(item)
                        self.board[row].append(item)

    def move(self, direction):
        if direction in ["left","right"]:
            check = self.pre_move(direction)
        elif direction == "up":
            self.swap_ver()
            check = self.pre_move("left")
            self.swap_ver()
        elif direction == "down":
            self.swap_ver()
            check = self.pre_move("right")
            self.swap_ver()
        else:
            print("ERROR wrong command at move func")
            check = 0
        return check

    def checkWin(self):
        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col] == 2048:
                    return True
        return False

    def checkPosMove(self):
        copied_board = list(self.board)
        temp = self.score
        self.move("right")
        self.move("left")
        self.move("down")
        self.move("up")
        self.score = temp
        if copied_board == self.board and not self.fill_ran_num(1):
            self.board = copied_board
            return False
        else:
            return True



playboard = Board(4)
playboard.dis_board(playboard.board)
print("Move right")
playboard.move("right")
playboard.dis_board(playboard.board)
print("Move up")
playboard.move("up")
playboard.dis_board(playboard.board)

# set new seed of the current time
# random.seed(datetime.datetime.now())
# print("Initial board")
# play_board = Board(4)
# print(play_board.board)
# if not play_board.checkPosMove():
#     print("GAMEOVER")
#     print(play_board.score)
