from collections import defaultdict
data_stream = ""
with open('inp1.txt', 'r') as file:
    data = file.readlines()
    data_stream = data[0].strip()
seen = defaultdict(int)
unique_chars = 0
STREAM_LENGTH = 14 # 4
for i, c in enumerate(data_stream):
    if unique_chars == STREAM_LENGTH:
        print(i)
        break
    if i >= STREAM_LENGTH:
        removed_char = data_stream[i-STREAM_LENGTH]
        seen[removed_char] -= 1
        if seen[removed_char] == 0:
            unique_chars -= 1
    if seen[c] == 0:
        unique_chars += 1
    seen[c] += 1