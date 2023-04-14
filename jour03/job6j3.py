chaine = "abcdefghijklmnopqrstuvwxyz" * 10

i=1

while i <= len(chaine):
    print(chaine[:i])

    chaine=chaine[i:]

    i+=1

