from copy import deepcopy

def board(data):
    show = deepcopy(data)
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == 0:
                show[i][j] = " "
            elif data[i][j] == 1:
                show[i][j] = "x"
            elif data[i][j] == 2:
                show[i][j] = 'o'
            else:
                raise Exception("Error!")

    print('   Player 1: x                      Player 2: o')
    print(' ')
    print(f"|-----|-----|-----|-----|-----|-----|-----|-----|")
    print(f"|  {show[0][0]}  |  {show[0][1]}  |  {show[0][2]}  |  {show[0][3]}  |  {show[0][4]}  |  {show[0][5]}  |  {show[0][6]}  |  {show[0][7]}  |  0  ")
    print(f"|-----|-----|-----|-----|-----|-----|-----|-----|")
    print(f"|  {show[1][0]}  |  {show[1][1]}  |  {show[1][2]}  |  {show[1][3]}  |  {show[1][4]}  |  {show[1][5]}  |  {show[1][6]}  |  {show[1][7]}  |  1  ")
    print(f"|-----|-----|-----|-----|-----|-----|-----|-----|")
    print(f"|  {show[2][0]}  |  {show[2][1]}  |  {show[2][2]}  |  {show[2][3]}  |  {show[2][4]}  |  {show[2][5]}  |  {show[2][6]}  |  {show[2][7]}  |  2  ")
    print(f"|-----|-----|-----|-----|-----|-----|-----|-----|")
    print(f"|  {show[3][0]}  |  {show[3][1]}  |  {show[3][2]}  |  {show[3][3]}  |  {show[3][4]}  |  {show[3][5]}  |  {show[3][6]}  |  {show[3][7]}  |  3  ")
    print(f"|-----|-----|-----|-----|-----|-----|-----|-----|")
    print(f"|  {show[4][0]}  |  {show[4][1]}  |  {show[4][2]}  |  {show[4][3]}  |  {show[4][4]}  |  {show[4][5]}  |  {show[4][6]}  |  {show[4][7]}  |  4  ")
    print(f"|-----|-----|-----|-----|-----|-----|-----|-----|")
    print(f"|  {show[5][0]}  |  {show[5][1]}  |  {show[5][2]}  |  {show[5][3]}  |  {show[5][4]}  |  {show[5][5]}  |  {show[5][6]}  |  {show[5][7]}  |  5  ")
    print(f"|-----|-----|-----|-----|-----|-----|-----|-----|")
    print(f"|  {show[6][0]}  |  {show[6][1]}  |  {show[6][2]}  |  {show[6][3]}  |  {show[6][4]}  |  {show[6][5]}  |  {show[6][6]}  |  {show[6][7]}  |  6  ")
    print(f"|-----|-----|-----|-----|-----|-----|-----|-----|")
    print(f"|  {show[7][0]}  |  {show[7][1]}  |  {show[7][2]}  |  {show[7][3]}  |  {show[7][4]}  |  {show[7][5]}  |  {show[7][6]}  |  {show[7][7]}  |  7  ")
    print(f"|-----|-----|-----|-----|-----|-----|-----|-----|")
    print(f"   0     1     2     3     4     5     6     7   ")

def get_user_move(player):
    print("___________________________________________________")
    print(f"Lượt của Player {player}:")
    current_row = int(input("Nhập hàng hiện tại của quân cờ: "))
    current_col = int(input("Nhập cột hiện tại của quân cờ: "))
    target_row = int(input("Nhập hàng mà bạn muốn di chuyển đến: "))
    target_col = int(input("Nhập cột mà bạn muốn di chuyển đến: "))
    return current_row, current_col, target_row, target_col

def move_piece(data, player, current_row, current_col, target_row, target_col):
    global p1_count, p2_count
    # Kiểm tra nếu vị trí hiện tại có quân cờ của người chơi
    if data[current_row][current_col] == player:
        # Gọi hàm is_valid_move() với tất cả các đối số cần thiết
        if is_valid_move(data, player, current_row, current_col, target_row, target_col):
            # Di chuyển quân cờ
            data[target_row][target_col] = data[current_row][current_col]
            data[current_row][current_col] = 0  
            print("Di chuyển thành công!")
        else:
            print("Bước di chuyển không hợp lệ!")
        
        if player == 1:
            p1_count += 1
        else:
            p2_count += 1
    else:
        print("Không có quân cờ của bạn ở vị trí này!")

def is_valid_move(data, player, current_row, current_col, target_row, target_col):
    # Kiểm tra xem vị trí đích có trống không
    if data[target_row][target_col] == 0:
        return True
    else:
        print("Vị trí đích đã có quân cờ!")
        return False
    # else: 
    #     return True

    # Kiểm tra xem nước đi có nằm trong bảng không
    if (0 <= target_row < 8) or (0 <= target_col < 8):
        return True
    else:
        print("Nước đi nằm ngoài bảng!")
        return False
    # else: 
    #     return True

    # Kiểm tra xem nước đi có phù hợp không
    if player == 1:  # Nếu là người chơi 1 (quân 'x')
        return (target_row == current_row - 1) and (abs(target_col - current_col) == 1)
    elif player == 2:  # Nếu là người chơi 2 (quân 'o')
        return (target_row == current_row + 1) and (abs(target_col - current_col) == 1)
    else: 
        return True


data = [
    [0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [2, 0, 2, 0, 2, 0, 2, 0],
    [0, 2, 0, 2, 0, 2, 0, 2],
    [2, 0, 2, 0, 2, 0, 2, 0],
]

p1_count = 0
p2_count = 0
player = 1
while True:
    board(data)
    print("  ")
    print(f"Số lượt di chuyển của Người chơi 1: {p1_count}")
    print(f"Số lượt di chuyển của Người chơi 2: {p2_count}")
    current_row, current_col, target_row, target_col = get_user_move(player)
    move_piece(data, player, current_row, current_col, target_row, target_col)
    player = 2 if player == 1 else 1
