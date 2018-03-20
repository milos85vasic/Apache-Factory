import sys

source_file = ""
destination_file = ""
replace_what = ""
replace_with = ""

for arg in sys.argv:
    if sys.argv.index(arg) == 1:
        source_file = arg
    if sys.argv.index(arg) == 2:
        destination_file = arg
    if sys.argv.index(arg) == 3:
        replace_what = arg
    if sys.argv.index(arg) == 4:
        replace_with = arg

print "Wiping:\n"
print "From: " + source_file
print "Into: " + destination_file
print "What: " + replace_what
print "Width: " + replace_with

with open(source_file, "rt") as fin:
    with open(destination_file, "wt") as fout:
        for line in fin:
            fout.write(line.replace(replace_what, replace_with))
