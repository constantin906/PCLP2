import getch
import math

def combinari():
    n = 10
    m = 0
    while m<1 or m>10:
        m = int(input("Introdu o valoare pentru m, intre 1 si 10: "))
    result = math.factorial(n)/(math.factorial(m)*math.factorial(n-m))
    print(f"Combinari de {n} luate cate {m}: {int(result)}")

def conversie_binar():
    n = int(input("Introdu un numar natural n: "))
    print(f"Numarul {n} in formatul binar este: {bin(n)[2:]}")


def meniu_ex3():

    def citire_afisare():
        valori = input("Introdu doua numere intregi m si n, separate prin spatiu: ")
        m, n = valori.split()
        m = int(m)
        n = int(n)
        print(f"Numerele citite sunt: {m} si {n}")

    while True:
        print("━" * 10 + " <[MENIU EX. 3]> " + "━" * 10 + "\n"
              "1. Citire m si n + afisarea acestora\n"
              "2. Patrate perfecte\n"
              "3. Numere prime\n"
              "4. Numere divizibile cu n si m\n"
              "5. CMMDC\n"
              "6. Exit\n\n"
              "Optiunea dumnveavoastra: ", end="", flush=True
              )
        choice = int(getch.getch())
        print(choice)
        match choice:
            case 1:
                citire_afisare()
            case 6:
                break

def main():
    while True:
        print("━" * 10 + " <[MENIU]> " + "━" * 10 + "\n"
              "1. Combinari de n luate cate m\n"
              "2. Conversia unui numar natural in binar\n"
              "3. Meniu cerinte exercitiul 3\n"
              "4. Calculeaza expresia: S=1-2+3-4+....+n, n apartine [20,50)\n"
              "5. Determina cifra maxima dintr-un numar\n"
              "6. MA cifrelor pare si produsul cifrelor impare dintr-un numar\n"
              "7. Determina daca un numar este perfect\n"
              "8. Calculeaza expresia: 1+1*2+1*2*3+1*2*3*4+...+1*2*...n\n"
              "9. Calculeaza expresia: 1+1/(1*2)+1/(1*2*3)+1/(1*2*3*4)+...+1/(1*2*...n)\n"
              "0. Iesire meniu\n\n"
              "Optiunea dumneavoastra: ", end="", flush=True
              )
        choice = int(getch.getch())
        print(choice)
        match choice:
            case 1:
                combinari()
            case 2:
                conversie_binar()
            case 3:
                meniu_ex3()
            case 0:
                break


if __name__ == '__main__':
    main()