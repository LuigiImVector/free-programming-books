import re

with open('output.log') as oldfile, open('error.log', 'w') as newfile:
    for line in oldfile:
        if not (b'\xE2\x9A\xA0' in line.encode()):
            if ('warning' in line):
                r = line.partition("warning")[2].partition(" remark")[0]
                s = str(r).rsplit('  ', 1)[0]
                newfile.write(s)
            if ('home/runner/work' in line):
                s = line.replace("/home/runner/work/free-programming-books/", "", 1)
                newfile.write(s)
        else:
            newfile.write("\n\n")

