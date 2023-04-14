def triangle(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        print("Impossible de construire un triangle.")
    elif a == b == c:
        print("Triangle équilatéral.")
    elif a == b or a == c or b == c:
        if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            print("Triangle isocèle et rectangle.")
        else:
            print("Triangle isocèle.")
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("Triangle rectangle.")
    else:
        print("Triangle quelconque.")

triangle(5, 5, 5)
triangle(5, 2, 5)
triangle(2, 5, 5)
triangle(5, 3, 4)