from getch import getch

def echilibrare():
    s1 = input("Introdu primul sir: ")
    s2 = input("Introdu al doilea sir: ")
    for i in range(len(s1)):
        if s1[i] in s2: echilibrat = True
        else: echilibrat = False
    
    if echilibrat: print("Sirul este echilibrat!")
    else: print("Sirul nu este echilibrat!")

def aparitie():
    s = input("Introdu un sir de caractere: ")
    subsir = input("Introdu cuvantul caruia sa-i afisezi aparitiile: ")
    cuvinte = s.split()

    for cuvant in cuvinte:
        if subsir.lower() in cuvant.lower():
            print(cuvant, end=" ")

def duplica_vocale():
    s = input("Introdu un sir: ")
    if len(s)>100: print("Exista o limita de 100 caractere! Incearca din nou :)")

    sir_nou=""
    for ch in s:
        if ch in "aeiouAEIOU": sir_nou+= ch*2
        else: sir_nou+=ch
    print(f"Sirul nou este: {sir_nou}")

def n_litere():
    s = input("Introdu un sir de caractere: ")
    if len(s)>100: print("Exista o limita de 100 caractere! Incearca din nou :)")

    s = s.split()

    n = int(input("Introdu o valoare pentru n. Aceasta va reprezenta numarul de litere pe care un cuvant trebuie sa-l aiba pentru a fi afisat: "))
    print(f"Cuvintele a cate {n} litere sunt: ", end="")
    for cuvant in s:
        if len(cuvant)==n:
            print(cuvant, end=" ")

def speciale_punctuatie():
    new = ""
    s = input("Introdu un sir de caractere, acesta poate sa includa caractere speciale si semne de punctuatie: ")
    for ch in s:
        if ch.isalnum() or ch.isspace():
            new +=ch
    print(f"Sirul dupa eliminarea semnelul de punctuatie si caracterelor speciale: {new}")


def sortare():
    s = input("Introdu un sir de caractere: ")
    s = s.split()
    s.sort()
    print("Sirul introdus in ordine alfabetica:", *s)

def oglinda():
    s = input("Introdu un sir de caractere: ")
    s = s.split()

    for cuvant in s:
        ogl = ""
        for i in range(len(cuvant) - 1, -1, -1):
            ogl += cuvant[i]
        print(ogl, end=" ")


def main():
    while True:
        print("\n" + "━" * 10 + " <[MENIU]> " + "━" * 10 + "\n"
              "1. Verifica daca doua siruri sunt echilibrate\n"
              "2. Gaseste aparitiile unui subsir intr-un sir dat\n"
              "3. Duplica vocalele dintr-un sir dat\n"
              "4. Afiseaza cuvintele cu N litere dintr-un sir\n"
              "5. Elimina semnele de punctuatie si caracterele speciale\n"
              "6. Afiseaza un sir in ordine alfabetica\n"
              "7. Afiseaza in oglinda cuvintele unui sir\n"
              "X. Iesire\n\n"
              "Optiunea dumneavoastra: ", end="", flush=True)
        choice = getch().decode().upper()
        print(choice)
        match choice:
            case "1":
                echilibrare()  
            case "2":
                aparitie()  
            case "3":
                duplica_vocale() 
            case "4":
                n_litere()
            case "5":
                speciale_punctuatie()
            case "6":
                sortare()
            case "7":
                oglinda()
            case "X":
                exit()

if __name__ == '__main__':
    main()