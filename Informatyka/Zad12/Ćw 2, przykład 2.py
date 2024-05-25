

szyfr = {
    "A":"Z",
    "Y":"B",
    "C":"X",
    "W":"D",
    "E":"V",
    "U":"F",
    "G":"T",
    "S":"H",
    "I":"R",
    "Q":"J",
    "K":"P",
    "0":"L",
    "M":"N",
    "Z":"A",
    "B":"Y",
    "X":"C",
    "D":"W",
    "V":"E",
    "F":"U",
    "T":"G",
    "H":"S",
    "R":"I",
    "J":"Q",
    "P":"K",
    "L":"O",
    "N":"M"
}

input = "WLALYZXAVMRZLGIAVXRVQ"

output = ""

for char in input:
    if char in szyfr:
        output += szyfr[char]
    else:
        output += char

print(output)