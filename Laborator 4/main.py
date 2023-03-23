import getch

def citire():
    global s
    s = input("Introdu sirul de caractere: ")

def afisare():
    print(f"Sirul este: {s}")

def nr_cuvinte():
    cuvinte = s.split()
    print(f"Sirul contine {len(cuvinte)} cuvinte: ")
    for i in range(len(cuvinte)):
        print(f"{i+1}. {cuvinte[i]} = {len(cuvinte[i])} caractere")

def inlocuire():
    x = input("Introdu caracterul pe care vrei sa-l inlocuiesti: ")
    y = input("Introdu caracterul cu care vrei sa fie inlocuit: ")
    sir = s.replace(x, y)
    print(f"Noul sir este: {sir}")

def majuscule():
    lista_m = []
    for i in range(len(s)):
        if s[i].isupper():
            lista_m.append(s[i])
    print(f"Lista cu caracterele majuscule din sirul initial este: {lista_m}")

def aparitii():
    numar_aparitii = 0
    vocale = "aeiouăâîAEIOUĂÂÎ"
    for i in range(len(s)):
        if s[i] in vocale:
            numar_aparitii+=1
    print(f"Numarul de aparitii a vocalelor este: {numar_aparitii}")

def caractere_speciale():
    fara_speciale=""
    for i in s:
        if i.isalnum() or i == " ":
            fara_speciale+=i
    print(f"Sirul introdus fara caracterel speciale este: {fara_speciale}")

def pozitie():
    x = int(input("Introdu pozitia de la care vrei sa pornesti: "))
    print(f"{s[x:]}" + f"{s[:x]}")
            
def main():
    while True:
        print("\n" + "━" * 10 + " <[MENIU]> " + "━" * 10 + "\n"
              "1. Citire sir de caractere\n"
              "2. Afisare sir de caractere\n"
              "3. Afisare nr. total de cuvinte, si numarul de caractere pentru fiecare cuvant\n"
              "4. Inlocuirea caracterului X cu Y (se vor citi de la tastatura)\n"
              "5. Construieste un sir nou doar cu caracterele majuscule din sirul initial\n"
              "6. Afisati numarul de aparitii pentru fiecare vocala din sirul initial\n"
              "7. Eliminati caracterele speciale din sir\n"
              "8. Afisati sirul de la o pozitie X\n"
              "9. Iesire\n\n"
              "Optiunea dumneavoastra: ", end="", flush=True)
        choice = int(getch.getch())
        print(choice)
        
        match choice:
            case 1:
                citire()
            case 2:
                afisare()
            case 3:
                nr_cuvinte()
            case 4:
                inlocuire()
            case 5:
                majuscule()
            case 6:
                aparitii()
            case 7:
                caractere_speciale()
            case 8:
                pozitie()
            case 9:
                return True

if __name__ == "__main__":
    main()