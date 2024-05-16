def check_win(board, player, last_move):
    row, col = last_move
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]  # right, down, down-right, down-left
    
    for dr, dc in directions:
        count = 1
        for i in range(1, 5):
            r, c = row + dr * i, col + dc * i
            if 0 <= r < 19 and 0 <= c < 19 and board[r][c] == player:
                count += 1
            else:
                break
        
        for i in range(1, 5):
            r, c = row - dr * i, col - dc * i
            if 0 <= r < 19 and 0 <= c < 19 and board[r][c] == player:
                count += 1
            else:
                break
        
        if count == 5:
            return (row+1, col+1)
    
    return None

def print_rules():
    print("Ласкаво просимо до гри The GAME!")
    print("Правила:")
    print("1. Гра відбувається на дошці розміром 19x19.")
    print("2. Два гравці по черзі ставлять чорні (1) та білі (2) камені.")
    print("3. Чорні завжди ходять першими.")
    print("4. Мета - поставити п'ять каменів одного кольору підряд по горизонталі, вертикалі або діагоналі.")
    print("5. Гра закінчується, коли один з гравців виграє або дошка повністю заповнена (нічия).")

def validate_board(board):
    if len(board) != 19:
        return False
    
    for row in board:
        if len(row) != 19:
            return False
        for cell in row:
            if cell not in [0, 1, 2]:
                return False
    
    return True

def main():
    print_rules()
    
    while True:
        try:
            num_cases = int(input("Введіть кількість тест-кейсів: "))
            break
        except ValueError:
            print("Будь ласка, введіть ціле число.")
    
    for _ in range(num_cases):
        print("Введіть конфігурацію дошки (19 рядків по 19 чисел в кожному, 0 - пусто, 1 - чорний, 2 - білий):")
        
        while True:
            board = []
            for _ in range(19):
                try:
                    row = list(map(int, input().split()))
                    board.append(row)
                except ValueError:
                    print("Неправильний формат введення. Спробуйте ще раз.")
                    break
            else:
                if validate_board(board):
                    break
                else:
                    print("Неправильні розміри дошки або невірні значення. Спробуйте ще раз.")
        
        for row in range(19):
            for col in range(19):
                if board[row][col] != 0:
                    player = board[row][col]
                    win = check_win(board, player, (row, col))
                    
                    if win:
                        print(f"Гравець {player} переміг!")
                        print(f"Виграшна позиція: ({win[0]}, {win[1]})")
                        break
            else:
                continue
            break
        else:
            print("Нічия!")
        
        print()

if __name__ == "__main__":
    main()