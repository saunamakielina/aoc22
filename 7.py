# DIRECTORY CLEAN-UP
with open("7.txt") as f:
    data = [line.strip() for line in f.readlines()]

# Convert data to a directory dictionary
# where each key is the directory path joined by .
dir = {}
now_in = ["~"]
for x in data:
    if x[0:4] == "$ cd" and x[-2:] != "..":  # Make & move to new subfolder
        now_in.append(".".join([now_in[-1], x.split(" ")[-1]]))
        current_dir = now_in[-1]
        dir[current_dir] = 0
        continue
    if x[-2:] == "..":  # Move 1 back and add subfolder size to it
        subfolder = current_dir
        now_in.pop()
        current_dir = now_in[-1]
        dir[current_dir] += dir[subfolder]
    try:  # Add file size to current folder
        a = int(x.split(" ")[0])
        dir[current_dir] += a
    except ValueError:
        continue

for x in range(0, len(now_in)-2):
    subfolder = current_dir
    now_in.pop()
    current_dir = now_in[-1]
    dir[current_dir] += dir[subfolder]

# Part 1
print(sum([dir[key] for key in dir if dir[key] <= 100000]))

# Part 2
free_space = dir["~./"] - (70000000 - 30000000)
d = [dir[i] for i in dir if dir[i] >= free_space]
print(min(d))
