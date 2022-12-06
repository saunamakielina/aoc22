# BACKBAG REORGANISATION
import string

with open("3.txt") as f:
    data = [line.strip() for line in f.readlines()]

priorities = " " + string.ascii_lowercase + string.ascii_uppercase

# Part 1 | find same item in both compartments
sum = 0
for x in data:
    start = x[: int(len(x) / 2)]
    end = x[int(len(x) / 2):]
    wrong = "".join(set(start).intersection(end))
    sum += priorities.index(wrong)
print(sum)

# Part 2 | find same item for 3 elves
elves_list = [
    data[i * 3: (i + 1) * 3] for i in range((len(data) + 3 - 1) // 3)
]
sum = 0
for x in elves_list:
    wrong = "".join(set(x[0]).intersection(x[1]))
    wrong = "".join(set(wrong).intersection(x[2]))
    sum += priorities.index(wrong)
print(sum)
