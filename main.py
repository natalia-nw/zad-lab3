# zad 1
A = [1-x for x in range(1, 11)]
print(A)

B = [4**i for i in range(0, 8)]
print(B)

C = [x for x in B if x % 2 == 0]
print(C)

print("\n")

# zad 2
import random
lista1 = [random.randint(1, 100) for _ in range(10)]
nowa_lista = [x for x in lista1 if x % 2 == 0]
print(nowa_lista)

print("\n")

# zad 3
produkty = {"kawa": "kg", "bułki": "sztuki", "sok": "l"}
produkty2 = {key: value for value, key in produkty.items()}
print(produkty2)

print("\n")

# zad 4
def czy_prostokatny(a,b,c):
    if (a**2) + (b**2) == (c**2):
        return "tak, trójkąt jest protokątny"
    else:
        return "trójkąt nie jest prostokątny"

print(czy_prostokatny(3,4,5))

print("\n")

# zad 5
def pole_trapezu(a=2,b=3,h=5):
    p = ((a+b)*h)/2
    return p

print(pole_trapezu())

print("\n")

# zad 6
def ciag(a=1, b=4, ile=10):
    for x in range(a, ile):
        print(x*b)

ciag()

print("\n")

# zad 7
def funkcja(*liczby):
    if len(liczby) != 3:
        print('Podaj trzy liczby ')
        return -1
    for x in range(liczby[0], liczby[2]):
        print(x * liczby[1])

funkcja(1, 5, 4)

print("\n")

# zad 8
def licz(**a):
    return len(a.items()), sum(x for x in a.values())

print(licz(sok=5, kurczak=17, ryż=7))
