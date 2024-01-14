# Old Style %
# string_2


#nome = "Zenaldo"
#idade = 35
#profissao = "Programador"
#linguagem = "Python"
#saldo = 50.456
#dados = {"nome": "zenaldo", "idade": 35} 

#print("nome: %s Idade: %d" % (nome, idade))
#print("nome: {} idade: {}".format(nome, idade))
#print("nome: {1} idade: {0}".format(idade, nome))
#print("nome: {1} idade: {0} nome: {1} {1}".format(idade, nome))
#print("nome: {nome} idade: {idade}".format(nome=nome, idade=idade))
#print("nome: {nome} idade: {age} {nome} {nome} {age}".format(age=idade, nome=nome))
#rint("nome: {nome} idade: {idade}".format(**dados))

#print(f"nome: {nome} idade: {idade} saldo: {saldo:.1f}")





#profissao = "Programador"
#linguagem = "Python"


#print("nome: %s Idade: %d" % (nome, idade))
#print("nome: {} idade: {}".format(nome, idade))
#print("nome: {1} idade: {0}".format(idade, nome))

# Ler a variável de entrada como uma string
# Dicionário de meses em inglês
# Entrada do mês fornecida pelo usuário
# Dicionário de meses em inglês

# Ler um valor inteiro entre 1 e 12
# Dicionário de meses em inglês
# Dicionário de meses em inglês



# Lista de meses em inglês


#projet de um sistema bancario 

menu = """
[d] Depositar
[s] Sacar 
[e] Extrato 
[q] Sair 

=>"""

saldo = 0
limite = 500
cheque_especial = 1000
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > (saldo + cheque_especial)
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUE

        if excedeu_saldo:
            print("Operação falhou! Saldo insuficiente, incluindo cheque especial.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            if valor > saldo:
                # Se o valor do saque exceder o saldo, utiliza o cheque especial
                saldo -= valor
                extrato += f"Saque (Cheque Especial): R$ {valor:.2f}\n"
                cheque_especial += saldo  # Atualiza o cheque especial
                saldo = 0
            else:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n===================EXTRATO =======================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print(f"Cheque Especial: R$ {cheque_especial:.2f}")
        print("=====================================================")

    elif opcao == "q":
        break
    else:
        print("Operação inválida. Por favor, selecione novamente a operação desejada.")
