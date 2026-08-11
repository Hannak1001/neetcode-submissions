from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(r, c):
            q = deque()
            visited.add((r, c))
            q.append((r, c))
            #right, left, down, up
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    newr, newc = (row+dr), (col+dc)
                    if (newr in range(rows) and newc in range(cols) and 
                        grid[newr][newc] == "1" and 
                        (newr, newc) not in visited):
                        visited.add((newr, newc))
                        q.append((newr, newc))


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1
        return islands
