grid = []
with open("inp1.txt", 'r') as file:
    for line in file:
        grid.append(list(map(int, line.strip())))

def max_with_count(L):
    M = -1
    c = 0
    for n in L:
        if n == M:
            c += 1
        elif n > M:
            M = n
            c = 1
    return (M, c)

def visible(grid, x, y):
    visible = True
    if x > 0:
        visible = visible and grid[x-1][y] < grid[x][y]
    if x < len(grid) - 1:
        visible = visible and grid[x+1][y] < grid[x][y]
    if y > 0:
        visible = visible and grid[x][y-1] < grid[x][y]
    if y < len(grid[0]) - 1:
        visible = visible and grid[x][y+1] < grid[x][y]
    return visible


# A tree is only visible if its on the edge, or its a unique maximum value
count = 2*(len(grid) + len(grid[0])) - 4 # edges
for row in grid:
    val, cnt = max_with_count(row)
    print(val, cnt)
    if cnt == 1:
        count += 1
    else:
        count += 2
    count -= (val in [row[0], row[-1]])
for j in range(len(grid[0])):
    column = []
    for i in range(len(grid)):
        column.append(grid[i][j])
    # should make new function instead of this slow, memory inefficient stuff 
    val, cnt = max_with_count(column)
    if cnt == 1:
        count += 1
    else:
        count += 2
    count -= (val in [column[0], column[-1]])
# print(count)