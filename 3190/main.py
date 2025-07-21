import sys
from collections import deque

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

apple_pos = []
for i in range(k):
    apple_pos.append(list(map(int , sys.stdin.readline().split())))

l = int(sys.stdin.readline())
command = deque()
for i in range(l):
    command.append(list(sys.stdin.readline().split()))

game_time = 0

dir = [0, 1] # 상하/좌우 (-1, 0, 1)로 표현
snake_head = [1, 1] # (1, 1)에서 시작
snake_body = []

while True:
    # command 입력을 검사 후 방향 재설정
    if command and game_time >= int(command[0][0]):
        x, c = command.popleft()

        if c == 'D':
            if dir == [-1, 0]:
                dir = [0, 1]
            elif dir == [1, 0]:
                dir = [0, -1]
            elif dir == [0, -1]:
                dir = [-1, 0]
            elif dir == [0, 1]:
                dir = [1, 0]
        else:
            if dir == [-1, 0]:
                dir = [0, -1]
            elif dir == [1, 0]:
                dir = [0, 1]
            elif dir == [0, -1]:
                dir = [1, 0]
            elif dir == [0, 1]:
                dir = [-1, 0]

    # head와 apple_pos가 겹치면 body를 생성
    if snake_head in apple_pos:
        apple_pos.remove(snake_head)
        if snake_body:
            snake_body.append(snake_body[-1])
        else:
            snake_body.append(snake_head)

    # head의 다음 위치를 검사
    next_head = [snake_head[0] + dir[0], snake_head[1] + dir[1]]
    if next_head[0] > n or next_head[0] < 1 or next_head[1] > n or next_head[1] < 1:
        break
    if next_head in snake_body[1:]:
        break

    
    if snake_body:
            size = len(snake_body)
            if size > 1:
                for i in range(size - 1, 0, -1):
                    snake_body[i] = [snake_body[i - 1][0], snake_body[i - 1][1]]

            snake_body[0] = [snake_head[0], snake_head[1]]

    snake_head = [snake_head[0] + dir[0], snake_head[1] + dir[1]]

    game_time += 1

print(game_time + 1)

