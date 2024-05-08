{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Haniki2k4/Checkers/blob/main/Checkers.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "G3m1daz2_CfJ"
      },
      "source": [
        "Create board\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "VRXWqn3H_LQk"
      },
      "outputs": [],
      "source": [
        "from copy import deepcopy\n",
        "\n",
        "def board(data):\n",
        "    show = deepcopy(data)\n",
        "    for i in range(len(data)):\n",
        "        for j in range(len(data[i])):\n",
        "            if data[i][j] == 0:\n",
        "                show[i][j] = \" \"\n",
        "            elif data[i][j] == 1:\n",
        "                show[i][j] = \"x\"\n",
        "            elif data[i][j] == 2:\n",
        "                show[i][j] = 'o'\n",
        "            else:\n",
        "                raise Exception(\"Error!\")\n",
        "\n",
        "    print('   Player 1: x                      Player 2: o')\n",
        "    print(' ')\n",
        "    print(f\"|-----|-----|-----|-----|-----|-----|-----|-----|\")\n",
        "    print(f\"|  {show[0][0]}  |  {show[0][1]}  |  {show[0][2]}  |  {show[0][3]}  |  {show[0][4]}  |  {show[0][5]}  |  {show[0][6]}  |  {show[0][7]}  |  0  \")\n",
        "    print(f\"|-----|-----|-----|-----|-----|-----|-----|-----|\")\n",
        "    print(f\"|  {show[1][0]}  |  {show[1][1]}  |  {show[1][2]}  |  {show[1][3]}  |  {show[1][4]}  |  {show[1][5]}  |  {show[1][6]}  |  {show[1][7]}  |  1  \")\n",
        "    print(f\"|-----|-----|-----|-----|-----|-----|-----|-----|\")\n",
        "    print(f\"|  {show[2][0]}  |  {show[2][1]}  |  {show[2][2]}  |  {show[2][3]}  |  {show[2][4]}  |  {show[2][5]}  |  {show[2][6]}  |  {show[2][7]}  |  2  \")\n",
        "    print(f\"|-----|-----|-----|-----|-----|-----|-----|-----|\")\n",
        "    print(f\"|  {show[3][0]}  |  {show[3][1]}  |  {show[3][2]}  |  {show[3][3]}  |  {show[3][4]}  |  {show[3][5]}  |  {show[3][6]}  |  {show[3][7]}  |  3  \")\n",
        "    print(f\"|-----|-----|-----|-----|-----|-----|-----|-----|\")\n",
        "    print(f\"|  {show[4][0]}  |  {show[4][1]}  |  {show[4][2]}  |  {show[4][3]}  |  {show[4][4]}  |  {show[4][5]}  |  {show[4][6]}  |  {show[4][7]}  |  4  \")\n",
        "    print(f\"|-----|-----|-----|-----|-----|-----|-----|-----|\")\n",
        "    print(f\"|  {show[5][0]}  |  {show[5][1]}  |  {show[5][2]}  |  {show[5][3]}  |  {show[5][4]}  |  {show[5][5]}  |  {show[5][6]}  |  {show[5][7]}  |  5  \")\n",
        "    print(f\"|-----|-----|-----|-----|-----|-----|-----|-----|\")\n",
        "    print(f\"|  {show[6][0]}  |  {show[6][1]}  |  {show[6][2]}  |  {show[6][3]}  |  {show[6][4]}  |  {show[6][5]}  |  {show[6][6]}  |  {show[6][7]}  |  6  \")\n",
        "    print(f\"|-----|-----|-----|-----|-----|-----|-----|-----|\")\n",
        "    print(f\"|  {show[7][0]}  |  {show[7][1]}  |  {show[7][2]}  |  {show[7][3]}  |  {show[7][4]}  |  {show[7][5]}  |  {show[7][6]}  |  {show[7][7]}  |  7  \")\n",
        "    print(f\"|-----|-----|-----|-----|-----|-----|-----|-----|\")\n",
        "    print(f\"   0     1     2     3     4     5     6     7   \")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "bAJSpN9MHL8r"
      },
      "source": [
        "Move"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "yaFGAD-LHM6q"
      },
      "outputs": [],
      "source": [
        "def get_user_move(player):\n",
        "    print(\"___________________________________________________\")\n",
        "    print(f\"Lượt của Player {player}:\")\n",
        "    current_row = int(input(\"Nhập hàng hiện tại của quân cờ: \"))\n",
        "    current_col = int(input(\"Nhập cột hiện tại của quân cờ: \"))\n",
        "    target_row = int(input(\"Nhập hàng mà bạn muốn di chuyển đến: \"))\n",
        "    target_col = int(input(\"Nhập cột mà bạn muốn di chuyển đến: \"))\n",
        "    return current_row, current_col, target_row, target_col\n",
        "\n",
        "def move_piece(data, player, current_row, current_col, target_row, target_col):\n",
        "    global p1_count, p2_count\n",
        "    # Kiểm tra nếu vị trí hiện tại có quân cờ của người chơi\n",
        "    if data[current_row][current_col] == player:\n",
        "        # Gọi hàm is_valid_move() với tất cả các đối số cần thiết\n",
        "        if is_valid_move(data, player, current_row, current_col, target_row, target_col):\n",
        "            # Di chuyển quân cờ\n",
        "            data[target_row][target_col] = data[current_row][current_col]\n",
        "            data[current_row][current_col] = 0\n",
        "            print(\"Di chuyển thành công!\")\n",
        "        else:\n",
        "            print(\"Bước di chuyển không hợp lệ!\")\n",
        "\n",
        "        if player == 1:\n",
        "            p1_count += 1\n",
        "        else:\n",
        "            p2_count += 1\n",
        "    else:\n",
        "        print(\"Không có quân cờ của bạn ở vị trí này!\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "-E7ZxnExonL1"
      },
      "source": [
        "Condition"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 9,
      "metadata": {
        "id": "a8Ct3ijGoxiq"
      },
      "outputs": [],
      "source": [
        "def is_valid_move(data, player, current_row, current_col, target_row, target_col):\n",
        "    # Kiểm tra xem vị trí đích có trống không\n",
        "    if data[target_row][target_col] == 0:\n",
        "        if (0 <= target_row < 8) or (0 <= target_col < 8):          # Kiểm tra xem nước đi có nằm trong bảng không\n",
        "            if player == 1:  # Nếu là người chơi 1 (quân 'x')            # Kiểm tra xem nước đi có phù hợp không\n",
        "                return (abs(target_row - current_row) == 1) and (abs(target_col - current_col) == 1) and (target_row > current_row)\n",
        "            elif player == 2:  # Nếu là người chơi 2 (quân 'o')\n",
        "                return (abs(target_row - current_row) == 1) and (abs(target_col - current_col) == 1) and (target_row < current_row)\n",
        "        else:\n",
        "            print(\"Nước đi nằm ngoài bảng!\")\n",
        "            return False\n",
        "    else:\n",
        "        print(\"Vị trí đích đã có quân cờ!\")\n",
        "        return False\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "BLAVoPUzFkPs"
      },
      "source": [
        "Data & main"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 10,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1000
        },
        "id": "4cyrbQHVEzwk",
        "outputId": "1a938800-e325-40ee-fd08-4ad7f32baab4"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "   Player 1: x                      Player 2: o\n",
            " \n",
            "|-----|-----|-----|-----|-----|-----|-----|-----|\n",
            "|     |  x  |     |  x  |     |  x  |     |  x  |  0  \n",
            "|-----|-----|-----|-----|-----|-----|-----|-----|\n",
            "|  x  |     |  x  |     |  x  |     |  x  |     |  1  \n",
            "|-----|-----|-----|-----|-----|-----|-----|-----|\n",
            "|     |  x  |     |  x  |     |  x  |     |  x  |  2  \n",
            "|-----|-----|-----|-----|-----|-----|-----|-----|\n",
            "|     |     |     |     |     |     |     |     |  3  \n",
            "|-----|-----|-----|-----|-----|-----|-----|-----|\n",
            "|     |     |     |     |     |     |     |     |  4  \n",
            "|-----|-----|-----|-----|-----|-----|-----|-----|\n",
            "|  o  |     |  o  |     |  o  |     |  o  |     |  5  \n",
            "|-----|-----|-----|-----|-----|-----|-----|-----|\n",
            "|     |  o  |     |  o  |     |  o  |     |  o  |  6  \n",
            "|-----|-----|-----|-----|-----|-----|-----|-----|\n",
            "|  o  |     |  o  |     |  o  |     |  o  |     |  7  \n",
            "|-----|-----|-----|-----|-----|-----|-----|-----|\n",
            "   0     1     2     3     4     5     6     7   \n",
            "  \n",
            "Số lượt di chuyển của Người chơi 1: 0\n",
            "Số lượt di chuyển của Người chơi 2: 0\n",
            "___________________________________________________\n",
            "Lượt của Player 1:\n",
            "Nhập hàng hiện tại của quân cờ: 2\n",
            "Nhập cột hiện tại của quân cờ: 7\n",
            "Nhập hàng mà bạn muốn di chuyển đến: 3\n",
            "Nhập cột mà bạn muốn di chuyển đến: 6\n",
            "Di chuyển thành công!\n",
            "   Player 1: x                      Player 2: o\n",
            " \n",
            "|-----|-----|-----|-----|-----|-----|-----|-----|\n",
            "|     |  x  |     |  x  |     |  x  |     |  x  |  0  \n",
            "|-----|-----|-----|-----|-----|-----|-----|-----|\n",
            "|  x  |     |  x  |     |  x  |     |  x  |     |  1  \n",
            "|-----|-----|-----|-----|-----|-----|-----|-----|\n",
            "|     |  x  |     |  x  |     |  x  |     |     |  2  \n",
            "|-----|-----|-----|-----|-----|-----|-----|-----|\n",
            "|     |     |     |     |     |     |  x  |     |  3  \n",
            "|-----|-----|-----|-----|-----|-----|-----|-----|\n",
            "|     |     |     |     |     |     |     |     |  4  \n",
            "|-----|-----|-----|-----|-----|-----|-----|-----|\n",
            "|  o  |     |  o  |     |  o  |     |  o  |     |  5  \n",
            "|-----|-----|-----|-----|-----|-----|-----|-----|\n",
            "|     |  o  |     |  o  |     |  o  |     |  o  |  6  \n",
            "|-----|-----|-----|-----|-----|-----|-----|-----|\n",
            "|  o  |     |  o  |     |  o  |     |  o  |     |  7  \n",
            "|-----|-----|-----|-----|-----|-----|-----|-----|\n",
            "   0     1     2     3     4     5     6     7   \n",
            "  \n",
            "Số lượt di chuyển của Người chơi 1: 1\n",
            "Số lượt di chuyển của Người chơi 2: 0\n",
            "___________________________________________________\n",
            "Lượt của Player 2:\n",
            "Nhập hàng hiện tại của quân cờ: 6\n",
            "Nhập cột hiện tại của quân cờ: 7\n",
            "Nhập hàng mà bạn muốn di chuyển đến: 6\n",
            "Nhập cột mà bạn muốn di chuyển đến: 5\n",
            "Vị trí đích đã có quân cờ!\n",
            "Bước di chuyển không hợp lệ!\n",
            "   Player 1: x                      Player 2: o\n",
            " \n",
            "|-----|-----|-----|-----|-----|-----|-----|-----|\n",
            "|     |  x  |     |  x  |     |  x  |     |  x  |  0  \n",
            "|-----|-----|-----|-----|-----|-----|-----|-----|\n",
            "|  x  |     |  x  |     |  x  |     |  x  |     |  1  \n",
            "|-----|-----|-----|-----|-----|-----|-----|-----|\n",
            "|     |  x  |     |  x  |     |  x  |     |     |  2  \n",
            "|-----|-----|-----|-----|-----|-----|-----|-----|\n",
            "|     |     |     |     |     |     |  x  |     |  3  \n",
            "|-----|-----|-----|-----|-----|-----|-----|-----|\n",
            "|     |     |     |     |     |     |     |     |  4  \n",
            "|-----|-----|-----|-----|-----|-----|-----|-----|\n",
            "|  o  |     |  o  |     |  o  |     |  o  |     |  5  \n",
            "|-----|-----|-----|-----|-----|-----|-----|-----|\n",
            "|     |  o  |     |  o  |     |  o  |     |  o  |  6  \n",
            "|-----|-----|-----|-----|-----|-----|-----|-----|\n",
            "|  o  |     |  o  |     |  o  |     |  o  |     |  7  \n",
            "|-----|-----|-----|-----|-----|-----|-----|-----|\n",
            "   0     1     2     3     4     5     6     7   \n",
            "  \n",
            "Số lượt di chuyển của Người chơi 1: 1\n",
            "Số lượt di chuyển của Người chơi 2: 1\n",
            "___________________________________________________\n",
            "Lượt của Player 1:\n",
            "Nhập hàng hiện tại của quân cờ: 3\n",
            "Nhập cột hiện tại của quân cờ: 6\n",
            "Nhập hàng mà bạn muốn di chuyển đến: 4\n",
            "Nhập cột mà bạn muốn di chuyển đến: 2\n",
            "Bước di chuyển không hợp lệ!\n",
            "   Player 1: x                      Player 2: o\n",
            " \n",
            "|-----|-----|-----|-----|-----|-----|-----|-----|\n",
            "|     |  x  |     |  x  |     |  x  |     |  x  |  0  \n",
            "|-----|-----|-----|-----|-----|-----|-----|-----|\n",
            "|  x  |     |  x  |     |  x  |     |  x  |     |  1  \n",
            "|-----|-----|-----|-----|-----|-----|-----|-----|\n",
            "|     |  x  |     |  x  |     |  x  |     |     |  2  \n",
            "|-----|-----|-----|-----|-----|-----|-----|-----|\n",
            "|     |     |     |     |     |     |  x  |     |  3  \n",
            "|-----|-----|-----|-----|-----|-----|-----|-----|\n",
            "|     |     |     |     |     |     |     |     |  4  \n",
            "|-----|-----|-----|-----|-----|-----|-----|-----|\n",
            "|  o  |     |  o  |     |  o  |     |  o  |     |  5  \n",
            "|-----|-----|-----|-----|-----|-----|-----|-----|\n",
            "|     |  o  |     |  o  |     |  o  |     |  o  |  6  \n",
            "|-----|-----|-----|-----|-----|-----|-----|-----|\n",
            "|  o  |     |  o  |     |  o  |     |  o  |     |  7  \n",
            "|-----|-----|-----|-----|-----|-----|-----|-----|\n",
            "   0     1     2     3     4     5     6     7   \n",
            "  \n",
            "Số lượt di chuyển của Người chơi 1: 2\n",
            "Số lượt di chuyển của Người chơi 2: 1\n",
            "___________________________________________________\n",
            "Lượt của Player 2:\n"
          ]
        },
        {
          "output_type": "error",
          "ename": "KeyboardInterrupt",
          "evalue": "Interrupted by user",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-10-c97b8bffbfc3>\u001b[0m in \u001b[0;36m<cell line: 15>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     18\u001b[0m     \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34mf\"Số lượt di chuyển của Người chơi 1: {p1_count}\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     19\u001b[0m     \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34mf\"Số lượt di chuyển của Người chơi 2: {p2_count}\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 20\u001b[0;31m     \u001b[0mcurrent_row\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcurrent_col\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mtarget_row\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mtarget_col\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mget_user_move\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mplayer\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     21\u001b[0m     \u001b[0mmove_piece\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdata\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mplayer\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcurrent_row\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcurrent_col\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mtarget_row\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mtarget_col\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     22\u001b[0m     \u001b[0mplayer\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;36m2\u001b[0m \u001b[0;32mif\u001b[0m \u001b[0mplayer\u001b[0m \u001b[0;34m==\u001b[0m \u001b[0;36m1\u001b[0m \u001b[0;32melse\u001b[0m \u001b[0;36m1\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m<ipython-input-2-44a4376a140b>\u001b[0m in \u001b[0;36mget_user_move\u001b[0;34m(player)\u001b[0m\n\u001b[1;32m      2\u001b[0m     \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"___________________________________________________\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m     \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34mf\"Lượt của Player {player}:\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 4\u001b[0;31m     \u001b[0mcurrent_row\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0minput\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Nhập hàng hiện tại của quân cờ: \"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      5\u001b[0m     \u001b[0mcurrent_col\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0minput\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Nhập cột hiện tại của quân cờ: \"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      6\u001b[0m     \u001b[0mtarget_row\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0minput\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Nhập hàng mà bạn muốn di chuyển đến: \"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/ipykernel/kernelbase.py\u001b[0m in \u001b[0;36mraw_input\u001b[0;34m(self, prompt)\u001b[0m\n\u001b[1;32m    849\u001b[0m                 \u001b[0;34m\"raw_input was called, but this frontend does not support input requests.\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    850\u001b[0m             )\n\u001b[0;32m--> 851\u001b[0;31m         return self._input_request(str(prompt),\n\u001b[0m\u001b[1;32m    852\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_parent_ident\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    853\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_parent_header\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/ipykernel/kernelbase.py\u001b[0m in \u001b[0;36m_input_request\u001b[0;34m(self, prompt, ident, parent, password)\u001b[0m\n\u001b[1;32m    893\u001b[0m             \u001b[0;32mexcept\u001b[0m \u001b[0mKeyboardInterrupt\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    894\u001b[0m                 \u001b[0;31m# re-raise KeyboardInterrupt, to truncate traceback\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 895\u001b[0;31m                 \u001b[0;32mraise\u001b[0m \u001b[0mKeyboardInterrupt\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Interrupted by user\"\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    896\u001b[0m             \u001b[0;32mexcept\u001b[0m \u001b[0mException\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0me\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    897\u001b[0m                 \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mlog\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mwarning\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Invalid Message:\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mexc_info\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mTrue\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m: Interrupted by user"
          ]
        }
      ],
      "source": [
        "data = [\n",
        "    [0, 1, 0, 1, 0, 1, 0, 1],\n",
        "    [1, 0, 1, 0, 1, 0, 1, 0],\n",
        "    [0, 1, 0, 1, 0, 1, 0, 1],\n",
        "    [0, 0, 0, 0, 0, 0, 0, 0],\n",
        "    [0, 0, 0, 0, 0, 0, 0, 0],\n",
        "    [2, 0, 2, 0, 2, 0, 2, 0],\n",
        "    [0, 2, 0, 2, 0, 2, 0, 2],\n",
        "    [2, 0, 2, 0, 2, 0, 2, 0],\n",
        "]\n",
        "\n",
        "p1_count = 0\n",
        "p2_count = 0\n",
        "player = 1\n",
        "while True:\n",
        "    board(data)\n",
        "    print(\"  \")\n",
        "    print(f\"Số lượt di chuyển của Người chơi 1: {p1_count}\")\n",
        "    print(f\"Số lượt di chuyển của Người chơi 2: {p2_count}\")\n",
        "    current_row, current_col, target_row, target_col = get_user_move(player)\n",
        "    move_piece(data, player, current_row, current_col, target_row, target_col)\n",
        "    player = 2 if player == 1 else 1\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "4RqBJ5CxP9_h"
      },
      "outputs": [],
      "source": [
        "data"
      ]
    }
  ],
  "metadata": {
    "colab": {
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}