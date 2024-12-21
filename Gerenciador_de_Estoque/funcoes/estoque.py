import time
import os
from funcoes.cadastro import estoque, cor

# [6] FUNÇÃO CALCULAR ESTOQUE =================
def calc_estoque():
    """Essa função calcula o valor total do estoque."""
    os.system("cls")
    while True:
        print(f"{cor['mg']}=" * 50)
        print("CALCULAR VALOR DO ESTOQUE".center(50))
        print(f"{cor['mg']}=" * 50)
        print(f"{cor['mg']}Calculando o valor total do estoque...{cor['no']}")
        time.sleep(1)
        print(f"{cor['mg']}-" * 50)
        
        # listando os produtos ------------------
        encontrado = False
        for produtos in estoque:
            produtos["total"] = float(produtos.get("preco") * produtos.get("qtde"))
            print(f"{cor['mg']}Produto: {cor['no']}{produtos.get('nome')} {cor['mg']}| Categoria: {cor['no']}{produtos.get('categ')} {cor['mg']}| Preço: {cor['no']}R${produtos.get('preco'):.2f} {cor['mg']}| Qtde.: {cor['no']}{produtos.get('qtde')} {cor['mg']}/ Total: {cor['no']}R${produtos.get('total'):.2f}")
            encontrado = True
        if not encontrado:
            print(f"{cor['vm']}Nenhum produto cadastrado no estoque!{cor['no']}")
        print(f"{cor['mg']}-" * 50)
        
        # calculando o valor total do estoque ---
        total = sum(produtos.get("preco") * produtos.get("qtde") for produtos in estoque)
        print(f"{cor['mg']}Valor total do estoque: {cor['no']}R${total:.2f}")
        print(f"{cor['mg']}-" * 50)
        cont = input(f"{cor['mg']}Enter para continuar... {cor['no']}")
        break