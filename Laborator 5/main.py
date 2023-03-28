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
        a, b = input("Valorea minima trebuie sa fie mai mica decat valoarea maxima!\nReintrodu valorile intervaluli (a, b]:").split()
        a = int(a)
        b = int(b)
    vector = []
    for i in range(n):
        vector.append(randint(a+1, b))
    return vector

def media_aritmetica(vector):
    ma = sum(vector)/len(vector)
    print("Elementele mai mari decat media aritmetica a vectorului sunt: ", end="")
    for i in range(len(vector)):
        if vector[i]>ma:
            print(vector[i], end=" ")

def valoare_maxima(vector):
    maxx = vector[0]
    pozitie = 0
    for i in vector:
        if i>maxx:
            maxx = i
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
        if vector[i]<=a and vector[i]>=b:
            print(vector[i])


def afisare_vector(vector):
    print("Vectorul este: ", *vector)

def main():
    a, b, n, x = 0, 0, 0, 0
    while True:
        print("\n"+ "━" * 10 + " <[MENIU]> " + "━" * 10 + "\n"
              "A. Generare vector de n elemente\n"
              "B. Afisare vector generat\n"
              "C. Afisare elemente > media aritmetica a vectorului\n"
              "D. Determinare valoare maxima si pozitia\n"
              "E. Deplasare elemente cu x pozitii\n"
              "F. Eliminare elemente care nu apartin intervalului [a, b]\n"
              "G. Info autor\n"
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
            case "H":
                exit()      