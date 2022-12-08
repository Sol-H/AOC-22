f = open('day-7/input.txt', 'r')

dirs = {}
subdirs = {}
path = "/"


def count_sizes(path):
  result = dirs[path]
  for subdir in subdirs[path]:
    if subdir in dirs:
      result += count_sizes(subdir)
  return result

for line in f:
  if '$' in line:
    if '$ cd ..' in line:
        path = "/".join(path.split('/')[:-2]) + "/"
    elif '$ cd /' in line:
        path = "/"
    elif '$ cd' in line:
        path += line.split('$ cd ')[1].strip() + "/"
    if path not in dirs:
        dirs[path] = 0
        subdirs[path] = []
  else:
    if 'dir' in line:
        subdirs[path].append(path + line.split('dir ')[1].strip() + "/")
    else:
        dirs[path] += int(line.split(' ')[0].strip())

count = 0   
for dir in dirs:
  if count_sizes(dir) <= 100000:
    count += count_sizes(dir)

print(count)