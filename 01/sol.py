# Part One
elf_calories = []
with open('inp1.txt', 'r') as file:
    current_elf = []
    for row in file:
        if row.strip() == "":
            # elf_calories.append((sum(current_elf), current_elf))
            elf_calories.append(sum(current_elf))
            current_elf = []
        else:
            current_elf.append(int(row.strip()))

print(max(elf_calories))
# (70296, [10963, 5485, 10936, 12139, 8948, 10772, 11053])
# Answer: 70296

# Part Two
# Could max heapify elf_calories and pop top 3, but I will just sort
elf_calories.sort(reverse=True)
print(sum(elf_calories[:3]))