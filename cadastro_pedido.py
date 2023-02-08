import lib
import cadastro_cliente
import uuid
import connection_factory as cf

def listar():
    lib.limpar_tela();
    
    try:
        cf.cursor.execute('''SELECT * FROM pedidos''')
    except:
        print("Ocorreu algum erro relacionado ao banco de dados...")
    else:
        pedidos = cf.cursor.fetchall()
        print('-' * 70)
        for pedido in pedidos:
            print('ID: {} \nCLIENTE_ID: {} \nPRODUTO: {} \nQUANTIDADE: {} \nVALOR: {} \nVALOR TOTAL: {}'.format(*pedido))
            print('-' * 70)

    input("\nDigite 'Enter' para continuar ...")
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
        INSERT INTO pedidos (id, cliente_id, produto, quantidade, valor, valor_total)
        VALUES (?, ?, ?, ?, ?, ?);
    ''', (pedido["id"], str(pedido["cliente_id"]), pedido["produto"], pedido["quantidade"], pedido["valor"], str(pedido["valor_total"])))

    print("Ocorreu algum erro relacionado ao banco de dados...")

    cf.cursor.commit()
    print("-" * 100)
    lib.mensagem("Pedido cadastrado com sucesso!")
    print("-" * 100)