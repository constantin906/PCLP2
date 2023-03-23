import math
import getch

def ex1():
    x = int(input("Introdu un numar intreg. Pentru x>100, se converteste in formatul octal, daca nu, in hexazecimal\nNumarul tau: "))
    if x>100:
        print(f"Numarul {x} in formatul octal este: {oct(x)[2:]}")
    else:
        print(f"Numarul {x} in formatul hexazecimal este: {hex(x)[2:].upper()}")

def ex2():
    print("Ecuatia de gradul intai! (ax+b=0)")
    valori = input("Introdu valorile pentru a si b, separate prin spatiu: ")
    a, b = valori.split()
    a = int(a)
    b = int(b)
    x = -b/a
    print(f"Solutia ecuatiei {a}x+{b} este: x = {x}")

def ex3():
    valori = input("Introdu 3 numere intregi, separate prin spatiu: ")
    a, b, c = valori.split()
    a = int(a)
    b = int(b)
    c = int(c)
    if(a==b-1==c-2) or (a==b+1==c+2):
        print("Numerele introduse sunt consecutive!")
    else:
        print("Numerele introduse nu sunt consecutive!")

def ex4():
    x = int(input("Introdu un numar intreg: "))
    if x%2==0:
        print("Numarul introdus este par!")
    else:
        print("Numarul introdus nu este par!")

def ex5():
    x = int(input("Introdu valoarea lui x: "))
    if x>0:
        aria = 4*math.pi*(x**2)
        volum = (4*math.pi*(x**3)) / 3
        print(f"Aria sferei este [{aria:.2f}], iar volumul [{volum:.2f}]")
    else:
        print("Numarul introdus nu reprezinta o raza a sferei.")

def ex6():
    valori = input("Introdu doua valori intregi, separate prin spatiu: ")
    a, b = valori.split()
    a = int(a) 
    b = int(b)
    if a>b:
        maxx = a
        minn = b
    elif b>a:
        maxx = b
        minn = a
    print(f"Maximul dintre cele doua numere este [{maxx}], iar minimul [{minn}]")
    
def ex7():
    x = int(input("Introdu o valoare pentru x: "))
    interval = input("Introdu cele doua numere pentru interval, separate prin spatiu: ")
    a, b = interval.split()
    a = int(a)
    b = int(b)
    if a<x and x<b:
        print(f"Numarul [{x}] se afla in intervalul ({a}, {b})!")
    else:
        print(f"Numarul [{x}] nu se afla in intervalul ({a}, {b})!")

def ex8():
    valori = input("Introdu trei numere intregi, separate prin spatiu: ")
    a, b, c = valori.split()
    a = int(a)
    b = int(b)
    c = int(c)

    maxx = a
    minn = a

    if b>maxx: maxx = b
    if c>maxx: maxx = c

    if b<minn: minn = b
    if c<minn: minn = c

    list = [a, b, c]
    list.sort()

    print(f"Maximul dintre cele trei numere este [{maxx}], iar valoarea minima [{minn}]\n"
          "Ordinea crescatoare a numerelor este: ", list[0], list[1], list[2]
          )
def ex9():
    coordonate = input("Introdu coordonatele pentru axa X si Y, separate prin spatiu: ")
    x, y = coordonate.split()
    x = int(x)
    y = int(y)

    if x>0 and y>0:
        print("Coordonatele introduse se afla in cadranul 1!")
    elif x<0 and y>0:
        print("Coordonatele introduse se afla in al doilea cadran!")
    elif x<0 and y<0:
        print("Coordonatele introduse se afla in cel de-al treilea cadran!")
    elif x>0 and y<0:
        print("Coordonatele introduse sunt in cel de-al patrulea cadran!")

def main():
    menu = {
        1: ex1,
        2: ex2,
        3: ex3,
        4: ex4,
        5: ex5,
        6: ex6,
        7: ex7,
        8: ex8,
        9: ex9,
        0: exit
    }
    while True:
        print("\n" + "━" * 10 + " <[MENIU]> " + "━" * 10 + "\n"
                "1. Exercitiul 1\n"
                "2. Exercitiul 2\n"
                "3. Exercitiul 3\n"
                "4. Exercitiul 4\n"
                "5. Exercitiul 5\n"
                "6. Exercitiul 6\n"
                "7. Exercitiul 7\n"
                "8. Exercitiul 8\n"
                "9. Exercitiul 9\n"
                "0. Iesire program\n\n"
                "Optiunea dumneavoastra: ", end ="", flush=True
              )
        choice = int(getch.getch())
        print(choice)

        if choice in menu:
            menu[choice]()
        else:
            print("Optiune invalida, incearca din nou!")


if __name__ == '__main__':
    main()