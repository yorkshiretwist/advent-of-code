import io

file = open('2022/1/input.txt', 'r')
lines = file.read()

elves = lines.split('\n\n')

calories = []

for elf in elves:
    elf_calories = elf.split('\n')
    # print(elf_calories)
    total_elf_calories = sum([int(i) for i in elf_calories if i.isdigit()])
    # print(total_elf_calories)
    calories.append(total_elf_calories)

# print(sorted(calories))

print(max(calories))

top_3 = sorted(calories)[-3:]

# print(top_3)

print(sum(top_3))