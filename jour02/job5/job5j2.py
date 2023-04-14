def calcule(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1/num2
    else:
        print ("wrong operator")

print(calcule(12, "+", 5))
print(calcule(12, "-",5))
print(calcule(12, "*",5))
print(calcule(12,"/",5))
print(calcule(12,"%",5))



