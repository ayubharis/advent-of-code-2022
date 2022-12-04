# Part Two
prio = dict()
for i in range(26):
    char = chr(ord('a') + i)
    prio[char] = i+1
for i in range(26):
    char = chr(ord('A') + i)
    prio[char] = i+26+1

sack_prio = []
lines = []
with open('inp1.txt', 'r') as file:
    for line in file:
        lines.append(line.strip())

for i in range(len(lines)//3):
    s1 = set(lines[3*i])
    s2 = set(lines[3*i+1])
    s3 = set(lines[3*i+2])
    for item in s1 & s2 & s3:
        sack_prio.append(prio[item])
print(sum(sack_prio))