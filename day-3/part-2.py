f = open('input.txt', 'r')

def get_priority(item):
  if item.islower():
    return ord(item) - 96
  else:
    return ord(item) - 38

priorities = 0
current_group = []

for backpack in f:
  backpack = backpack[:-1]
  current_group.append(backpack)
  if len(current_group) == 3:
    common_item = "".join(set(current_group[0]).intersection(current_group[1]).intersection(current_group[2]))
    current_group = []
    priorities += get_priority(common_item)

print(priorities)
f.close()