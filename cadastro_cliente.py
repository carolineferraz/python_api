import lib
import uuid
import connection_factory as cf

def localiza_cliente():
    lib.limpar_tela()
    
    try:
        cf.cursor.execute('''SELECT * FROM clientes''')
    except:
        print("Ocorreu algum erro relacionado ao banco de dados...")
    else:
        clientes = cf.cursor.fetchall()
        print('-' * 70)
        for cliente in clientes:
            print('ÍNDICE: {} \nID: {} \nNOME: {} \nTELEFONE: {} \nE-MAIL: {}'.format(*cliente))
            print('-' * 70)
    
    indice = input("Digite o indice de qual cliente você deseja selecionar: \n")
    indice = int(indice)

    try:
        cf.cursor.execute('''SELECT id FROM clientes WHERE indice = ?''', indice)
    except:
        print("Ocorreu algum erro relacionado ao banco de dados...")
    else:
        id = cf.cursor.fetchone()
        
    return id


def listar():
    lib.limpar_tela();
    
    try:
        cf.cursor.execute('''SELECT * FROM clientes''')
    except:
        print("Ocorreu algum erro relacionado ao banco de dados...")
    else:
        clientes = cf.cursor.fetchall()
        print('-' * 70)
        for cliente in clientes:
            print('ID: {} \nNOME: {} \nTELEFONE: {} \nE-MAIL: {}'.format(*cliente))
            print('-' * 70)

    input("\nDigite 'Enter' para continuar ...")
    lib.limpar_tela()
    
def cadastrar():
    
    lib.limpar_tela()
    cliente = {}

    cliente["id"] = str(uuid.uuid4())

    cliente["nome"] = input("Digite o nome do cliente: ")

    cliente["telefone"] = input("Digite o telefone do cliente: ")

    cliente["email"] = input("Digite o email do cliente: ")

    try:
        cf.cursor.execute('''
            INSERT INTO clientes (id, nome, telefone, email)
            VALUES (?, ?, ?, ?);
        ''', (cliente["id"], cliente["nome"], cliente["telefone"], cliente["email"]))
    except:
        print("Ocorreu algum erro relacionado ao banco de dados...")
    else:
        cf.cursor.commit()
        print("-" * 100)
        lib.mensagem("Cliente cadastrado com sucesso!")
        print("-" * 100)
    