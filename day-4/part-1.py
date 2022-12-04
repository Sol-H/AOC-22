f = open('day-4/input.txt', 'r')

sum = 0

for line in f:
    elf1 = line.split(',')[0]
    elf2 = line.split(',')[1]

    elf1_start = int(elf1.split('-')[0])
    elf1_end = int(elf1.split('-')[1])

    elf2_start = int(elf2.split('-')[0])
    elf2_end = int(elf2.split('-')[1])

    if (elf1_start <= elf2_start and elf1_end >= elf2_end) or (elf2_start <= elf1_start and elf2_end >= elf1_end):
      # elf1 is overlapping with elf2 or elf2 is overlapping with elf1
        sum += 1


print(sum)