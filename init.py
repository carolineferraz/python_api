import lib
import cadastro_cliente
import cadastro_pedido

print("-" * 100)
print("Bem vindo ao programa para pedidos de clientes")
print("-" * 100)

while(True):
    print("Selecione uma das opções abaixo:")
    print("1 - Cadastro de clientes")
    print("2 - Lista clientes")
    print("3 - Cadastro de pedidos")
    print("4 - Lista de pedidos")
    print("5 - Sair")

    opcao = input()

    if opcao == "1":
        cadastro_cliente.cadastrar()
    elif opcao == "2":
        cadastro_cliente.listar()
    elif opcao == "3":
        cadastro_pedido.cadastrar()
    elif opcao == "4":
        cadastro_pedido.listar()
    elif opcao == "5":
        lib.mensagem("Programa encerrado!")
        break
    else:
        lib.mensagem("Opcão inválida")
    
    lib.limpar_tela()