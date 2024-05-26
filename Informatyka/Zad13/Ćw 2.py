
alfabet = ["A","Ą","B","C","Ć","D","E","Ę","F","G","H","I","J","K","L","Ł","M","N",
           "Ń","O","Ó","P","Q","R","S","Ś","T","U","V","W","X","Y","Z","Ź","Ż"]


Inputs = ["Bartłomiej Patyk","Gwiezdne wojny, część V: Imperium kontratakuje","Lew"]
przesuniecie = 3
znaki_specjalne = [',','.',' ',':']

dlugosc_alfabet = len(alfabet)
for input in Inputs:
    output = ""
    input_word = input.upper()
    for i, znak in enumerate(input_word):
        if znak in znaki_specjalne:
            litera_wy = znak
        else:
            idx_litery_we = alfabet.index(znak)
            idx_litery_wy = idx_litery_we + przesuniecie

            while idx_litery_wy > dlugosc_alfabet-1:
                idx_litery_wy -= dlugosc_alfabet

            litera_wy = alfabet[idx_litery_wy]

        if input[i].islower():
            output += litera_wy.lower()
        else:
            output += litera_wy

    print(f"{input} -> {output}")