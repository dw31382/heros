#!/usr/bin/env python3

import os

# os.system("ls /usr/share/man/man* >> man.txt")

# reads the txt files into a list
with open("man.txt", "r") as file:
    pages = file.readlines()
file.close()

p = []

for x in pages:
    p.append(x.split('.gz')[0])

os.system("mkdir man".format())
i = 0
for j in p:
    os.system("touch ./man/{}.html 2>/dev/null".format(j))
    os.system("echo '<pre>' > ./man/{}.html 2>/dev/null".format(j))
    os.system("man {} >> ./man/{}.html 2>/dev/null".format(j, j))
    print("progress: " + str((i*100)/(len(p)-1)))
    i += 1