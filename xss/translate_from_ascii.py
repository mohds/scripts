import sys

input_file = sys.argv[1]
output=""


with open(input_file) as f:
    while True:
        c = f.read(1)
        if not c:
            break
        else:
            output += "&#x" + str(c.encode("hex"))
    print(output)
