def panier(type,saison):
    if type == "fruits" and saison == "hiver":
        print("orange, kiwi, mandarine")
    elif type == "fruits" and saison == "été":
        print("poire, fraises, cassis")
    elif type == "legume" and saison == "hiver":
        print("carotte, topinambour, endive")
    elif type == "legume" and saison == "été":
        print("artichaut, aubergine, navet")
    else:
        print("other")

panier("fruits","hiver")
panier("fruits","été")
panier("legume","hiver")
panier("legume","hiver")
panier("legume","automne")