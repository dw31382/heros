#!/usr/bin/env python3

# get list of all files in a directory
import os

# get list of all files in a directory
def get_files(dir):
    files = []
    for file in os.listdir(dir):
        if os.path.isfile(os.path.join(dir, file)):
            files.append(file)
    return files

files = (get_files('/home/daniel/code/man/'))

files = sorted(files)

d = {}
for file in files:
    if file == "[.1.html":
        pass
    elif file != "pr.1.html":
        pass
    else:
        d[file.split(".")[0]] = file

os.system("cat /home/daniel/code/quicksort >> ./test.txt")

i = 0
for key in d:
    with open("./test.txt") as f:
        text = f.read()
        for key in d:
            text = text.replace(key, "<a href='{}'>".format(d[key]) + key + "</a>")
        with open("./man/{}".format(d[key]), "w") as f:
            f.write(text)
        f.close()
    f.close()
    progress = (i*100)/(len(files)-1)
    print("progress: {}%".format(progress) + ", checking key: {}".format(key))
    i += 1