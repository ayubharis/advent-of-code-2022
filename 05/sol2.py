from collections import deque
with open('inp1.txt', 'r') as file:
    stacks = [deque() for _ in range(9)]
    commands = []
    for line in file:
        values = line.strip("\n").replace("    ", "# ").split(" ")
        #print(values)
        if len(values) > 9: continue
        if line.startswith("move"):
            amt, frm, to = map(int, values[1::2])
            tmp = deque()
            for _ in range(amt):
                tmp.append(stacks[frm-1].pop())
            for _ in range(amt): #should probably just use reverse iterator
                stacks[to-1].append(tmp.pop())
        else:
            for i, val in enumerate(values):
                if val not in ["#", ""]:
                    stacks[i].appendleft(val.strip("#[]"))
#print(stacks)
tops = [s[-1] for s in stacks]
print(''.join(tops))
