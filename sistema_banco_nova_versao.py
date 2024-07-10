def menu():
    menu="""
    Bem vindo(a)!\n
    ==== MENU ====\n
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Cadastrar_usuario
    [5] Abrir_conta
    [0] Sair\n 
    ============
    => """
    return input(menu)

def depositar (saldo,valor,extrato,/):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato    

def sacar (*,saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    
    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= LIMITE_SAQUES # type: ignore

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques diários excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print ("Saque realizado com sucesso!")

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato
       
def extrato (saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


def cadastrar_usuario (usuarios):
    cpf = input("Informe o seu CPF (somente números): ")
    usuario= filtrar_usuarios(cpf, usuarios)
    
    if usuario:
        print( "Você já é cliente do nosso banco!")
        return
    
    nome = input("Informe seu nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input ("Informe o endereço (logradouro, n° - bairro, cidade/sigla estado): )")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print ("""Usuário cadastrado com sucesso!\n
          Agradecemos pela preferência!""")

def filtrar_usuarios (cpf,usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados [0] if usuarios_filtrados else None


def abrir_conta (agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("Erro! Usuário nao encontrado.")
    return None
    
def main( ):
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = " "
    numero_saques = 0
    usuarios = [ ]
    contas = [ ]
    numero_conta = 1

    while True:
        opcao = menu ( )

        if opcao == "1":
            valor = float (input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)
        
        elif opcao == "2":
            valor = float (input ("Informe o valor do saque: "))
        
            saldo, extrato = sacar(
                saldo=saldo,
                valor= valor,
                extrato= extrato,
                numero_saques= numero_saques,
                limite= limite,
                limite_saques= LIMITE_SAQUES, 
            )
         
        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato) # type: ignore

        elif opcao == "4":
            cadastrar_usuario(usuarios)

        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = abrir_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
                numero_conta += 1

        elif opcao == "0":
            break
      
        else:
            print("Operação inválida.")
         
main ( )