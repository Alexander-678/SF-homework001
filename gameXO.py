
import random

field = [[" ", "0", "1", "2"],["0", "-", "-", "-"],["1", "-", "-", "-"],["2", "-", "-", "-"]]
xy = [0,0]
gameover = 0

def result(): # Вывод результатов хода
    print("")
    for x in range(0, len(field)):
        for y in range(0, len(field[x])):
            print(field[x][y], end=" ")
        print("")
    print("")
    return

def turngame(): # Ввод хода игрока
    while True:
        inxy = input("Ведите координаты Вашего хода двумя числами в формате 'Столбец Строка': ")
        inxy2 = list(map(int, inxy.split()))[::-1]
        if 0 <= inxy2[0] <= 2 and 0 <= inxy2[1] <= 2:
            if field[inxy2[0]+1][inxy2[1]+1] == "-":
                break
            else:
                print("Это поле уже занято, будьте внимательны, попробуйте еще раз")
        else:
            print("Некорректный вввод, пожалуйста, будьте внимательны, попробуйте еще раз")
    return inxy2

def turncomp(): # Логика ответного хода

# Блок занятия центра если свободен
    if field[2][2] == "-":
        field[2][2] = "O"
        return 0  # признак Игра не окончена

# Блок проверки поражения компьютера
    i,contXO = 1,0 # Проверка 1 строки на три X
    while i <= 3:
        if field[1][i] == "X":
            contXO += 1
        i += 1
    if contXO == 3:
        return 1 # признак Победа Игрока
    i,contXO = 1,0 # Проверка 2 строки на три X
    while i <= 3:
        if field[2][i] == "X":
            contXO += 1
        i += 1
    if contXO == 3:
        return 1 # признак Победа Игрока
    i,contXO = 1,0 # Проверка 3 строки на три X
    while i <= 3:
        if field[3][i] == "X":
            contXO += 1
        i += 1
    if contXO == 3:
        return 1 # признак Победа Игрока
    i,contXO = 1,0 # Проверка 1 столбца на три X
    while i <= 3:
        if field[i][1] == "X":
            contXO += 1
        i += 1
    if contXO == 3:
        return 1 # признак Победа Игрока
    i,contXO = 1,0 # Проверка 2 столбца на три X
    while i <= 3:
        if field[i][2] == "X":
            contXO += 1
        i += 1
    if contXO == 3:
        return 1 # признак Победа Игрока
    i,contXO = 1,0 # Проверка 3 столбца на три X
    while i <= 3:
        if field[i][3] == "X":
            contXO += 1
        i += 1
    if contXO == 3:
        return 1 # признак Победа Игрока
    i,contXO = 1,0 # Проверка диагонали на три X
    while i <= 3:
        if field[i][i] == "X":
            contXO += 1
        i += 1
    if contXO == 3:
        return 1 # признак Победа Игрока
    i,contXO = 1,0 # Проверка другой диагонали на три X
    while i <= 3:
        if field[i][4-1] == "X":
            contXO += 1
        i += 1
    if contXO == 3:
        return 1 # признак Победа Игрока

# Проверяем состояние НИЧЬЯ
    contXO = 0
    i,j = 1,1
    while i <= 3:
        j = 0
        while j <= 3:
            if field[i][j] == "-":
                contXO += 1
            j += 1
        i += 1
    if contXO == 0:
        return 3 # признак НИЧЬЯ

# Блок попытки выграть
    i,contXO = 1,0 # Проверка 1 строки на два O
    while i <= 3:
        if field[1][i] == "O":
            contXO += 1
        i += 1
    if contXO == 2:
        j = 1
        while j <= 3:
            if field[1][j] == "-":
                field[1][j] = "O"
                return 2 # признак Победа компьютера
            j += 1

    i,contXO = 1,0 # Проверка 2 строки на два O
    while i <= 3:
        if field[2][i] == "O":
            contXO += 1
        i += 1
    if contXO == 2:
        j = 1
        while j <= 3:
            if field[2][j] == "-":
                field[2][j] = "O"
                return 2 # признак Победа компьютера
            j += 1

    i,contXO = 1,0 # Проверка 3 строки на два O
    while i <= 3:
        if field[3][i] == "O":
            contXO += 1
        i += 1
    if contXO == 2:
        j = 1
        while j <= 3:
            if field[3][j] == "-":
                field[3][j] = "O"
                return 2 # признак Победа компьютера
            j += 1

    i,contXO = 1,0 # Проверка 1 столбца на два O
    while i <= 3:
        if field[i][1] == "O":
            contXO += 1
        i += 1
    if contXO == 2:
        j = 1
        while j <= 3:
            if field[j][1] == "-":
                field[j][1] = "O"
                return 2 # признак Победа компьютера
            j += 1

    i,contXO = 1,0 # Проверка 2 столбца на два O
    while i <= 3:
        if field[i][2] == "O":
            contXO += 1
        i += 1
    if contXO == 2:
        j = 1
        while j <= 3:
            if field[j][2] == "-":
                field[j][2] = "O"
                return 2 # признак Победа компьютера
            j += 1

    i,contXO = 1,0 # Проверка 3 столбца на два O
    while i <= 3:
        if field[i][3] == "O":
            contXO += 1
        i += 1
    if contXO == 2:
        j = 1
        while j <= 3:
            if field[j][3] == "-":
                field[j][3] = "O"
                return 2 # признак Победа компьютера
            j += 1

    i,contXO = 1,0 # Проверка диагонали на два O
    while i <= 3:
        if field[i][i] == "O":
            contXO += 1
        i += 1
    if contXO == 2:
        j = 1
        while j <= 3:
            if field[j][j] == "-":
                field[j][j] = "O"
                return 2 # признак Победа компьютера
            j += 1

    i,contXO = 1,0 # Проверка другой диагонали на два O
    while i <= 3:
        if field[i][4-i] == "O":
            contXO += 1
        i += 1
    if contXO == 2:
        j = 1
        while j <= 3:
            if field[j][4-j] == "-":
                field[j][4-j] = "O"
                return 2 # признак Победа компьютера
            j += 1

# Блок сопротивления игроку, шоб не проигрывать слишком легко
    i,contXO = 1,0 # Проверка 1 строки на два X
    while i <= 3:
        if field[1][i] == "X":
            contXO += 1
        i += 1
    if contXO == 2:
        j = 1
        while j <= 3:
            if field[1][j] == "-":
                field[1][j] = "O"
                return 0 # признак Продолжения игры
            j += 1

    i,contXO = 1,0 # Проверка 2 строки на два X
    while i <= 3:
        if field[2][i] == "X":
            contXO += 1
        i += 1
    if contXO == 2:
        j = 1
        while j <= 3:
            if field[2][j] == "-":
                field[2][j] = "O"
                return 0 # признак Продолжения игры
            j += 1

    i,contXO = 1,0 # Проверка 3 строки на два X
    while i <= 3:
        if field[3][i] == "X":
            contXO += 1
        i += 1
    if contXO == 2:
        j = 1
        while j <= 3:
            if field[3][j] == "-":
                field[3][j] = "O"
                return 0 # признак Продолжения игры
            j += 1

    i,contXO = 1,0 # Проверка 1 столбца на два X
    while i <= 3:
        if field[i][1] == "X":
            contXO += 1
        i += 1
    if contXO == 2:
        j = 1
        while j <= 3:
            if field[j][1] == "-":
                field[j][1] = "O"
                return 0 # признак Продолжения игры
            j += 1

    i,contXO = 1,0 # Проверка 2 столбца на два X
    while i <= 3:
        if field[i][2] == "X":
            contXO += 1
        i += 1
    if contXO == 2:
        j = 1
        while j <= 3:
            if field[j][2] == "-":
                field[j][2] = "O"
                return 0 # признак Продолжения игры
            j += 1

    i,contXO = 1,0 # Проверка 3 столбца на два X
    while i <= 3:
        if field[i][3] == "X":
            contXO += 1
        i += 1
    if contXO == 2:
        j = 1
        while j <= 3:
            if field[j][3] == "-":
                field[j][3] = "O"
                return 0 # признак Продолжения игры
            j += 1

    i,contXO = 1,0 # Проверка диагонали на два X
    while i <= 3:
        if field[i][i] == "X":
            contXO += 1
        i += 1
    if contXO == 2:
        j = 1
        while j <= 3:
            if field[j][j] == "-":
                field[j][j] = "O"
                return 0 # признак Продолжения игры
            j += 1

    i,contXO = 1,0 # Проверка другой диагонали на два X
    while i <= 3:
        if field[i][4-i] == "X":
            contXO += 1
        i += 1
    if contXO == 2:
        j = 1
        while j <= 3:
            if field[j][4-j] == "-":
                field[j][4-j] = "O"
                return 0 # признак Продолжения игры
            j += 1

# Блок, который все бездарно проиграет, потому как не думает
# Здесь случайно заполняем одно из пустых мест
# Весь код, реализующий более умную логику, дописывать до этого блока
    i = 1
    fieldempty = []
    listrandom = []
    while i <= 3:
        j = 1
        while j <= 3:
            if field[i][j] == "-":
                fieldempty.append([i,j])
            j += 1
        i += 1
    listrandom = random.sample(fieldempty, 1)
    field[listrandom[0][0]][listrandom[0][1]] = "O"
    return 0

# Основная программа
print(
    """
   Я - твой компьютер считаю, что способен победить тебя в игре "Крестики-нолики".
   Чтобы сделать ход, введи два числа через пробел, в порядке столбец, строка:
   Координаты полей можешь видеть на поле внизу:

                      0 1 2 
                    0 - - - 
                    1 - - - 
                    2 - - -
                   
   Приготовься и не надейся на простую победу! Чтобы начать нажми "Enter".""")
input()
result()
while not gameover:
    xy = turngame()
    field[xy[0]+1][xy[1]+1] = 'X'
    gameover = turncomp()
    result()
if gameover == 1:
    print("Вы победили! Человек умнее!")
elif gameover == 2:
    print("Я победил, Искуственный Интелект сильнее!")
elif gameover == 3:
    print("Game Over! У нас НИЧЬЯ...")
