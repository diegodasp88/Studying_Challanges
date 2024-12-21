import time
import os

# DICIONÁRIO DE CORES ===========================
cor = {
    "vm": "\033[31m",
    "vd": "\033[32m",
    "am": "\033[33m",
    "az": "\033[34m",
    "mg": "\033[35m",
    "ci": "\033[36m",
    "no": "\033[0m",
}

# VARIÁVEIS GLOBAIS =============================
estoque = []    # lista global de dicionário de produtos


# [1] FUNÇÃO CADASTRAR OS PRODUTOS ==================
def cad_prod():
    """Essa função cadastra os produtos em dicionários (produtos) e adicione-os a uma lista (estoque)."""
    os.system("cls")
    while True:
            produtos = {}   # dicionário local de produtos
            print(f"{cor['az']}=" * 50)
            print("CADASTRO DE PRODUTOS".center(50))
            print(f"=" * 50)
            
            # cadastrando o produto -------------
            produtos["nome"] = input(f"{cor['az']}Produto: {cor['no']}").strip().upper()
            produtos["categ"] = input(f"{cor['az']}Categoria: {cor['no']}").strip().upper()
            produtos["preco"] = float(input(f"{cor['az']}Preço: {cor['no']}R$"))
            produtos["qtde"] = int(input(f"{cor['az']}Qtde.: {cor['no']}"))
            print(f"{cor['az']}-" * 50)
            
            # confirmar cadastro do produto -----
            print(f"{cor['az']}Produto: {cor['no']}{produtos.get('nome')} {cor['az']}| Categoria: {cor['no']}{produtos.get('categ')} {cor['az']}| Preço: {cor['no']}R${produtos.get('preco'):.2f} {cor['az']}| Qtde.: {cor['no']}{produtos.get('qtde')}")
            print(f"{cor['az']}-" * 50)
            conf = input(f"{cor['az']}Confirma o cadastro desse produto (S/N)? {cor['no']}").strip().upper()
            if conf == "S":
                  estoque.append(produtos)
                  time.sleep(1)
                  print(f"{cor['vd']}Cadastro registrado com sucesso!{cor['no']}")
                  print(f"{cor['az']}-" * 50)
            else:
                  time.sleep(1)
                  print(f"{cor['vm']}Cadastro cancelado!{cor['no']}")
                  print(f"{cor['az']}-" * 50)
            # fazer novo cadastro? --------------
            novo = input(f"Cadastrar mais um produto (S/N)? {cor['no']}").strip().upper()
            if novo == "N":
                  print(f"{cor['az']}=" * 50)
                  print(f"{cor['vm']}\nVoltando para o menu principal...{cor['no']}")
                  time.sleep(2)
                  break
            else:
                  os.system("cls")
