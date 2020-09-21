meses = {
    1  : "Janeiro",
    2  : "Fevereiro",
    3  : "Março",
    4  : "Abril",
    5  : "Maio",
    6  : "Junho",
    7  : "Julho",
    8  : "Agosto",
    9  : "Setembro",
    10 : "Outubro",
    11 : "Novembro",
    12 : "Dezembro", 
}  
escolha = int(input("Qual o mês que voce deseja? Digite o numero de 1 a 12 de acordo com o mes escolhido. "))

if escolha in meses:
    print("O mês escolhido foi: ",meses.get(escolha))
else:
    print("Este mes nao existe, por favor tente novamente.")