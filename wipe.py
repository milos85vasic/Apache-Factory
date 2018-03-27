import sys

source_file = ""
destination_file = ""
replacement_pairs = []

for arg in sys.argv:
    index = sys.argv.index(arg)
    if index == 1:
        source_file = arg
    if index == 2:
        destination_file = arg
    pair = []
    if index >= 3:
        pair.extend(arg)
        if index % 2 == 0:
            replacement_pairs.extend(pair)
            pair = []

print "Wiping:"
print "From: " + source_file
print "Into: " + destination_file
print "-----"

with open(source_file, "rt") as fin:
    with open(destination_file, "wt") as fout:
        for line in fin:
            replaced = line
            for pair in replacement_pairs:
                print "What: " + pair[0]
                print "Width: " + pair[1]
                print "---"
                replaced = replaced.replace(pair[0], pair[1])
            fout.write(replaced)

print "-----"
