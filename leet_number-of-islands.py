# 200. Number of Islands
# https://leetcode.com/problems/number-of-islands/

delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
WATER, LAND = '0', '1'

def numIslands(grid):
    R, C = len(grid), len(grid[0])
    checked = [[False] * C for _ in range(R)]
    answer = 0

    def dfs(row, col):
        for dr, dc in delta:
            n_row, n_col = row + dr, col + dc
            if 0 <= n_row < R and 0 <= n_col < C \
            and grid[n_row][n_col] == LAND \
            and checked[n_row][n_col] == False:
                checked[n_row][n_col] = True
                dfs(n_row, n_col)

    for row in range(R):
        for col in range(C):
            if grid[row][col] == WATER:
                continue
            if checked[row][col] == True:
                continue
            
            checked[row][col] = True
            dfs(row, col)
            answer += 1

    return answer

grid = [["1","1","1","1","0"], ["1","1","0","1","0"], ["1","1","0","0","0"], ["0","0","0","0","0"]]
print(numIslands(grid))


