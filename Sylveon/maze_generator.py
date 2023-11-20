import random


class MazeGen:
    @staticmethod
    def recursive_backtracking_core(n, m, **kwargs):
        maze = [[1 for _ in range(m)] for _ in range(n)]
        shuffle_dir = kwargs.get("shuffle_dir", True)

        def is_valid(x, y):
            return 0 <= x < n and 0 <= y < m and maze[x][y] == 1

        def dfs(x, y):
            dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            if shuffle_dir:
                random.shuffle(dir)
            for dx, dy in dir:
                nx, ny = x + dx, y + dy
                if is_valid(nx * 2, ny * 2):
                    maze[nx * 2][ny * 2] = maze[x * 2 + dx][y * 2 + dy] = 0
                    dfs(nx, ny)

        sx, sy = random.randint(0, (n - 1) // 2), random.randint(0, (m - 1) // 2)
        maze[sx * 2][sy * 2] = 0
        dfs(sx, sy)
        return maze

    @staticmethod
    def recursive_division_core(n, m, **kwargs):
        maze = [[1 for _ in range(m)] for _ in range(n)]

        def divide(xa, ya, xb, yb):
            if xa == xb and ya == yb:
                return
            cnt_x, cnt_y = xb - xa, yb - ya
            k = random.randint(0, cnt_x + cnt_y - 1)
            if k < cnt_x:
                xm = xa + k
                y_choose = random.randint(ya, yb)
                maze[xm * 2 + 1][y_choose * 2] = 0
                divide(xa, ya, xm, yb)
                divide(xm + 1, ya, xb, yb)
            else:
                k -= cnt_x
                ym = ya + k
                x_choose = random.randint(xa, xb)
                maze[x_choose * 2][ym * 2 + 1] = 0
                divide(xa, ya, xb, ym)
                divide(xa, ym + 1, xb, yb)

        ex, ey = (n - 1) // 2, (m - 1) // 2
        divide(0, 0, ex, ey)

        for i in range(ex + 1):
            for j in range(ey + 1):
                maze[i * 2][j * 2] = 0
        return maze
