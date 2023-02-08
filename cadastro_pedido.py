import lib
import cadastro_cliente
import uuid
import connection_factory as cf

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
    pedido = {}

    pedido["id"] = str(uuid.uuid4())
    pedido["cliente_id"] = cadastro_cliente.localiza_cliente()
    pedido["produto"] = input("Digite o nome do produto: ")
    pedido["quantidade"] = input("Digite a quantidade: ")
    pedido["valor"] = input("Digite o valor: ")
    pedido["valor_total"] = float(pedido["quantidade"]) * float(pedido["valor"])

    cf.cursor.execute('''
        INSERT INTO pedidos (id, cliente_id, produto, quantidade, valor)
        VALUES (?, ?, ?, ?, ?);
    ''', (pedido["id"], str(pedido["cliente_id"]), pedido["produto"], pedido["quantidade"], pedido["valor"]))

    print("Ocorreu algum erro relacionado ao banco de dados...")

    cf.cursor.commit()
    print("-" * 100)
    lib.mensagem("Pedido cadastrado com sucesso!")
    print("-" * 100)