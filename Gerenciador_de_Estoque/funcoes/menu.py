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


# FUNÇÃO MENU PRINCIPAL =========================
def main_menu() -> str:
    """Essa função mostra um menu interativo e pede ao usuário que escolha uma opção.
Retorna: opcao (str)"""
    os.system("cls")
    print(f"{cor['ci']}=" * 50)
    print("M E N U".center(50))
    print(f"=" * 50)
    print(f"""{cor['no']}- {cor['ci']}[1]{cor['no']} Cadastro de produtos
- {cor['ci']}[2]{cor['no']} Consulta de produtos
- {cor['ci']}[3]{cor['no']} Atualização de produtos
- {cor['ci']}[4]{cor['no']} Filtrar produtos por preço
- {cor['ci']}[5]{cor['no']} Remoção de produtos
- {cor['ci']}[6]{cor['no']} Calcular o valor do estoque
- {cor['ci']}[0]{cor['no']} Sair do programa""")
    print(f"{cor['ci']}-" * 50)
    opcao = input(f"Digite a opção desejada:{cor['no']} ").strip()
    print(f"{cor['ci']}=" * 50)
    print(f"{cor['no']}")
    time.sleep(1)
    return opcao


# FUNÇÃO NENHUMA DAS OPÇÕES =====================
def no_opcao():
    """Essa função avisa o usuário que a opção digitada foi inválida."""
    print(f"{cor['vm']}Opção inválida! Tente novamente.{cor['no']}")
    time.sleep(2)


# FUNÇÃO VOLTAR AO MENU PRINCIPAL ===============
def back_menu():
    """Essa função avisa ao usuário que o programa vai retornar para o menu principal."""
    print(f"{cor['vm']}Voltando ao menu principal...{cor['no']}")
    time.sleep(1)


# FUNÇÃO ENCERRAR PROGRAMA ======================
def fim():
    """Essa função avisa o usuário que o programa está sendo encerrado."""
    print(f"{cor['am']}Encerrando programa...{cor['no']}")
    time.sleep(2)
    print(f"{cor['vm']}Programa encerrado.{cor['no']}")
    print(f"{cor['vm']}=" * 50)
    print(f"{cor['no']}")