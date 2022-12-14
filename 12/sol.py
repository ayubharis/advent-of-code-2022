from collections import deque
grid = []
start = []
with open("inp1.txt", 'r') as file:
    i = 0
    for line in file:
        j = 0
        this_row = []
        for c in line.strip():
            if c == 'S' or c == 'a':
                start.append((i, j))
                c = 'a'
            this_row.append(c)
            j += 1
        grid.append(this_row)
        i += 1
# print(grid)
LENGTH = len(grid)
HEIGHT = len(grid[0])
cost_map = {}
q = deque()
for (i,j) in start:
    q.append(('a', 0, (i, j)))
while q:
    (last_char, cost, (i, j)) = q.popleft()
    #print(i, j)
    if (not (0 <= i < LENGTH and 0 <= j < HEIGHT)) or (ord(grid[i][j]) > ord(last_char) + 1):
        continue
    cur_char = grid[i][j]
    if cur_char == "E":
        print(i, j)
        print(cost)
        break
    if (i, j) in cost_map: # this actually does nothing since BFS visits closest nodes first
        best = min(cost_map[(i,j)], cost+1)
        cost_map[(i,j)] = best
    else:
        cost_map[(i, j)] = cost
        q.append((cur_char, cost+1, (i+1, j)))
        q.append((cur_char, cost+1, (i, j+1)))
        q.append((cur_char, cost+1, (i-1, j)))
        q.append((cur_char, cost+1, (i, j-1)))
#print(cost_map)