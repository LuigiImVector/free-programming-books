import re

with open('output.log') as oldfile, open('error.log', 'w') as newfile:
    for line in oldfile:
        if not (b'\xc3\xa2\xc5\xa1\xc2\xa0' in line.encode()):
            if ('warning' in line):
                r = re.search('warning(.*)remark', line)
                s = r.group(1).rsplit(' ', 1)[0]
                newfile.write(s)
            if ('home/runner/work' in line):
                s = line.replace("/home/runner/work/free-programming-books/", "", 1)
                newfile.write(s)
        else:
            newfile.write("\n\n")
