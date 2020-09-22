vidade = 0
vpeso = 0
vhoras =0
print("Olá, abaixo está um teste para ver se voce pode mesmo ser um doador,só basta verificar os requisitos! " )
idade=(int(input("Qual a sua idade? - ")))
peso=(float(input("Qual o seu peso? - ")))
horas=(int(input( "Quantas horas voce dormiu na ultima noite? - ")))

if idade>=16 and idade<=69:
    vidade+=1
else:
    print("Voce nao tem idade a idade necessaria!")
if peso>50:
    vpeso+=1
else:
    print("Seu peso esta fora dos requisitos!")
if horas>=6:
    vhoras+=1
else:
    print("Horas de sono fora dos requisitos!")
if vidade == 1 and vpeso == 1 and vhoras == 1:
    print("Você pode ser um doador!")
    cadastro=(int(input("Deseja se cadastrar?  Digite 1 para Sim ou 2 para Não:")))
    if cadastro == 1:
        doador1={"Nome:":"","CPF:":"","Senha:":"", "Apto para doar:":""}
        doador2={"Nome:":"","CPF:":"","Senha:":"", "Apto para doar:":""}
        doador3={"Nome:":"","CPF:":"","Senha:":"", "Apto para doar:":""}
        doador4={"Nome:":"","CPF:":"","Senha:":"", "Apto para doar:":""}
        doador5={"Nome:":"","CPF:":"","Senha:":"", "Apto para doar:":""}
        
        doador1["Nome:"] = "Victor Bonomi"
        doador1["CPF:"] = "092.478.225-15"
        doador1["Senha:"]= "bonomi234"
        doador1["Apto para doar:"]= "Sim"
         

        doador2["Nome:"] = "Julia Barbosa"
        doador2["CPF:"] = "153.472.330-73"
        doador2["Senha:"]= "mikix123"
        doador2["Apto para doar:"]= "Não"

        doador3["Nome:"] = "Guilherme Agostinho"
        doador3["CPF:"] = "179.930.537-54"
        doador3["Senha:"]= "cacadordegamba123"
        doador3["Apto para doar:"]= "Não"

        doador4["Nome:"] = "Brian Tomasi"
        doador4["CPF:"] = "410.548.937-61"
        doador4["Senha:"]= "19072003"
        doador4["Apto para doar:"]= "Sim"

        doador5["Nome:"] = "Nathan Dias"
        doador5["CPF:"] = "247.679.405-15"
        doador5["Senha:"]= "panda123"
        doador5["Apto para doar:"]= "Sim"

        for x in doador1:
            print(x, doador1[x])
            print("Cadastro concluido!")
             
        for x in doador2:
            print(x, doador2[x])
            print("Cadastro concluido!")
             
        for x in doador3:
            print(x, doador3[x])
            print("Cadastro concluido!")
              
        for x in doador4:
            print(x, doador4[x])
            print("Cadastro concluido!")
              
        for x in doador5:
            print(x, doador5[x])
            print("Cadastro concluido!")
              
    if cadastro == 2:
        print("Cadastro recusado!")

else:
    print("Você não pode ser um doador.")