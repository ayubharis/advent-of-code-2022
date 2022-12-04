# Part One
prio = dict()
for i in range(26):
    char = chr(ord('a') + i)
    prio[char] = i+1
for i in range(26):
    char = chr(ord('A') + i)
    prio[char] = i+26+1

sack_prio = []

with open('inp1.txt', 'r') as file:
    for row in file:
        line = row.strip()
        n = len(line)
        left, right = set(line[:n//2]), set(line[n//2:])
        for item in (left & right):
            sack_prio.append(prio[item])

print(sum(sack_prio))