print("Este programa serve para calcular combinações!")

#formar n de elementos
n = int(input("Digite o número de elementos em quastão: "))

#formar seleções de p à p
p = int(input("Digite o tamanho dos grupos de elementos que deseja formar: "))

#calcular n!
n1 = 1
resultadon1 = 1

while n1 <= n:
    resultadon1 *= n1
    n1 += 1
#resultado n1

#calcular p!
p1 = 1
resultadop1 = 1

while p1 <= p:
    resultadop1 *= p1
    p1 += 1
#resultado p1

#calcular (n-p)!
np = (n - p)

np1 = 1
resultadonp = 1

while np1 <= np:
    resultadonp *= np1
    np1 += 1
#resultado np

#dividir e multiplicar
total = int(resultadon1/(resultadop1*resultadonp))
print(f"O total é: {total} combinações")

#fim :)