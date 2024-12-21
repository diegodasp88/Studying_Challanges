import time
import os
from funcoes.cadastro import estoque, cor


# [2] FUNÇÃO MENU CONSULTAR OS PRODUTOS =========
def cons_prod():
    """Essa função mostra um menu interativo onde o usuário escolhe a opção de consulta dos produtos."""
    os.system("cls")
    while True:
        print(f"{cor['am']}=" * 50)
        print("CONSULTA DE PRODUTOS".center(50))
        print(f"=" * 50)
        print(f"""{cor['no']}-- {cor['am']}[1]{cor['no']} Consulta por produto
-- {cor['am']}[2]{cor['no']} Consulta por categoria
-- {cor['am']}[3]{cor['no']} Consulta por preço
-- {cor['am']}[4]{cor['no']} Consulta por quantidade
-- {cor['am']}[5]{cor['no']} Consulta completa do estoque
-- {cor['am']}[0]{cor['no']} Retornar ao menu principal""")
        print(f"{cor['am']}-" * 50)
        opcao = input(f"Digite a opção desejada:{cor['no']} ").strip().upper()
        print(f"{cor['am']}=" * 50)
        print(f"{cor['no']}")
        time.sleep(1)
        return opcao


# --[1] FUNÇÃO CONSULTAR POR PRODUTO ==============
def cons_1():
    """Essa função consulta os produtos do estoque por NOME."""
    os.system("cls")
    print(f"{cor['am']}=" * 50)
    print("CONSULTA POR PRODUTO".center(50))
    print(f"=" * 50)
    busca = input(f"Nome do produto: {cor['no']}").strip().upper()
    encontrado = False
    for produtos in estoque:
        if busca == produtos.get("nome"):
            print(f"{cor['am']}Produto: {cor['no']}{produtos.get('nome')} {cor['am']}| Categoria: {cor['no']}{produtos.get('categ')} {cor['am']}| Preço: {cor['no']}R${produtos.get('preco'):.2f} {cor['am']}| Qtde.: {cor['no']}{produtos.get('qtde')}")
            encontrado = True
    if encontrado == False:
        print(f"{cor['vm']}Produto não encontrado!{cor['no']}")
    print(f"{cor['am']}=" * 50)
    cont = input(f"Enter para continuar... {cor['no']}")


# --[2] FUNÇÃO CONSULTAR POR PRODUTO ==============
def cons_2():
    """Essa função consulta os produtos do estoque por CATEGORIA."""
    os.system("cls")
    print(f"{cor['am']}=" * 50)
    print("CONSULTA POR CATEGORIA".center(50))
    print(f"=" * 50)
    busca = input(f"Categoria: {cor['no']}").strip().upper()
    encontrado = False
    for produtos in estoque:
        if busca == produtos.get("categ"):
            print(f"{cor['am']}Produto: {cor['no']}{produtos.get('nome')} {cor['am']}| Categoria: {cor['no']}{produtos.get('categ')} {cor['am']}| Preço: {cor['no']}R${produtos.get('preco'):.2f} {cor['am']}| Qtde.: {cor['no']}{produtos.get('qtde')}")
            encontrado = True
    if encontrado == False:
        print(f"{cor['vm']}Produtos de categoria {busca} não encontrados!{cor['no']}")
    print(f"{cor['am']}=" * 50)
    cont = input(f"Enter para continuar... {cor['no']}")


# --[3] FUNÇÃO CONSULTAR POR PREÇO ================
def cons_3():
    """Essa função consulta os produtos do estoque por PREÇO."""
    os.system("cls")
    print(f"{cor['am']}=" * 50)
    print("CONSULTA POR PREÇO".center(50))
    print(f"=" * 50)
    busca = float(input(f"Preço: {cor['no']}R$"))
    encontrado = False
    for produtos in estoque:
        if busca == produtos.get("preco"):
            print(f"{cor['am']}Produto: {cor['no']}{produtos.get('nome')} {cor['am']}| Categoria: {cor['no']}{produtos.get('categ')} {cor['am']}| Preço: {cor['no']}R${produtos.get('preco'):.2f} {cor['am']}| Qtde.: {cor['no']}{produtos.get('qtde')}")
            encontrado = True
    if encontrado == False:
        print(f"{cor['vm']}Produtos de preço R${busca} não encontrados!{cor['no']}")
    print(f"{cor['am']}=" * 50)
    cont = input(f"Enter para continuar... {cor['no']}")


# --[4] FUNÇÃO CONSULTAR POR QUANTIDADE =========
def cons_4():
    """Essa função consulta os produtos do estoque por QUANTIDADE."""
    os.system("cls")
    print(f"{cor['am']}=" * 50)
    print("CONSULTA POR QUANTIDADE".center(50))
    print(f"=" * 50)
    busca = int(input(f"Quantidade: {cor['no']}"))
    encontrado = False
    for produtos in estoque:
        if busca == produtos.get("qtde"):
            print(f"{cor['am']}Produto: {cor['no']}{produtos.get('nome')} {cor['am']}| Categoria: {cor['no']}{produtos.get('categ')} {cor['am']}| Preço: {cor['no']}R${produtos.get('preco'):.2f} {cor['am']}| Qtde.: {cor['no']}{produtos.get('qtde')}")
            encontrado = True
    if encontrado == False:
        print(f"{cor['vm']}Nenhum produto de quantidade {busca} encontrado!{cor['no']}")
    print(f"{cor['am']}=" * 50)
    cont = input(f"Enter para continuar... {cor['no']}")


# --[5] FUNÇÃO CONSULTAR ESTOQUE COMPLETO
def cons_5():
    """Essa função consulta todos os produtos do estoque."""
    os.system("cls")
    print(f"{cor['am']}=" * 50)
    print("CONSULTAR ESTOQUE COMPLETO".center(50))
    print(f"=" * 50)
    encontrado = False
    for produtos in estoque:
        print(f"{cor['am']}Produto: {cor['no']}{produtos.get('nome')} {cor['am']}| Categoria: {cor['no']}{produtos.get('categ')} {cor['am']}| Preço: {cor['no']}R${produtos.get('preco'):.2f} {cor['am']}| Qtde.: {cor['no']}{produtos.get('qtde')}")
        encontrado = True
    if not encontrado:
        print(f"{cor['vm']}Nenhum produto cadastrado no estoque!{cor['no']}")
    print(f"{cor['am']}=" * 50)
    cont = input(f"Enter para continuar... {cor['no']}")
