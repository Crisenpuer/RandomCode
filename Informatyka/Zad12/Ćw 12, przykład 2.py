


# Utworzenie listy z literami
uppercase_letters = [chr(i) for i in range(ord('A'), ord('Z') + 1)] # Wielkie litery
lowercase_letters = [chr(i) for i in range(ord('a'), ord('z') + 1)] # Małe litery


# Utworzenie listy z literami w odwrotnej kolejności
uppercase_letters_rev = uppercase_letters.copy()
uppercase_letters_rev.reverse()

lowercase_letters_rev = lowercase_letters.copy()
lowercase_letters_rev.reverse()


# Tekst jawny
Input = "Witaj Grzegorz, chcesz dzisiaj pograć w CB?"


# Definiowanie listy na szyfrogram
Output_list = []


# Funkcja do szyfrowania znaków
def encrypt_alphanumeric(char:str):    
    global uppercase_letters, uppercase_letters_rev, lowercase_letters, lowercase_letters_rev # Zmienne globalne utworzone wcześniej
    encrypted_char = ''

    if char in uppercase_letters:  # Litera jest wielka
        encrypted_char = uppercase_letters_rev[uppercase_letters.index(char)] # Szyfrujemy uzywając list z wielkimi znakami
    elif char in lowercase_letters: # Litera jest mała
        encrypted_char = lowercase_letters_rev[lowercase_letters.index(char)] # Sszyfrujemy uzywając list z małymi znakami
    else: # Podany znak nie znajduje się w listach ze znakami (uppercase_letters, lowercase_letters), więc nie szyfrujemy go (nie mamy informacji o tym jak go zaszyfrować)
        print(f"Podany znak to nie jest angielska litera: {char}")
        encrypted_char = char

    return encrypted_char # Zwracamy zakodowany znak
    print(encrypted_char)

# Lista ze znakami specjalnymi
special_chars = ['@','!','?',' ','.',',']


#Główna pętla
for char in Input:
    if char in special_chars:
        Output_list.append(char) # char jest znakiem specjalnym, jego nie szyfrujemy
    else:
        Output_list.append(encrypt_alphanumeric(char))


# Zamienamy listę za stringa i pokazujemy wynik w konsoli:
Output = ''.join(Output_list)
print(Output)