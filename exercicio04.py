vidade = 0
vpeso = 0
vhoras =0

print("Olá, abaixo está um teste para ver se voce pode mesmo ser um doador,só basta verificar os requisitos! " )
idade=(int(input("Informe sua idade: ")))
peso=(float(input("Informe seu peso: ")))
horas=(int(input("Quantas horas voce dormiu na ultima noite? - ")))

if idade>=16 and idade<=69:
    vidade+=1
else:
    print("Idade fora dos requisitos!")
if peso>50:
    vpeso+=1
else:
    print("Peso fora dos requisitos!")
if horas>=6:
   vhoras+=1
else:
    print("Horas de sono fora dos requisitos!")
if vidade == 1 and vpeso == 1 and vhoras == 1:
    print("Você pode ser um doador!")
else:
    print("Você não pode ser um doador.")

 