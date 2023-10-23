import tkinter as tk
import random
import sys

# 游戏设置
board_size = 10
num_mines = 10

# 初始化扫雷板
def initialize_board(size, mines):
    board = [[' ' for _ in range(size)] for _ in range(size)]
    for _ in range(mines):
        row, col = random.randint(0, size - 1), random.randint(0, size - 1)
        while board[row][col] == 'X':
            row, col = random.randint(0, size - 1), random.randint(0, size - 1)
        board[row][col] = 'X'
    return board

# 创建主窗口
window = tk.Tk()
window.title("扫雷游戏")

# 初始化扫雷板
board = initialize_board(board_size, num_mines)

# 创建按钮网格
buttons = [[None for _ in range(board_size)] for _ in range(board_size)]

# 处理按钮点击事件
def on_button_click(row, col):
    if board[row][col] == 'X':
        buttons[row][col]["text"] = "X"
        print("游戏结束！你踩到了地雷。")
        sys.exit(0)  # 在踩到地雷后退出程序
    else:
        mines = count_adjacent_mines(row, col)
        buttons[row][col]["text"] = str(mines)

# 处理右键点击事件（标记/取消标记地雷）
def on_right_click(event, row, col):
    if buttons[row][col]["text"] == " ":
        buttons[row][col]["text"] = "M"
    elif buttons[row][col]["text"] == "M":
        buttons[row][col]["text"] = " "

# 统计周围的地雷数量
def count_adjacent_mines(row, col):
    count = 0
    for r in range(row - 1, row + 2):
        for c in range(col - 1, col + 2):
            if 0 <= r < board_size and 0 <= c < board_size and board[r][c] == 'X':
                count += 1
    return count

# 创建按钮并添加到窗口
for row in range(board_size):
    for col in range(board_size):
        buttons[row][col] = tk.Button(window, text=" ", width=3, height=3, command=lambda r=row, c=col: on_button_click(r, c))
        buttons[row][col].bind("<Button-3>", lambda event, r=row, c=col: on_right_click(event, r, c))  # 处理右键点击事件
        buttons[row][col].grid(row=row, column=col)

window.mainloop()
