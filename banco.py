import time

class Pessoa:

    def __init__(self,nome,sobrenome,sexo,idade,cidade,estado):

        self.nome = nome
        self.sobrenome = sobrenome
        self.sexo = sexo
        self.idade = idade
        self.cidade = cidade
        self.estado = estado

    def info (self):

        time.sleep(2)
        print("")
        print(f'nome: ',self.nome,self.sobrenome)
        time.sleep(2)
        print('Sexo: ',self.sexo)
        time.sleep(2)
        print('idade: ',self.idade)
        time.sleep(2)
        print('cidade: ',self.cidade,'de',self.estado)
        time.sleep(2)
        print('')

p1 = Pessoa ('Mateus','Almeida Duarte','Masculino',16,'Críciuma','Santa Catarina')
p1.info()


class Conta:
    def __init__(self, banco=None, saldo=0):
        self.banco = banco
        self.saldo = saldo
        self.senha_usuario = None

    def set_banco(self, novo_banco):
        bancos_disponiveis = {
            'Banco1': 'Santander',
            'Banco2': 'Itaú',
            'Banco3': 'Caixa',
            'Banco4': 'Nubank',
            'Banco5': 'Sicredi'
        }

        if novo_banco in bancos_disponiveis.values():
            self.banco = novo_banco
            time.sleep(2)
            print("Carregando...")
            print("")
            time.sleep(2)
            print(f"Agora seu banco é {novo_banco}")
            print('')
            time.sleep(2)
        else:
            print("Banco não encontrado. Escolha entre os bancos disponíveis:")
            for chave, valor in bancos_disponiveis.items():
                print(f"{chave}: {valor}")

    def criar_senha(self):
        time.sleep(2)
        self.senha_usuario = input('Crie uma senha para a sua conta: ')
        print("")
        time.sleep(2)
        print("Senha criada com sucesso.")
        print("")

    def depositar(self):
        time.sleep(2)
        deposito = int(input('Qual o valor do seu depósito: '))
        print("")
        time.sleep(2)
        verificação = input('Para continuar, digite a sua senha: ')
        print("")
        print("Carregando...")
        print("")
        time.sleep(2)

        if verificação == self.senha_usuario:
            self.saldo += deposito
            time.sleep(2)
            print('Depósito realizado com sucesso.')
            print("")
            time.sleep(2)
            print(f'Seu novo saldo é: R${self.saldo}')
            time.sleep(2)
        else:
            print("")
            print('Senha incorreta,por sua segurança sua conta foi banida por 3 dias')
            time.sleep(2)

    def sacar(self):
        print("")
        saque = int(input('Qual valor você deseja sacar: '))
        time.sleep(2)
        print("")
        verificação = input('Para continuar, digite a sua senha: ')
        print('')
        print('Carregando...')
        time.sleep(2)

        if saque > self.saldo:
            print("")
            print('Não é possivel sacar esse valor')
            time.sleep(2)
            print("")
            print('Operação cancelada, por segurança vamos banir sua conta por 3 dias')
            time.sleep(2)

        if self.saldo == 0:
            print('Não é possivel sacar, saldo = 0')
            time.sleep(2)

        if saque <= self.saldo and verificação:
            self.saldo -= saque
            print('Saque realizado com sucesso')
            time.sleep(2)
            print(f'Seu novo saldo é: R${self.saldo}')



conta1 = Conta ()
conta1.set_banco('Nubank')
conta1.criar_senha()
conta1.depositar()
conta1.sacar()