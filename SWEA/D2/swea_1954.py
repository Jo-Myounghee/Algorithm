import sys

sys.stdin = open("./input_data/input_1954.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    numbers = list(range(1, (N**2) + 1))
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    d = 0
    valX = valY = 0


    def Wall(valX, valY):
        testX = valX + dx[d]
        testY = valY + dy[d]
        if testX < 0 or testX >= N:
            return True
        elif testY < 0 or testY >= N:
            return True
        elif arr[testY][testX] != 0:
            return True
        else:
            return False

    for i in numbers:
        if Wall(valX, valY):
            d += 1
            d %= 4

        arr[valY][valX] = i
        testX = valX + dx[d]
        testY = valY + dy[d]
        valX = testX
        valY = testY
    print(f'#{tc}')
    for i in range(N):
        for j in range(N):
            print(f'{arr[i][j]}', end=' ')
        print()