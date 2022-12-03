f = open('input.txt', 'r')

def get_priority(item):
  if item.islower():
    return ord(item) - 96
  else:
    return ord(item) - 38

priorities = 0

for backpack in f:
  comp1 = backpack[:(len(backpack) - 1) // 2]
  comp2 = backpack[(len(backpack) - 1) // 2:]

  common_item = "".join(set(comp1).intersection(comp2))
  priorities += get_priority(common_item)

print(priorities)
f.close()