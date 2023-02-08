import lib
import csv_sistema
import uuid
import connection_factory as cf

nome_do_arquivo = "clientes.csv"

def localiza_cliente():
    lib.limpar_tela()
    lista = csv_sistema.ler(nome_do_arquivo)
    print("-" * 60)
    for idx, item in enumerate(lista):
        print("Indice: " + str(idx + 1))
        print("Nome: " + item["nome"])
        print("Telefone: " + item["telefone"])
        print("Email: " + item["email"])
        print("-" * 60)
    
    indice = input("Digite o indice de qual cliente você deseja selecionar: \n")
    cliente = lista[int(indice) - 1]
    if cliente == None:
        lib.mensagem("opção inválida")
        localiza_cliente()

    return cliente


def listar():
    lib.limpar_tela();
    lista = csv_sistema.ler(nome_do_arquivo)
    print("-" * 60)
    for item in lista:
        print("Id: " + item["id"])
        print("Nome: " + item["nome"])
        print("Telefone: " + item["telefone"])
        print("Email: " + item["email"])
        print("-" * 60)

    input("Digite 'Enter' para continuar ...")
    lib.limpar_tela()
    
def cadastrar():
    
    lib.limpar_tela()
    cliente = {}

    cliente["id"] = str(uuid.uuid4())

    cliente["nome"] = input("Digite o nome do cliente: ")

    cliente["telefone"] = input("Digite o telefone do cliente: ")

    cliente["email"] = input("Digite o email do cliente: ")

    cf.cursor.execute('''
        INSERT INTO clientes (id, nome, telefone, email)
        VALUES (?, ?, ?, ?);
    ''', (cliente["id"], cliente["nome"], cliente["telefone"], cliente["email"]))

    cf.cursor.commit()
    print("-" * 100)
    lib.mensagem("Cliente cadastrado com sucesso!")
    print("-" * 100)