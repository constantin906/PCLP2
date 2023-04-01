from random import randint
from getch import getch

def generare_vector(a, b, n):
    n = int(input("Introdu o valoare pentru n (intre 1 si 20, inclusiv): "))
    while n<1 or n>20:
        n = int(input("Valoarea n trebuie sa fie in intervalul (0, 20]!\nReintrodu valoarea lui n: "))
    a, b = input("Introdu valorile intervalului (a, b], separate prin spatiu: ").split()
    a = int(a)
    b = int(b)
    while a>=b:
        a, b = input("Valorea minima trebuie sa fie mai mica decat valoarea maxima!\nReintrodu valorile intervalului (a, b]:").split()
        a = int(a)
        b = int(b)
    vector = []
    for i in range(n):
        vector.append(randint(a+1, b))
    return vector

def afisare_vector(vector):
    print("Vectorul este: ", *vector)

def media_aritmetica(vector):
    ma = sum(vector)/len(vector)
    print("Elementele mai mari decat media aritmetica a vectorului sunt: ", end="")
    for i in range(len(vector)):
        if vector[i]>ma:
            print(vector[i], end=" ")

def valoare_maxima(vector):
    maxx = vector[0]
    pozitie = 0
    for i in range(len(vector)):
        if vector[i]>maxx:
            maxx = vector[i]
            pozitie = i
    print(f"Valoarea maxima din vector este [{maxx}], pe pozitia [{pozitie}]")

def deplasare(vector, x):
    x = int(input("Introdu o valoare pentru x, aceasta va reprezenta cu cate pozitii sa deplaseze elementele vectorului: "))
    if x==0:
        print(vector)
    elif x>0:
        print(vector[-x:] + vector[:-x])
    else:
        print(vector[-x:] + vector[:-x])

def eliminare(vector, a, b):
    for i in range(len(vector)):
        if vector[i]<a and vector[i]>b:
            print(vector[i])

################################### OPERATII CU MATRICE ###################################

def citire_matrice(mat):
    n, m = map(int, input("Introdu numarul de linii si coloane, separate prin spatiu: ").split())
    for i in range(n):
        valori = input(f"Introdu {m} elemente pentru linia {i+1}, separate prin spatiu: ")
        while len(valori.split())!=m:
            valori = input(f"Introdu {m} elemente pentru linia {i+1}, separate prin spatiu: ")
        mat.append([int(x) for x in valori.split()])
    return mat

def afisare_matrice(mat):
    for linie in mat:
        for elem in linie:
            print(f"{elem:5d}", end="")
        print()

def maxx_linie(mat):
    print("Elementele maxime de pe fiecare linie sunt: ", end="")
    for linie in mat:
        el_max = linie[0]
        for element in linie:
            if element>el_max: el_max = element
        print(el_max, end=" ")

def maxx_coloana(mat):
    print("Elementele maxime de pe fiecare coloana sunt: ", end="")
    for coloana in zip(*mat):
        print(coloana)
        el_max = coloana[0]
        for element in coloana:
            if element>el_max: el_max = element
        print(el_max, end=" ")

def transpusa(mat):
    n = len(mat)
    m = len(mat[0])
    for j in range(m):
        for i in range(n):
            print(mat[i][j], end=" ")
        print()

def adauga_linie(mat):
    m = len(mat[0])
    valori = input(f"Introdu {m} elemente pentru linia noua, separate prin spatiu: ")
    while len(valori.split())!=m:
        valori = input(f"Introdu {m} elemente pentru linia noua, separate prin spatiu: ")
    mat.append([int(el) for el in valori.split()])
    print("Matricea noua este: ")
    for linie in mat:
        for elem in linie:
            print(f"{elem:5d}", end="")
        print()


def adauga_coloana(mat):
    n = len(mat)
    valori = input(f"Introdu {n} elemente pentru coloana noua, separate prin spatiu: ").split()
    while len(valori)!=n:
        valori = input(f"Introdu {n} elemente pentru coloana noua, separate prin spatiu: ").split()
    coloana = [int(x) for x in valori]
    for i in range(n):
        mat[i].append(coloana[i])
    print("Matricea noua este: ")
    for linie in mat:
        for elem in linie:
            print(f"{elem:5d}", end="")
        print()

def sterge_linie(mat):
    n = int(input("Introdu numarul liniei pe care vrei sa o stergi: "))-1
    del mat[n]
    print("Matricea noua este: ")
    for linie in mat:
        for elem in linie:
            print(f"{elem:5d}", end="")
        print()

def sterge_coloana(mat):
    n = int(input("Introdu numarul coloanei pe care vrei sa o stergi: "))-1
    for linie in mat:
        del linie[n]
    for linie in mat:
        for elem in linie:
            print(f"{elem:5d}", end="")
        print()

def linializare(mat):
    n, m = len(mat), len(mat[0])
    vector = []
    for i in range(n):
        for j in range(m):
            vector.append(str(mat[i][j]))
    print("Linializare matrice: ", ", ".join(vector))
            

def matrice():
    mat = []
    while True:
        print("\n" + "━" * 10 + " <[MENIU MATRICE]> " + "━" * 10 + "\n"
              "1. Citire matrice (pe linii)\n"
              "2. Afisare matrice\n"
              "3. Afisare elemente maxime (pe linii)\n"
              "4. Afisare elemente maxime (pe coloane)\n"
              "5. Afisare matrice transpusa\n"
              "6. Adauga linie\n"
              "7. Adauga coloana\n"
              "8. Sterge linie\n"
              "9. Sterge coloana\n"
              "0. Linializare matrice\n"
              "X. Revenire meniu principal\n\n"
              "Optiunea dumneavoastra: ", end="")
        choice = getch().decode().upper()
        print(choice)
        match choice:
            case "1":
                mat = citire_matrice(mat)
            case "2":
                afisare_matrice(mat)
            case "3":
                maxx_linie(mat)
            case "4":
                maxx_coloana(mat)
            case "5":
                transpusa(mat)
            case "6":
                adauga_linie(mat)
            case "7":
                adauga_coloana(mat)
            case "8":
                sterge_linie(mat)
            case "9":
                sterge_coloana(mat)
            case "0":
                linializare(mat)
            case "X":
                main()


def main():
    a, b, n, x = 0, 0, 0, 0
    while True:
        print("\n"+ "━" * 10 + " <[MENIU PRINCIPAL]> " + "━" * 10 + "\n"
              "A. Generare vector de n elemente\n"
              "B. Afisare vector generat\n"
              "C. Afisare elemente > media aritmetica a vectorului\n"
              "D. Determinare valoare maxima si pozitia\n"
              "E. Deplasare elemente cu x pozitii\n"
              "F. Eliminare elemente care nu apartin intervalului [a, b]\n"
              "G. Info autor\n"
              "M. Meniu matrice\n"
              "H. Exit\n\n"
              "Optiunea dumneavoastra: ", end="")
        choice = getch().decode().upper()
        print(choice)
        match choice:
            case "A":
                vector = generare_vector(a, b, n)
            case "B":
                afisare_vector(vector)
            case "C":
                media_aritmetica(vector)
            case "D":
                valoare_maxima(vector)
            case "E":
                deplasare(vector, x)
            case "F":
                eliminare(vector, a, b)
            case "G":
                print("Info autor: Tanase Constantin")
            case "H":
                exit()
            case "M":
                matrice()

if __name__ == '__main__':
    main()