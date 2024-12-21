import funcoes.menu as menu
import funcoes.cadastro as cadastro
import funcoes.consulta as consulta
import funcoes.atualizacao as update
import funcoes.filtrar as filtrar
import funcoes.remove as remove
import funcoes.estoque as estoque

# INÍCIO DO PROGRAMA ============================
while True:
    main_menu = menu.main_menu()

    # [1] CADASTRO DE PRODUTOS ------------------
    if main_menu == "1":
        cadastro.cad_prod()

    # [2] CONSULTA DE PRODUTOS ------------------
    elif main_menu == "2":
        while True:
            cons = consulta.cons_prod()
            if cons == "1":     # [A] consulta por produto
                consulta.cons_1()
            elif cons == "2":   # [B] consulta por categoria
                consulta.cons_2()
            elif cons == "3":   # [C] consulta por preço
                consulta.cons_3()
            elif cons == "4":   # [C] consulta por quantidade
                consulta.cons_4()
            elif cons == "5":   # [D] consulta estoque completo
                consulta.cons_5()
            elif cons == "0":   # [D] retorna ao menu principal
                menu.back_menu()
                break
            else:
                menu.no_opcao()  # opção inválida

    # [3] ATUALIZAÇÃO DE PRODUTOS ---------------
    elif main_menu == "3":
        update.update_prod()

    # [4] FILTRAR PRODUTOS POR PREÇO ------------
    elif main_menu == "4":
        filtrar.filt_prod()

    # [5] REMOÇÃO DE PRODUTOS -------------------
    elif main_menu == "5":
        remove.remove_prod()

    # [6] CALCULAR VALOR DO ESTOQUE -------------
    elif main_menu == "6":
        estoque.calc_estoque()

    # [0] SAIR DO PROGRAMA ----------------------
    elif main_menu == "0":
        menu.fim()
        break
    
    # OPÇÃO INVÁLIDA
    else:
        menu.no_opcao()

# FIM DO PROGRAMA ===============================