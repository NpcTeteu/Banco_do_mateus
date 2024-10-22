import time
import sys

def animacao_de_digitacao(texto, delay=0.05):
    for caractere in texto:
        sys.stdout.write(caractere)
        sys.stdout.flush()
        time.sleep(delay)
    print()

class Pessoa:
    def __init__(self, nome="", sobrenome="", sexo="", idade=0, cidade="", estado=""):
        self.nome = nome
        self.sobrenome = sobrenome
        self.sexo = sexo
        self.idade = idade
        self.cidade = cidade
        self.estado = estado

    def info(self):
        print('------INFORMAÇÕES DO USUARIO------')
        animacao_de_digitacao(f'Nome: {self.nome} {self.sobrenome}')
        animacao_de_digitacao(f'Sexo: {self.sexo}')
        animacao_de_digitacao(f'Idade: {self.idade}')
        animacao_de_digitacao(f'Cidade: {self.cidade} de {self.estado}')
        print('----------------------------------')
        animacao_de_digitacao('')

    def cadastrar_usuario(self):
        while True:
            self.nome = input('Digite seu primeiro nome: ')
            if self.nome.isalpha():
                animacao_de_digitacao("Entrada Valida")
                break
            else:
                animacao_de_digitacao('Entrada Invalida, por favor digite apenas letras')

        while True:
            self.sobrenome = input('Agora seu sobrenome: ')
            if self.sobrenome.replace(" ","").isalpha():
                animacao_de_digitacao('Entrada Valida')
                break
            else:
                animacao_de_digitacao('Entrada Invalida, por favor digite apenas letras')
                
        while True:
            self.sexo = input('Sexo: Masculino/Feminino: ').lower()
            if self.sexo in ['masculino', 'feminino']:
                animacao_de_digitacao('Entrada Valida')
                break
            else:
                animacao_de_digitacao('Entrada invalida, por favor digite uma das duas opcoes')
                
        while True:
            self.idade = input('Idade: ')
            if self.idade.isdigit():
                animacao_de_digitacao('Entrada Valida')
                break
            else:
                animacao_de_digitacao('Entrada invalida, por favor digite apenas numeros')

        while True:
            self.cidade = input('Cidade: ')
            if self.cidade.replace(" ",'').isalpha():
                animacao_de_digitacao("Entrada Valida")
                break
            else:
                animacao_de_digitacao('Entrada Invalida, por favor digite apenas letras')

        while True:
            self.estado = input('Estado: ')
            if self.estado.replace(" ","").isalpha():
                animacao_de_digitacao("Entrada Valida")
                break
            else:
                animacao_de_digitacao('Entrada Invalida, por favor digite apenas letras')

class Conta:
    def __init__(self, pessoa, banco=None, saldo=0):
        self.pessoa = pessoa
        self.banco = banco
        self.saldo = saldo
        self.senha_usuario = None
        self.bloqueada = False
        self.operacoes_dia = 0
        self.tentativas_senha = 0

    def set_banco(self):
        bancos_disponiveis = {
            'Banco1': 'Santander',
            'Banco2': 'Itaú',
            'Banco3': 'Caixa',
            'Banco4': 'Nubank',
            'Banco5': 'Sicredi'
        }

        animacao_de_digitacao("Bancos disponíveis:")
        for valor in bancos_disponiveis.values():
            animacao_de_digitacao(f"- {valor}")

        while True:
            novo_banco = input('Digite o nome do banco desejado: ')
            if novo_banco in bancos_disponiveis.values():
                self.banco = novo_banco
                animacao_de_digitacao(f"Banco atualizado para {novo_banco}")
                break
            else:
                animacao_de_digitacao("Banco não encontrado. Por favor, escolha um dos bancos disponíveis:")
                for valor in bancos_disponiveis.values():
                    animacao_de_digitacao(f"- {valor}")

    class Senha:
        def __init__(self, palavra_chave, numeros):
            self.palavra_chave = palavra_chave
            self.numeros = numeros

        def misturador(self):
            numeros_str = ''.join(map(str, self.numeros))
            nova_senha = self.palavra_chave + numeros_str
            return nova_senha

    def criar_senha(self):
        animacao_de_digitacao('Vamos criar sua senha')
        palavra_chave = input('Coloque uma palavra de qualquer: ')
        numeros = list(map(int, input('Agora quero que digite 3 numeros aleatórios separados por espaço: ').split()))

        senha = self.Senha(palavra_chave, numeros)
        self.senha_usuario = senha.misturador()
        animacao_de_digitacao('Senha criada com sucesso.')

    def mostrar_senha(self):
        print(f'Sua senha agora é {self.senha_usuario}')

    def verificar_senha(self):
        verificação = input('Digite a sua senha: ')
        if verificação == self.senha_usuario:
            self.tentativas_senha = 0
            return True
        else:
            animacao_de_digitacao('Senha incorreta')
            self.tentativas_senha += 1
            if self.tentativas_senha >= 3:
                animacao_de_digitacao('Conta bloqueada após 3 tentativas incorretas.')
                self.bloqueada = True
            return False

    def verificar_limite_operacoes(self):
        if self.operacoes_dia >= 4:
            animacao_de_digitacao('Limite de operações atingido para hoje.')
            return False
        return True

    def depositar(self):
        if self.bloqueada:
            animacao_de_digitacao('Operação não permitida. Conta bloqueada.')
            return

        if not self.verificar_limite_operacoes():
            return

        try:
            deposito = int(input('Qual o valor do seu depósito: '))
        except ValueError:
            animacao_de_digitacao("Por favor, insira um valor numérico válido.")
            return

        if self.verificar_senha():
            self.saldo += deposito
            self.operacoes_dia += 1
            animacao_de_digitacao('Depósito realizado com sucesso.')
            animacao_de_digitacao(f'Seu novo saldo é: R${self.saldo}')
        else:
            animacao_de_digitacao('Depósito não realizado.')

    def sacar(self):
        if self.bloqueada:
            animacao_de_digitacao('Operação não permitida. Conta bloqueada.')
            return

        if not self.verificar_limite_operacoes():
            return

        try:
            saque = int(input('Qual valor você deseja sacar: '))
        except ValueError:
            animacao_de_digitacao("Por favor, insira um valor numérico válido.")
            return

        if saque > self.saldo:
            animacao_de_digitacao('Não é possível sacar esse valor. Saldo insuficiente.')
            return

        if self.verificar_senha():
            self.saldo -= saque
            self.operacoes_dia += 1
            animacao_de_digitacao('Saque realizado com sucesso.')
            animacao_de_digitacao(f'Seu novo saldo é: R${self.saldo}')
        else:
            animacao_de_digitacao('Saque não realizado.')

    def realizar_operacao(self):
        while True:
            decisao = input("Deseja continuar fazer alguma ação? S/N: ").upper()
            if decisao == "S":
                decisao2 = input("Deseja fazer o quê: SACAR - DEPOSITAR: ").upper()
                if decisao2 == "SACAR":
                    self.sacar()
                elif decisao2 == "DEPOSITAR":
                    self.depositar()
                else:
                    animacao_de_digitacao("Operação inválida.")
            elif decisao == "N":
                print("Tenha um bom dia!")
                break
            else:
                animacao_de_digitacao("Entrada inválida, por favor responda com S ou N.")

pessoa1 = Pessoa()
pessoa1.cadastrar_usuario()
pessoa1.info()

conta1 = Conta(pessoa1)
conta1.set_banco()
conta1.criar_senha()
conta1.mostrar_senha()
conta1.realizar_operacao()