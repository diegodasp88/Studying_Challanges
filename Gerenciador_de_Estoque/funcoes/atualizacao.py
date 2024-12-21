import time
import os
from funcoes.cadastro import estoque, cor

# [3] FUNÇÃO ATUALIZAR PRODUTOS =================
def update_prod():
    """Essa função atualiza os dados dos produtos de acordo com o usuário."""
    os.system("cls")
    while True:
        print(f"{cor['mg']}=" * 50)
        print("ATUALIZAÇÃO DE PRODUTOS".center(50))
        print(f"=" * 50)
        busca = input(f"Nome do produto a ser atualizado: {cor['no']}").strip().upper()
        print(f"{cor['mg']}-" * 50)

        # buscando o produto --------------------
        encontrado = None
        for produtos in estoque:
            if busca == produtos.get("nome"):
                print(f"{cor['vd']}Produto encontrado:{cor['no']}")
                print(f"{cor['mg']}Produto: {cor['no']}{produtos.get('nome')} {cor['mg']}| Categoria: {cor['no']}{produtos.get('categ')} {cor['mg']}| Preço: {cor['no']}R${produtos.get('preco'):.2f} {cor['mg']}| Qtde.: {cor['no']}{produtos.get('qtde')}")
                encontrado = produtos
                print(f"{cor['mg']}-" * 50)
                print(f"{cor['vm']}Caso não deseja alterar alguma informação, deixe vazio.{cor['no']}")
                print(f"{cor['vm']}*" * 60)

                # criando um dicionário para atualizar o produto
                atualizado = {}    
                novo_nome = input(f"{cor['mg']}Alterar o nome do produto para: {cor['no']}").strip().upper()
                if novo_nome:   # se o usuário digitar algo
                    atualizado["nome"] = novo_nome
                else:
                    atualizado["nome"] = produtos["nome"]
                nova_cat = input(f"{cor['mg']}Alterar a categoria do produto para: {cor['no']}").strip().upper()
                if nova_cat:   # se o usuário digitar algo
                    atualizado["categ"] = nova_cat
                else:
                    atualizado["categ"] = produtos["categ"]
                novo_preco = float(input(f"{cor['mg']}Alterar o preço do produto para: {cor['no']}R$"))
                if novo_preco:   # se o usuário digitar algo
                    atualizado["preco"] = novo_preco
                else:
                    atualizado["preco"] = produtos["preco"]
                nova_qtde = int(input(f"{cor['mg']}Alterar a quantidade do produto para: {cor['no']}"))
                if nova_qtde:   # se o usuário digitar algo
                    atualizado["qtde"] = nova_qtde
                else:
                    atualizado["qtde"] = produtos["qtde"]

                # confirmar a atualização do produto
                print(f"{cor['mg']}-" * 50)
                print(f"{cor['mg']}Produto: {cor['no']}{atualizado.get('nome')} {cor['mg']}| Categoria: {cor['no']}{atualizado.get('categ')} {cor['mg']}| Preço: {cor['no']}R${atualizado.get('preco'):.2f} {cor['mg']}| Qtde.: {cor['no']}{atualizado.get('qtde')}")
                print(f"{cor['mg']}-" * 50)
                conf = input(f"{cor['mg']}Confirma a atualização desse produto (S/N)? {cor['no']}").strip().upper()
                if conf == "S":
                    produtos.update(atualizado)
                    time.sleep(1)
                    print(f"{cor['vd']}Atualização registrada com sucesso!{cor['no']}")
                    print(f"{cor['mg']}-" * 50)
                else:
                    time.sleep(1)
                    print(f"{cor['vm']}Atualização cancelado!{cor['no']}")
                    print(f"{cor['mg']}-" * 50)
                break

        # se o produto não for encontrado -------
        if not encontrado:
            print(f"{cor['vm']}Produto não encontrado!{cor['no']}")
            print(f"{cor['mg']}=" * 50)
            time.sleep(1)
        
        # fazer nova atualização? ---------------
        novo = input(f"{cor['mg']}Atualizar mais um produto (S/N)? {cor['no']}").strip().upper()
        if novo == "N":
            print(f"{cor['mg']}=" * 50)
            print(f"{cor['vm']}\nVoltando para o menu principal...{cor['no']}")
            time.sleep(2)
            break
        else:
            os.system("cls")
