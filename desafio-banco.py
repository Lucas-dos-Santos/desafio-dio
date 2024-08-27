menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
[c] cadastar  usuario
[m] mostra usuarios

=> """


limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
usuarios =  []

def usuario():
    if len(usuarios) == 0:
        print('não existe usuarios cadastrados')
    else:
       for usuario in usuarios:
            print(f"\nNome: {usuario['nome']}, CPF: {usuario['cpf']}, Conta: {usuario['conta']}, Saldo: R$ {usuario['saldo']:.2f}, ")
        

    
def sacar(valor):
    for usuario in usuarios:
            if usuario['conta'] == conta:
                if valor > usuario['saldo']:
                    print(f'Saldo insuficiente. Seu saldo atual é R$ {usuario["saldo"]:.2f}')
                elif usuario['numero_saques'] >= LIMITE_SAQUES:
                    print("Operação falhou! Número máximo de saques excedido.")
                elif valor > limite:
                    print(f'Valor do saque excede o limite de R$ {limite:.2f}.')
                else:
                    usuario['saldo'] -= valor
                    usuario['numero_saques'] += 1
                    usuario['extrato'].append(f"Saque de R$ {valor:.2f}")
                    print('Saque realizado com sucesso!')
                return
    print('Conta não encontrada.')
        
def extrato(conta):
    for usuario in usuarios:
        if usuario['conta'] == conta:
            print("\n================ EXTRATO ================")
            if not usuario['extrato']:
                print("Não foram realizadas movimentações.")
            else:
                for movimento in usuario['extrato']:
                    print(movimento)
            print(f"\nNome: {usuario['nome']}, CPF: {usuario['cpf']}, Conta: {usuario['conta']}, Saldo: R$ {usuario['saldo']:.2f}")
            print("==========================================")
            return
    print("Conta não encontrada.")

def extrato_geral():
    print("\n================ EXTRATO GERAL ================")
    if not usuarios:
        print("Nenhum usuário cadastrado.")
    else:
        for usuario in usuarios:
            print(f"\nUsuário: {usuario['nome']}, Conta: {usuario['conta']}")
            if not usuario['extrato']:
                print("  Não foram realizadas movimentações.")
            else:
                for movimento in usuario['extrato']:
                    print(f"  {movimento}")
            print(f"  Saldo atual: R$ {usuario['saldo']:.2f}")
    print("===============================================")
    
def deposito(valor):
    if valor > 0:
        for usuario in usuarios:
            if usuario['conta'] == conta:
                usuario['saldo'] += valor
                usuario['extrato'].append(f"Depósito de R$ {valor:.2f}")
                print('deposito feito com sucesso')
                return
        print('Conta não encontrada.')
    else:
        print('Valor de depósito inválido.')


def criauser():
    nome = input('digite seu nome:')
    cpf = input('digite seu cpf')
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print('CPF já cadastrado')
            return
    if len(usuarios) == 0:
        numero_conta = '0001'
    else:
        ultimo_numero_conta = int(usuarios[-1]['conta'])
        numero_conta = f'{ultimo_numero_conta + 1:04}'

    # Adiciona o novo usuário à lista de usuários
    novo_usuario = {'nome': nome, 'cpf': cpf, 'conta': numero_conta, 'saldo': 0.0, 'extrato': [], 'numero_saques': 0}
    usuarios.append(novo_usuario)

    print('Usuário cadastrado com sucesso!')
    
while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        conta = input("digite o numero da conta")
        deposito(valor)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
         conta = input("digite o numero da conta")
        sacar(valor)

    elif opcao == "e":
        conta = input("digite o numero da conta")
        extrato(conta)
    
    elif opcao == "m":
        usuario()
        
    elif opcao == "c":
        criauser()
        
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
