import sys

document = open(sys.argv[1], "rb")
contents = document.read()
document.close()

string = contents.decode("utf8")

i = 0
while i<len(string):
    if ord(string[i]) > 127:
        string = string[:i] + "&#" + str(ord(string[i])) + ";" + string[i+1:]
    i = i+1

print(string, end="")
