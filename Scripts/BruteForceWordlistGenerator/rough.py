data = open("bruteresu.txt").read()
data = data.split("\n")
previ = None
common = False
for i in data:
    if i == previ:
        common = True
        previ = i
    else:
        previ = i
print(common)