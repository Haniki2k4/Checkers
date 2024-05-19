# @title Board
from copy import deepcopy
import sys

def board(data):
    show = deepcopy(data)
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == 0:
                show[i][j] = " "
            elif data[i][j] == 1:
                show[i][j] = "x"
            elif data[i][j] == 2:
                show[i][j] = "o"
            elif data[i][j] == 3:
                show[i][j] = "K"
            elif data[i][j] == 4:
                show[i][j] = "Q"
            else:
                raise Exception("Error!")

    print(" Player 1: x | K                 Player 2: o | Q")
    print(" ")
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
    while True:
        print(" ")
        print("___________________________________________________")
        print(f"Lượt của Player {player}:")
        try:
            current_row = int(input("Nhập hàng hiện tại của quân cờ: "))
            if current_row == 100:
                print(f"Player {player} đã đầu hàng! :<<")
                print(f"Player {3 - player} là người chiến thắng!")
                # exit()
                sys.exit()
            current_col = int(input("Nhập cột hiện tại của quân cờ: "))
            target_row = int(input("Nhập hàng mà bạn muốn di chuyển đến: "))
            target_col = int(input("Nhập cột mà bạn muốn di chuyển đến: "))
            if (0 <= current_row < 8) and (0 <= current_col < 8) and (0 <= target_row < 8) and (0 <= target_col < 8):
                return current_row, current_col, target_row, target_col
            else:
                print("Nước đi không hợp lệ, vui lòng nhập lại!")
        except ValueError:
            print("Nước đi không hợp lệ, vui lòng nhập lại!")

def move_piece(data, player, current_row, current_col, target_row, target_col):
    global p1_count, p2_count
    # Kiểm tra vị trí hiện tại có quân cờ của người chơi
    if data[current_row][current_col] == player:
        if data[target_row][target_col] == 0 and abs(target_row - current_row) == 2 and abs(target_col - current_col) == 2:
            if player == 1:
                mid_row = current_row + 1
                mid_col = int((current_col + target_col) /2)
                print(mid_col,mid_row)
            else:
                mid_row = current_row - 1
                mid_col = int((current_col - target_col) /2)

            if data[mid_row][mid_col] == (3 - player):
                if is_valid_move(data, player, current_row, current_col, target_row, target_col):
                    data[target_row][target_col] = player
                    data[mid_row][mid_col] = 0
                    data[current_row][current_col] = 0
                    print("Quân cờ đã ăn quân đối phương!")
                    check_and_update_king(data, player, target_row, target_col)
            elif data[mid_row][mid_col] == player:
                print("Vị trí đích đã có quân cờ!")

        elif data[target_row][target_col] == 0 and abs(target_row - current_row) == 1 and abs(target_col - current_col) == 1:
            if is_valid_move(data, player, current_row, current_col, target_row, target_col):
            # Di chuyển quân cờ
                data[target_row][target_col] = player
                data[current_row][current_col] = 0
                print("Di chuyển thành công!")
                check_and_update_king(data, player, target_row, target_col)
        else:
            print("Di chuyển không thành công!")

        if player == 1:
            p1_count += 1
        else:
            p2_count += 1

    elif data[current_row][current_col] in [3,4]:
        if data[target_row][target_col] == 0 and abs(target_row - current_row) == 2 and abs(target_col - current_col) == 2:
            mid_row = (current_row + target_row) // 2
            mid_col = (current_col + target_col) // 2
            # print(mid_col,mid_row)

            if data[mid_row][mid_col] == (3 - player) or data[mid_row][mid_col] in [3,4]:
                if is_valid_king_move(data, player, current_row, current_col, target_row, target_col):
                    if data[current_row][current_col] == 3:
                        data[target_row][target_col] = 3
                        data[mid_row][mid_col] = 0
                        data[current_row][current_col] = 0
                        print("Quân cờ đã ăn quân đối phương!")
                    elif data[current_row][current_col] == 4:
                        data[target_row][target_col] = 4
                        data[mid_row][mid_col] = 0
                        data[current_row][current_col] = 0
                        print("Quân cờ đã ăn quân đối phương!")
            elif data[mid_row][mid_col] == player:
                print("Vị trí đích đã có quân cờ!")

        elif data[target_row][target_col] == 0 and abs(target_row - current_row) == 1 and abs(target_col - current_col) == 1:
            if is_valid_king_move(data, player, current_row, current_col, target_row, target_col):
                if data[current_row][current_col] == 3:
                    data[target_row][target_col] = 3
                    data[current_row][current_col] = 0
                    print("Di chuyển thành công!")
                elif data[current_row][current_col] == 4:
                    data[target_row][target_col] = 4
                    data[current_row][current_col] = 0
                    print("Di chuyển thành công!")
        else:
            print("Di chuyển không thành công!")

        if player == 1:
            p1_count += 1
        else:
            p2_count += 1

    else:
        print("Không có quân cờ của bạn ở vị trí này!")

def is_valid_move(data, player, current_row, current_col, target_row, target_col):
    # Kiểm tra xem vị trí đích có trống không
    if player == 1:  # Nếu là người chơi 1 (quân 'x')            # Kiểm tra xem nước đi có phù hợp không
        return (target_row > current_row)
    elif player == 2:  # Nếu là người chơi 2 (quân 'o')
        return (target_row < current_row)

def check_and_update_king(data, player, target_row, target_col):
    if player == 1 and target_row == 7:  
        data[target_row][target_col] = 3  # Cập nhật thành 'X' (vua)
        print("Quân 'x' đã được trở thành vua 'xXx' !")
    elif player == 2 and target_row == 0:  
        data[target_row][target_col] = 4  # Cập nhật thành 'O' (vua)
        print("Quân 'o' đã được trở thành vua 'o0o' !")

def is_valid_king_move(data, player, current_row, current_col, target_row, target_col):
    if player == 1:  
        return (target_row > current_row) or (target_row < current_row)
    elif player == 2:
        return (target_row < current_row) or (target_row > current_row)

def check_win(data, player):
    # Đếm số quân cờ của mỗi người chơi
    p1_pieces = sum(row.count(1) for row in data)
    p2_pieces = sum(row.count(2) for row in data)
    king_p1 = sum(row.count(3) for row in data)
    king_p2 = sum(row.count(4) for row in data)
    # Nếu một trong hai người chơi không còn quân cờ, trả về True
    if (p1_pieces == 0 and king_p1 == 0) or (p2_pieces == 0 and king_p2 == 0):
        return True
    return False


data = [
    [0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [2, 0, 2, 0, 2, 0, 2, 0],
    [0, 2, 0, 2, 0, 2, 0, 2],
    [2, 0, 2, 0, 2, 0, 2, 0],
    
    # [0, 0, 0, 0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0, 0, 2, 0],
    # [0, 0, 0, 0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0, 0, 0, 0],
    # [0, 0, 2, 0, 1, 0, 0, 0],
    # [0, 0, 0, 0, 0, 1, 0, 0],
    # [0, 0, 0, 0, 0, 0, 0, 0],
]

print("     ##### Chào mừng tới Cờ đam (Checkers) #####     ")
print("  Lưu ý:")
print("1.Bạn cần nhập từng hàng, cột của quân cờ")
print("2.Bạn có thể lựa chọn đầu hàng bằng cách nhập 100 vào ô nhập hàng hiện tại.")
print("3.Bạn cần phải nhập đúng vị trí và đúng ô cần đến nếu không sẽ bị mất lượt.")
print("""4.Điều quan trọng phải nhắc lại 3 lần:
            NHỚ ĐIỀN ĐÚNG Ô
            NHỚ ĐIỀN ĐÚNG Ô
            NHỚ ĐIỀN ĐÚNG Ô""")
print("""5.Nếu bạn điền sai và muốn điền lại thì:
            i. Nhấn enter vào ô điền trống
           ii. Nhập đầu vào là số có giá trị lớn hơn 8
          iii. Nhập vào 1 ký tự bất kì""")
print("6.Khi quân cờ của người chơi đi đến cuối bàn cờ: quân 'K' là vua của 'x' và 'Q' là vua của 'y;.")
print("7.Bạn đã nắm rõ được các quy tắc, hãy tận hưởng trò chơi!!")
print(" ")
p1_count = 0
p2_count = 0
player = 1

while not check_win(data, player):
    board(data)
    print("  ")
    print(f"Số lượt di chuyển của Người chơi 1: {p1_count}")
    print(f"Số lượt di chuyển của Người chơi 2: {p2_count}")
    current_row, current_col, target_row, target_col = get_user_move(player)
    move_piece(data, player, current_row, current_col, target_row, target_col)
    if check_win(data, player):
        print(f"Player {player} thắng!")
        board(data)
        print("Trò chơi kết thúc!!")
        sys.exit()
    # Chuyển lượt cho người chơi tiếp theo
    player = 2 if player == 1 else 1
