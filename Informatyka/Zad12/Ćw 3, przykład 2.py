
alfabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]


input = "MATEMATYKA"
przesuniecie = 3


output = ""
dlugosc_alfabet = len(alfabet)
for znak in input:
    idx_litery_we = alfabet.index(znak)
    idx_litery_wy = idx_litery_we + przesuniecie

    while idx_litery_wy > dlugosc_alfabet-1:
        idx_litery_wy -= dlugosc_alfabet

    output += alfabet[idx_litery_wy]

print(output)