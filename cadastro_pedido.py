import lib
import csv_sistema
import cadastro_cliente
import uuid

nome_do_arquivo = "pedidos.csv"

def listar():
    lib.limpar_tela();
    lista = csv_sistema.ler(nome_do_arquivo)
    print("-" * 60)
    for item in lista:
        print("Id: " + item["id"])
        cliente = csv_sistema.busca_por_id(item["cliente_id"], "clientes.csv")
        print("Cliente: " + cliente["nome"])
        print("Quantidade: " + item["quantidade"])
        print("Valor da unidade: R$" + item["valor"])
        print("Valor Total: R$" + item["valor_total"])
        print("-" * 60)

    input("Digite enter para continuar ...")
    lib.limpar_tela()
    
def cadastrar():
    lib.limpar_tela()

    cliente = cadastro_cliente.localiza_cliente()

    pedido = {}
    pedido["id"] = str(uuid.uuid4())
    pedido["cliente_id"] = cliente["id"]
    pedido["produto"] = input("Digite o nome do produto: ")
    pedido["quantidade"] = input("Digite a quantidade: ")
    pedido["valor"] = input("Digite o valor: ")
    pedido["valor_total"] = float(pedido["quantidade"]) * float(pedido["valor"])

    lista = csv_sistema.ler(nome_do_arquivo)
    lista.append(pedido)
    csv_sistema.salvar(lista, nome_do_arquivo)
    lib.mensagem("Pedido cadastrado com sucesso!")