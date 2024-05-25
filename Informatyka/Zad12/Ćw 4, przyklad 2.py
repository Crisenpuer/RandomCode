alfabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]


input = ["VCBIU","LQIRUPDWBND","NUBSWRJUDILD"]
przesuniecie = 3

dlugosc_alfabet = len(alfabet)

for input_word in input:
    output_word = ""
    for znak in input_word:
        idx_litery_we = alfabet.index(znak)
        idx_litery_wy = idx_litery_we - przesuniecie

        while idx_litery_wy < 0:
            idx_litery_wy += dlugosc_alfabet

        output_word += alfabet[idx_litery_wy]

    print(f"{input_word} -> {output_word}")