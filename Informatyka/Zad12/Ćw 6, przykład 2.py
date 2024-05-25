
# Tutaj nie ma zbyt wiele komentarzy, do Pani, ale mam nadzieje ze Pani bedzie wiedzala jak to dziala

# NAWOEIWATJEERERMJAJZOŚZSEŻČYAKNDDMI (klucz 5/7),
# NOAZSUIWMETSEOJRTŁCKEAWYHOSZYSSCZZCZŁHCUHĘ (klucz 6/7).
# (Y, X)

Inputs = [("NAWOEIWATJEERERMJAJZOŚZSEŻĆYAKNDDMI",5,7), # szyfrogram, wysokość siatki szyfru, szerokość siatki szyfru
          ("NOAZSUIWMETSEOJRTŁCKEAWYHOSZYSSCZZCZŁHCUHĘ",6,7)] # Szyfrogramy i szyfry

for inpidx in range(2):
    inp, gridY, gridX = Inputs[inpidx]
    grid = [['' for i in range(gridX)] for j in range(gridY)]

    # Generowanie siatki tak jak w przykładzie
    idx = 0
    for col in range(gridX):
        for row in range(gridY):
            if idx < len(inp):
                grid[row][col] = inp[idx]
                idx += 1 # hehe python nie ma idx++
    
    # Odczytywanie z siatki, aby odszyfrować wiadomość
    outp = []
    for row in grid:
        outp.extend(row)

    # Zamiana listy na tekst i wpis na konsole
    print(f"{inp} -({gridX},{gridY})> {''.join(outp)}")

