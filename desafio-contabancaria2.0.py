# Variáveis iniciais
menu = """
========== MENU ==========
[1] Depósito
[2] Saque
[3] Extrato
[4] Criar Conta
[5] Criar Usuario
[6] Listar usuarios
[7] Sair
========================
"""


def depositar(saldo, valorD, extrato ): 
        if valorD > 0:
            saldo += valorD
            extrato += f"Depósito realizado no valor de: R$ {valorD:.2f}\n"
            t_extrato.append(extrato)
        else:
            print('O valor informado é inválido')

        return saldo, extrato

def sacar(*, saldo, valorS, extrato, limite, quantidade_saques, limite_saques): 
        estourou_saldo = valorS > saldo
        estourou_limite = valorS > limite
        estourou_saques = quantidade_saques >= limite_saques

        if estourou_saldo:
            print('Saldo insuficiente para saque no valor desejado.')
        elif estourou_limite:
            print('O valor desejado excede o limite diário para saque.')
        elif estourou_saques:
            print('Você excedeu o número de saques diários.')
        elif valorS > 0:
            saldo -= valorS
            extrato += f"Saque realizado no valor de: R$ {valorS:.2f}\n"
            t_extrato.append(extrato)
            quantidade_saques += 1
        else:
            print('Operação não pode ser concluída! O valor informado para saque é inválido.')

        return saldo, extrato, quantidade_saques

def extrato_exibicao( saldo, /, *, extrato):
            
        print('========== EXTRATO ==========')
        print ('Nenhuma movimentação realizada.' if not extrato else extrato)       
        for d in t_extrato:
            print('->', d,end='')
        print(f"\nSaldo atual: R$ {saldo:.2f}")    
        print('=============================')  

        return saldo, extrato  

def criar_usuario(usuarios):
     cpf= input('Informe seu CPF(apenas números): ')
     usuario= filtrar_usuarios(cpf,usuarios)
     
     if usuario:
          print('\n Já existe um usuário registrado com o mesmo CPF! ')
          return
     
     nome = input('Insira o nome completo: ')
     data_nasc = input('Insira sua datat de nascimento (dd-mm-aaaa): ')
     endereco = input('Informe seu endereço á seguir(ex : logradouro, num - bairro - cidade-SP): ')

     usuarios.append({ 'cpf': cpf, 'nome': nome, 'data_nasc': data_nasc,'endereco': endereco})
     
     print('Usuário criada com sucesso! =]')


def filtrar_usuarios(cpf, usuarios):
    usuarios_filt = [usuario for usuario in usuarios if usuario['cpf']==cpf]
    return usuarios_filt[0] if usuarios_filt else None


def criar_conta(agencia, numero_conta, usuarios):
     cpf = input('Insira seu CPF: ')
     usuario= filtrar_usuarios(cpf, usuarios)

     if usuario:
        print('Conta criada com sucesso ! =]')
        return{'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}
      
     print('Usuario não encontrado, operação encerrada')

def listar_contatos(contas):
     for conta in contas:
        linha = f"""
        Agência:\t{conta['agencia']}
        C/C:\t\t{conta['numero_conta']}
        Titular:\t{conta['usuario']['nome']}
        """
        print('=' * 100)
        print(linha)




saldo = 0
limite = 500
extrato = ''
quantidade_saques = 0
usuarios=[]
contas=[]
LIMITE_SAQUES = 3
AGENCIA='0001'
t_extrato = list()

# Iniciando tarefas
while True:
    escolha = input(menu)

    if escolha == "1":
        valorD = float(input('Informe o valor desejado para depósito: '))
        
        saldo, extrato = depositar(saldo, valorD, extrato)


    elif escolha == "2":
        valorS = float(input('Informe o valor desejado para saque: '))
        saldo, extrato,quantidade_saques = sacar( saldo= saldo, valorS= valorS, extrato= extrato,
                    limite = limite, quantidade_saques = quantidade_saques, limite_saques= LIMITE_SAQUES)
    elif escolha == "3":
        extrato_exibicao(saldo, extrato=extrato)

    elif escolha == "4":
        numero_conta=len(contas) + 1
        conta = criar_conta(AGENCIA, numero_conta, usuarios)
        
        if conta:
             contas.append(conta)

    elif escolha == "5":
         criar_usuario(usuarios)

    elif escolha == "6":
        
        listar_contatos(contas)

    elif escolha == "7":
        print('Obrigado por utilizar nossos serviços. Estamos sempre à disposição :)')
        break

    else:
        print('A opção escolhida é inválida')


