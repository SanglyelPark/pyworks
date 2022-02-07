f = open("book.xls","r")
lines = f.readlines()
for line in lines:
    print(line)
f.close()