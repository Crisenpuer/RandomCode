
alfabet = ["A","Ą","B","C","Ć","D","E","Ę","F","G","H","I","J","K","L","Ł","M","N",
           "Ń","O","Ó","P","Q","R","S","Ś","T","U","V","W","X","Y","Z","Ź","Ż"]


przesuniecie = 3
Inputs = ["stqjtcoqzcólg","igtlg aloqzg","slńmc óqbóc","elgoóq stczlg óqe","slgtzuaż falgp zlquóż"]
dlugosc_alfabet = len(alfabet)

for input in Inputs: 
    output_word = ""
    input_word = input.upper()
    for id, znak in enumerate(input_word):
        if znak == ' ':
            output_word += znak
        else:
            idx_litery_we = alfabet.index(znak)
            idx_litery_wy = idx_litery_we - przesuniecie

            while idx_litery_wy < 0:
                idx_litery_wy += dlugosc_alfabet

            if input[id].islower():
                output_word += (alfabet[idx_litery_wy]).lower()
            else:
                output_word += alfabet[idx_litery_wy]

    print(f"{input} -> {output_word}")