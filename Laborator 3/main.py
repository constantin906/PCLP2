n=int(input("Introduceti o valoare pentru n: "))
# Exercitiul 2, punctul a

for i in range(n, -1, -1):
    print(i, end=" ")

# Punctul b

print("Numerele impare din intervalul (0, n] sunt: ", end="", flush=True)

for i in range(0, n+1):
    if i%2!=0:
        print(i, end=" ")

# Punctul c

produs = 1

for i in range(1, n+1):
    produs*=i

print(f"Produsul primelor {n} numere este: {produs}")

# Punctul d

x = int(input("Introdu numarul cu care sa verifici divizibilitatea: "))

sum = 0

for i in range(1, n+1):
    if i%x==0:
        sum+=i
print(f"Suma numerelor din intervalul (0, {n}], divizibile cu {x} este: {sum}")


# Exercitiul 3

sum = 0
cifra = 0
for i in range(n):
    cifra = n%10
    sum+=cifra
    n//=10
print(f"Suma cifrelor numarului {n} este: {sum}")


# Exercitiul 4

for i in range(1, n+1):
    print("*" * i)

for i in range(n-1, 0, -1):
    print("*" * i)


''' CONDITIA WHILE '''

# Exercitiul 1

nr = input("Introdu un sir de numere, separate prin spatiu: ")
lista = [int(x) for x in nr.split()]

suma = 0
i = 0

while i<len(lista):
    suma+=lista[i]
    i+=1
print(f"Suma numerelor introduse este: {suma}")


# Exercitiul 2

n = int(input("Introdu o valoare pentru n: "))
reverse = 0 
while n>0:
    ultima_cifra = n%10
    reverse = reverse*10+ultima_cifra
    n//=10
    print(n)
print(f"Reversul numarului este: {reverse}")


# Exercitiul 3 (p(x)=3x^2-7x-10)


x = int(input("Introdu valoarea lui x: "))
i = 1

while i<=x:
    p = 3*(i**2)-7*i-10
    print(f"p({i}) = 3*({i}^2)-7*{i}-10 = {p}")
    i+=1


''' MENIU '''

while True:
    print("━" * 10 + " <[MENIU]> " + "━" * 10 + "\n"
          "[C]. Citire\n"
          "[+]. Adunare\n"
          "[-]. Scadere\n"
          "[*]. Inmultire\n"
          "[/]. Impartire\n"
          "[X]. Iesire\n"
          )
    meniu = input("Optiunea dumnveavoastra: ")
    match meniu.split():
        case ["C", "c"]:
            valori = input("Introdu doua numere intregi, separate prin spatiu: ")
            x, y = valori.split()
            x = int(x)
            y = int(y)
        case ["+"]:
            print(f"Suma numerelor {x} si {y} este: ", x+y)
        case ["-"]:
            print(f"Diferenta celor doua numere {x} si {y} este: ", x-y)
        case ["*"]:
            print(f"Produsul celor doua numere {x} si {y} este: ", x*y)
        case["/"]:
            print(f"Rezultatul in urma impartirii numerelor {x} si {y} este: ", x/y)
        case ["X"]:
            exit(0)

