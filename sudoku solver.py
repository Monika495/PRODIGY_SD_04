N = 9
def printing(arr):
	for i in range(N):
		for j in range(N):
			print(arr[i][j], end = " ")
		print()
def isSafe(grid, r, c, n):
	for x in range(9):
		if grid[r][x] == n:
			return False
	for x in range(9):
		if grid[x][c] == n:
			return False
	sR = r - r % 3
	sC = c - c % 3
	for i in range(3):
		for j in range(3):
			if grid[i + sR][j + sC] == n:
				return False
	return True

def solveSudoku(grid, r, c):

	if (r == N - 1 and c == N):
		return True
	if c == N:
		r += 1
		c = 0
		return solveSudoku(grid, r, c + 1)
	for n in range(1, N + 1, 1):
	
		if isSafe(grid, r, c, n):
			grid[r][c] = n
			if solveSudoku(grid, r, c + 1):
				return True
		grid[r][c] = 0
	return False

grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
		[5, 2, 0, 0, 0, 0, 0, 0, 0],
		[0, 8, 7, 0, 0, 0, 0, 3, 1],
		[0, 0, 3, 0, 1, 0, 0, 8, 0],
		[9, 0, 0, 8, 6, 3, 0, 0, 5],
		[0, 5, 0, 0, 9, 0, 6, 0, 0],
		[1, 3, 0, 0, 0, 0, 2, 5, 0],
		[0, 0, 0, 0, 0, 0, 0, 7, 4],
		[0, 0, 5, 2, 0, 6, 3, 0, 0]]

if (solveSudoku(grid, 0, 0)):
	printing(grid)
else:
	print("no solution exists ")

