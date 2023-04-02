from getch import getch

def suma_n(n):
    sum = 0
    n = int(input("Introdu un numar natural n: "))
    for i in range(1, n+1):
        sum+=i
    print(f"Suma primelor [{n}] numere naturale este: {sum}")

def cmmdc(a, b):
    print(f"Cel mai mare divizor comun dintre [{a}] si [{b}] este: ", end="")
    while b:
        a, b = b, a%b
    print(a)

def inversare(n):
    n = [int(el) for el in input("Introdu o lista de numere intregi, separate prin spatiu: ").split()]
    for i in range(len(n)-1, -1, -1):
        print(n[i], end=" ")

def nr_cuvinte(s):
    s = input("Introdu un sir de caractere: ")
    print(f"Sirul contine {len(s.split())} cuvinte!")

def maxx(n):
    n = [int(el) for el in input("Introdu o lista de numere intregi, separate prin spatiu: ").split()]
    maxxx = n[0]
    minn = n[0]
    for i in n:
        if i>maxxx:
            maxxx = i
        elif i<minn:
            minn = i
    print(f"Cel mai mare element din lista este: {maxxx}\nCel mai mic element din lista este: {minn}")

def este_prim(n):
    while n<=1:
        n = int(input("Introdu o valoare pentru n, aceasta trebuie sa fie mai mare decat 1: "))
    prim_sau_nu = True
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            prim_sau_nu = False
            break
    if prim_sau_nu: print(f"Numarul [{n}] este prim!")
    else: print(f"Numarul [{n}] nu este prim!")

def este_perfect(n):
    n = int(input("Introdu o valoare pentru n: "))
    suma_d = 0
    for i in range(1, n):
        if n%i==0:
            suma_d+=i
    if suma_d == n: print(f"Numarul [{n}] este perfect!")
    else: print(f"Numarul [{n}] nu este perfect!")


def s_palindrom(s):
    s = input("Introdu un sir de caractere: ")
    cuvinte = s.split()
    invers = []
    for i in range(len(cuvinte)-1, -1, -1):
        invers.append(cuvinte[i])
    invers_str = ' '.join(invers)
    if invers_str == s: print("Sirul introdus este palindrom!")
    else: print("Sirul introdus nu este palindrom!")

def sortare(n):
    n = [int(el) for el in input("Introdu o lista de numere intregi, separate prin spatiu: ").split()]
    ordine = input("Cum vrei sa ordonezi lista? Scrie 'C' pentru a ordona lista crescator, sau 'D' pentru descrescator: ")
    match ordine.upper():
        case "C":
            n.sort()
            print("Lista sortata crescator este: ", *n)
        case "D":
            n.sort(reverse=True)
            print(f"Lista sortata descrescator este: ", *n)

def sortare_sir(s):
    s = input("Introdu un sir de caractere: ")
    s = s.split() # Transformam sirul de caractere intr-o lista
    s.sort() # Pentru sortare inversa, introdu "reverse=True"
    print("Sirul introdus in ordine alfabetica:", *s)
    ######## MAJUSCULELE VOR APAREA INTOTDEAUNA INAINTEA ELEMENTELOR CARE INCEP CU LITERA MICA ########


def main():
    n = 0
    s = 0
    while True:
        print("\n" + "━" * 10 + " <[MENIU]> " + "━" * 10 + "\n"
              "1. Calculeaza suma primelor n numere naturale\n"
              "2. CMMDC a doua numere intregi\n"
              "3. Inverseaza ordinea unei liste\n"
              "4. Determina numarul de cuvinte dintr-un sir\n"
              "5. Determina cel mai mare si cel mai mic element dintr-o lista\n"
              "6. Determina daca un numar este prim sau nu\n"
              "7. Determina daca un sir este palindrom\n"
              "8. Determina daca un numar este perfect sau nu\n"
              "9. Sorteaza o lista in ordine crescatoare/descrescatoare\n"
              "0. Iesire\n\n"
              "Optiunea dumneavoastra: ", end="", flush=True)
        choice = getch().decode().upper()
        print(choice)
        match choice:
            case "1":
                suma_n(n)
            case "2":
                valori = input("Introdu doua numere intregi, separate prin spatiu: ")
                a, b = valori.split()
                a = int(a)
                b = int(b)
                cmmdc(a, b)
            case "3":
                inversare(n)
            case "4":
                nr_cuvinte(s)
            case "5":
                maxx(n)
            case "6":
                este_prim(n)
            case "7":
                s_palindrom(s)
            case "8":
                este_perfect(n)
            case "9":
                sortare(n)
            case "0":
                exit()


if __name__ == '__main__':
    main()