import sys

document = open(sys.argv[1], "rb")
contents = document.read()
document.close()

for char in contents:
    if char > 127:
        print(sys.argv[1] + ": Non-ascii character found.")
        sys.exit(0)
