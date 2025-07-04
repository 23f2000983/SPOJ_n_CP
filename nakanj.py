from collections import deque

moves = [(2,1), (1,2), (-1,2), (-2,1), 
         (-2,-1), (-1,-2), (1,-2), (2,-1)]

def to_pos(sq):
    return ord(sq[0]) - ord('a'), int(sq[1]) - 1
def knight_moves(start,end):
    sx,sy=to_pos(start)
    ex,ey=to_pos(end)
    if (sx, sy) == (ex, ey):
        return 0

    vis = [[0]*8 for _ in range(8)]
    q = deque()
    q.append((sx, sy, 0))
    vis[sx][sy] = 1

    while q:
        x, y, d = q.popleft()
        for dx, dy in moves:
            nx, ny = x+dx, y+dy
            if 0 <= nx < 8 and 0 <= ny < 8 and not vis[nx][ny]:
                if (nx, ny) == (ex, ey):
                    return d+1
                vis[nx][ny] = 1
                q.append((nx, ny, d+1))

T = int(input())
for _ in range(T):
    s, e = input().split()
    print(knight_moves(s, e))