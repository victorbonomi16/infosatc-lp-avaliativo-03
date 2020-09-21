 
iMulheres=0
iHomens=0
numMulheres=0
numHomens=0

for x in range(0,10):
    sexo=(input("Qual seu Sexo? (Digite F para Feminino ou M para Masculino): "))
    if sexo=="F":
         numMulheres=numMulheres+1
         iMulheres=iMulheres+(int(input("Qual sua idade? - ")))
    elif sexo=="M":
        numHomens=numHomens+1
        iHomens=iHomens+(int(input("Qual sua idade? -  ")))

mediaMulheres=(iMulheres/numMulheres)
mediaHomens=(iHomens/numHomens)
mediaGeral =(iMulheres+iHomens)/(numMulheres+numHomens)

print("A média de idade das mulheres é:",mediaMulheres)
print("A média de idade dos homens é:",mediaHomens)
print("A média de idade de todos  é:",mediaGeral)