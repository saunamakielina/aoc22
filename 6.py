# TUNING TROUBLE
# Find sequence of characters that are all different
def find_block(data, size):
    for i in range(0, len(data)):
        if len(set(data[i : i + size])) == size:
            return i + size


data = open("./6.txt", "r").read()
print(find_block(data, 4))  # Part 1
print(find_block(data, 14))  # Part 2
