# SUPPLY STACKS
def get_move_params(row):
    """
    Deduct 1 from to & from to match crate list index
    """
    return int(row[0]), int(row[1]) - 1, int(row[2]) - 1


def top_most_crates(stacks):
    return ("").join([p[-1] for p in stacks])


file = open("./5.txt", "r")
data = file.read().split("\n\n")

# Parse moves to a list of lists [count, from, to]
moves = data[1].split("\n")
moves = [row.split(" ")[1::2] for row in moves]

# Parse stacks to a list of strings where last char is the topmost crate
crates = [x[1::4] for x in data[0].split("\n")]
crates.reverse()
stacks = []
for x in range(0, len(crates[0])):
    stack = ""
    for p in crates:
        stack += p[x]
    stacks.append(stack.strip())

# Part 1 | move only one crate at a time
for row in moves:
    items, src, tgt = get_move_params(row)
    for x in range(0, items):
        stacks[tgt] = stacks[tgt] + stacks[src][-1]  # place
        stacks[src] = stacks[src][:-1]  # remove

# Part 2 | move crate stacks
for row in moves:
    items, src, tgt = get_move_params(row)
    stacks[tgt] = stacks[tgt] + stacks[src][-abs(items) :]  # place
    stacks[src] = stacks[src][: -abs(items)]  # remove

print(top_most_crates(stacks))
