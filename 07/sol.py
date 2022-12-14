FILES = {"/" : {}}
with open("inp1.txt", 'r') as file:
    cur_dir = FILES
    visited = []
    for line in file:
        line = line.strip()
        if line.startswith("$"):
            if line == "$ ls": continue
            _, _, dest = line.split(' ')
            if dest == "..":
                cur_dir = visited.pop()
            else:
                visited.append(cur_dir)
                cur_dir = cur_dir[dest]
        else:
            info, name = line.split(' ')
            if info == "dir":
                cur_dir[name] = {}
            else:
                cur_dir[name] = int(info)
#print(FILES)

MAX_ALLOWED_SIZE = 100_000

def add_sizes(dictionary, min_size, max_size):
    total = 0
    count = 0
    for k in dictionary:
        if type(dictionary[k]) == int:
            total += dictionary[k]
        else:
            subTotal, subCount = add_sizes(dictionary[k], min_size, max_size)
            total += subTotal
            count += subCount
    dictionary["SIZE"] = total
    if min_size <= total <= max_size:
        count += total
    return (total, count)

def get_dir_to_delete(dictionary):
    MAX_SIZE = 70_000_000
    REQUIRED_SIZE = 30_000_000
    SPACE_NEEDED = MAX_SIZE - REQUIRED_SIZE
    CURRENT_USAGE = dictionary["SIZE"]
    best_dir = float('inf')
    q = [dictionary]
    while q:
        cur_dict = q.pop()
        if CURRENT_USAGE - cur_dict["SIZE"] <= SPACE_NEEDED:
            best_dir = min(best_dir, cur_dict["SIZE"])
        for k in cur_dict:
            if type(cur_dict[k]) == dict:
                q.append(cur_dict[k])
    return best_dir
print(add_sizes(FILES, 0, MAX_ALLOWED_SIZE))
print(get_dir_to_delete(FILES["/"]))