# CALORIE COUNTING
file = open("./1.txt", "r")
calories = [
    sum([int(i) for i in e]) for e in [x.split("\n") for x in file.read().split("\n\n")]
]

# Part one
print(max(calories))

# Part 2
calories.sort(reverse=True)
print(sum(calories[0:3]))
