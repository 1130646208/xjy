f = open("fw.txt")
f.seek(0)
lines=f.readlines()
for line in lines:
    print(line)
f.close()
