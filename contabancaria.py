
#--------> Variaveis iniciais <---------#

menu = """

    ==========MENU==========

    [1] Depósito
    [2] Saque
    [3] Extrato
    [4] Sair

    ========================
"""

saldo= 0
limite= 500
extrato= ""
quantidade_saques=0
LIMITE_SAQUES=3

#----------> Iniciandos tarefas <-------------#

while True:
    
    escolha=input(menu)

    if escolha == "1":
        valorD = float(input('Informe o valor desejado para depósito: '))

        if valorD > 0:
            saldo += valorD
            extrato += f"Deposito realizado no valor de: R$ {valorD:.2f}\n"

        else:
            print('O valor informado é inválido')

    elif escolha == "2":
        valorS = float(input('informe o valor desejado para saque: '))

        estourou_saldo = valorS > saldo
        estourou_limite = valorS > limite
        estourou_saques = quantidade_saques >= LIMITE_SAQUES


        if estourou_saldo:
            print('O valor desejado excede o saldo atual')
        elif estourou_limite:
            print('o valor desejado excede o valor de limite diário para saque.')
        elif estourou_saques:
            print('você excedeu o número de saques diários')
        
        elif valorS > 0:
            saldo -= valorS
            extrato += f"Saque realizado no valor de: R$ {valorS:.2f}\n"
            quantidade_saques += 1
        else:
            print('Operação não pode ser concluída! O valor informado para saque é inaválido..')


    elif escolha=="3":
        extratotxt= 'Nenhuma movimentação realizada.' if not extrato else extrato
        print('==========EXTRATO==========\n')
        print(extratotxt)
        print(f'Saldo atual: R$ {saldo: .2f}')
        print('\n===========================')

    elif escolha=="4":
        print('Oobrigado por utilizar nossos serviços. Estamos sempre a disposição =]')
        break

    else:
        print('A opção escolhida é inválida')

        


        
    


        















