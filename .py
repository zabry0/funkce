def obvod(a, b, c):
    vysledek = a + b + c
    return vysledek

strana_a = input("Zadejte délku strany a: ")
strana_b = input("Zadejte délku strany b: ")
strana_c = input("Zadejte délku strany c: ")

strana_a = int(strana_a)
strana_b = int(strana_b)
strana_c = int(strana_c)

obvod_trojuhelniku = obvod(strana_a, strana_b, strana_c)

print("Obvod trojúhelníku je:", obvod_trojuhelniku)


def obsah_trojuhelniku(a, b):
    vysledek = (0.5 * a * b)
    return vysledek

strana_a = input("Zadejte délku základny trojúhelníku: ")
strana_b = input("Zadejte délku výšky trojúhelníku: ")

strana_a = int(strana_a)
strana_b = int(strana_b)

obsah = obsah_trojuhelniku(strana_a, strana_b)

print("Obsah trojúhelníku je:", obsah)
