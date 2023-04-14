def tapis(n): 
	# Le bord 
	bord="+" 
	for i in range(n+1): bord +="-" 
	bord+="+" 
  
	# La boucle d'affichage 
	print(bord) 
	for i in range(n+1): 
		tapis="" 
		for j in range(n-i): tapis+="#" 
		tapis+=" " 
		for j in range(i): tapis+="#" 
		print("|" + tapis + "|") 
	# for 
	print(bord) 
# tapis() 
  
tapis(10)