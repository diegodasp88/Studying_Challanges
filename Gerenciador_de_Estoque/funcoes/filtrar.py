import time
import os
from funcoes.cadastro import estoque, cor


# [4] FUNÇÃO MENU FILTRAR OS PRODUTOS POR PREÇO
def filt_prod():
    """Essa função filtra os produtos dentro de uma faixa de preços definida pelo usuário."""
    os.system("cls")
    while True:
        print(f"{cor['az']}=" * 50)
        print("FILTRAR PRODUTOS POR PREÇO".center(50))
        print(f"=" * 50)
        
        # definindo a faixa de preço ------------
        min = float(input(f"{cor['az']}Digite o preço mínimo: {cor['no']}R$"))
        max = float(input(f"{cor['az']}Digite o preço máximo: {cor['no']}R$"))
        print(f"{cor['az']}-" * 50)
        
        # encontrando os produtos ---------------
        for produtos in estoque:
            if min < produtos["preco"] < max:
                print(f"{cor['az']}Produto: {cor['no']}{produtos.get('nome')} {cor['az']}| Categoria: {cor['no']}{produtos.get('categ')} {cor['az']}| Preço: {cor['no']}R${produtos.get('preco'):.2f} {cor['az']}| Qtde.: {cor['no']}{produtos.get('qtde')}")
        print(f"{cor['az']}-" * 50)
        
        # fazer nova filtragem? -----------------
        novo = input(f"Filtrar novamente (S/N)? {cor['no']}").strip().upper()
        if novo == "N":
            print(f"{cor['az']}=" * 50)
            print(f"{cor['vm']}\nVoltando para o menu principal...{cor['no']}")
            time.sleep(2)
            break
        else:
            os.system("cls")