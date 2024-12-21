import time
import os
from funcoes.cadastro import estoque, cor

# [3] FUNÇÃO ATUALIZAR PRODUTOS =================
def remove_prod():
    """Essa função remove os produtos determinados pelo usuário do estoque."""
    os.system("cls")
    while True:
        print(f"{cor['am']}=" * 50)
        print("REMOÇÃO DE PRODUTOS".center(50))
        print(f"=" * 50)
        busca = input(f"Nome do produto a ser atualizado: {cor['no']}").strip().upper()
        print(f"{cor['am']}-" * 50)

        # buscando o produto --------------------
        encontrado = None
        for produtos in estoque:
            if busca == produtos.get("nome"):
                print(f"{cor['vd']}Produto encontrado:{cor['no']}")
                print(f"{cor['am']}Produto: {cor['no']}{produtos.get('nome')} {cor['am']}| Categoria: {cor['no']}{produtos.get('categ')} {cor['am']}| Preço: {cor['no']}R${produtos.get('preco'):.2f} {cor['am']}| Qtde.: {cor['no']}{produtos.get('qtde')}")
                encontrado = produtos
                print(f"{cor['am']}-" * 50)
        
        # confirmar remoção ---------------------
            conf = input(f"{cor['am']}Confirma a exclusão desse produto (S/N)? {cor['no']}").strip().upper()
            if conf == "S":
                estoque.remove(encontrado)
                time.sleep(1)
                print(f"{cor['vd']}Produto removido com sucesso!{cor['no']}")
                print(f"{cor['am']}-" * 50)
            else:
                time.sleep(1)
                print(f"{cor['vm']}Exclusão cancelada!{cor['no']}")
                print(f"{cor['am']}-" * 50)
        
        # se o produto não for encontrado -------     
        if not encontrado:
            print(f"{cor['vm']}Produto não encontrado!{cor['no']}")
            print(f"{cor['am']}=" * 50)
            time.sleep(1)
            
        # fazer nova filtragem? -----------------
        novo = input(f"{cor['am']}Remover mais um produto (S/N)? {cor['no']}").strip().upper()
        if novo == "N":
            print(f"{cor['am']}=" * 50)
            print(f"{cor['vm']}\nVoltando para o menu principal...{cor['no']}")
            time.sleep(2)
            break
        else:
            os.system("cls")