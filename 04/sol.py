num_pairs = 0
with open('inp1.txt', 'r') as file:
    for row in file:
        [l, r] = map(lambda s : s.split('-'), row.strip().split(','))
        [ls, le] = l
        ls, le = int(ls), int(le)
        [rs, re] = r
        rs, re = int(rs), int(re)
        # if (ls >= rs and le <= re) or (ls <= rs and le >= re): # Part One
        #     num_pairs += 1
        [[ls,le], [rs,re]] = sorted([[ls,le], [rs,re]])
        if le >= rs:
            num_pairs += 1
print(num_pairs)
