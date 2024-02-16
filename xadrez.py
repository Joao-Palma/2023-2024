
#------------------------------

def vazio():
    """
    espaço vazio no tabuleiro
    """
    return "vazio"


def verifica_vazio(Obj: any) -> bool:
    """
    verifica se o espaço está vazio 
    """
    return Obj == vazio()


def peao():
    """
    definição do peão \n
    devolve a representação do peão "peao" 
    """
    return "peao"


def verifica_peao(Obj: any) -> bool:
    """
    verifica se o objeto Obs é um peão 
    """
    return Obj == peao()


def torre():
    """
    definição do torre \n
    devolve a representação do torre "torre" 
    """
    return "torre"


def verifica_torre(Obj: any) -> bool:
    """
    verifica se o objeto Obs é uma torre 
    """
    return Obj == torre()


def bispo():
    """
    definição do bispo \n
    devolve a representação do bispo "bispo" 
    """
    return "bispo"


def verifica_bispo(Obj: any) -> bool:
    """
    verifica se o objeto Obs é um bispo 
    """
    return Obj == bispo()


def cavalo():
    """
    definição do cavalo \n
    devolve a representação do cavalo "cavalo" 
    """
    return "cavalo"


def verifica_cavalo(Obj: any) -> bool:
    """
    verifica se o objeto Obs é um cavalo 
    """
    return Obj == cavalo()


def rei():
    """
    efinição do rei \n
    devolve a representação do rei "rei" 
    """
    return "rei"


def verifica_rei(Obj: any) -> bool:
    """
    verifica se o objeto Obs é o rei 
    """
    return Obj == rei()


def rainha():
    """
    definição do rainha \n
    devolve a representação do rainha "rainha" 
    """
    return "rainha" 


def verifica_rainha(Obj: any) -> bool:
    """
    verifica se o objeto Obs é a rainha 
    """
    return Obj == rainha()

#------------------------------

def branco():
    """
    definição da peça branca \n
    devolve a representação da peça branca "branco" 
    """
    return "branco"


def verifica_branco(Cor: any) -> bool:
    """
    verifica se a cor Cor é branca
    """
    return Cor == branco()


def preto():
    """
    definição da peça preta \n
    devolve a representação da peça preta "preto" 
    """
    return "preto"


def verifica_preto(Cor: any) -> bool:
    """
    verifica se a cor Cor é preta
    """
    return Cor == preto()

#------------------------------

def movido():
    """
    definição do estado da peça movida \n
    devolve a representação do estado da peça movida "movido" 
    """
    return "movido"


def verifica_movido(Esta: any) -> bool:
    """
    verifica se o estado da peça é "movido"
    """
    return Esta == movido()


def por_mover():
    """
    definição do estado da peça por mover \n
    devolve a representação do estado peça por mover "por mover" 
    """
    return "por mover"


def verifica_por_mover(Esta: any) -> bool:
    """
    verifica se o estado da peça é "por_mover"
    """
    return Esta == por_mover()


def movido_uma_vez():
    """
    definição do estado da peça movida uma vez\n   (utilizado para o caso de en passante)\n
    devolve a representação do estado peça por mover "por mover" 
    """
    return "movido uma vez"


def verifica_movido_uma_vez(Esta: any) -> bool:
    """
    verifica se esta peça foi movida apenas uma vez
    """
    return Esta == movido_uma_vez()

#------------------------------

def verif_coord(Lin: int, Col: int) -> bool:
    """
    Verifica se as coordenadas introduzidas pertencem ao tabuleiro
    """
    return (Lin < 9 
            and Lin > 0 
            and Col < 9 
            and Col > 0)

#------------------------------ 
#     MOVIMENTO DAS PEÇAS  
#------------------------------ 

def obtem_hori_vert(Lin: int, Col: int) -> list:
    """
    Recebe coordenadas e devolve uma lista de listas com as coordenadas \n
    das casas na linhavertical e horizontal da mesma

    Returns: [ [hor_esq], [hor_dir], [ver_bai], [ver_cim] ]
    """
    List_ele_hor_dir = []
    List_ele_hor_esq = []
    List_ele_ver_cim = []
    List_ele_ver_bai = []

    for ind_col in range(1, 9):
        if ind_col != Col:
            if ind_col < Col:
                List_ele_hor_esq += [(Lin, ind_col)]
            else:
                List_ele_hor_dir += [(Lin, ind_col)]

    for ind_lin in range(1, 9):
        if ind_lin != Lin:
            if ind_lin < Lin:
                List_ele_ver_bai += [(ind_lin, Col)]
            else: 
                List_ele_ver_cim += [(ind_lin, Col)]
    
    return [List_ele_hor_esq, List_ele_hor_dir, List_ele_ver_bai, List_ele_ver_cim]


def obtem_diag(Lin: int, Col: int) -> list:
    """
    Recebe coordenadas e devolve uma lista de listas com as coordenadas \n
    das casas na diagonal da mesma 

    Returns: [ [inf_esq], [inf_dir], [sup_esq], [sup_dir] ]
    """
    List_ele_sup_dir = []
    List_ele_sup_esq = []
    List_ele_inf_dir = []
    List_ele_inf_esq = []
    Cond = True
    ind_lin = Lin
    ind_col = Col

    if Lin != 1 or Col != 8:
        while Cond:
            if(
                ind_col == 8
                or ind_lin == 1
                ):
                Cond = False
            else:
                ind_col += 1
                ind_lin -= 1 
                List_ele_sup_dir += [(ind_lin, ind_col)]
    
    Cond = True
    ind_lin = Lin
    ind_col = Col

    if Lin != 1 or Col != 1:
        while Cond:
            if(
                ind_col == 1 
                or ind_lin == 1
                ):
                Cond = False
            else:
                ind_col -= 1
                ind_lin -= 1 
                List_ele_sup_esq += [(ind_lin, ind_col)]
        
    Cond = True
    ind_lin = Lin
    ind_col = Col

    if Lin != 8 or Col != 8:
        while Cond:
            if( 
                ind_col == 8
                or ind_lin == 8
                ):
                Cond = False
            else:
                ind_col += 1
                ind_lin += 1 
                List_ele_inf_dir += [(ind_lin, ind_col)]
        
    Cond = True
    ind_lin = Lin
    ind_col = Col

    if Lin != 8 or Col != 1:
        while Cond:
            if( 
                ind_col == 1
                or ind_lin == 8
                ):
                Cond = False
            else:
                ind_col -= 1
                ind_lin += 1 
                List_ele_inf_esq += [(ind_lin, ind_col)]
    
    return [List_ele_inf_esq, List_ele_inf_dir, List_ele_sup_esq, List_ele_sup_dir]


def obtem_vizinhanca(Lin: int, Col: int) -> list:
    """
    Recebe coordenadas e devolve uma lista com as coordenadas \n
    das casas na vizinhaça da mesma 
    """
    Viz = []
    for ind_lin in range(Lin - 1, Lin + 2):
        for ind_col in range(Col - 1, Col + 2):
            if (
                (ind_lin != Lin or ind_col != Col) 
                and verif_coord(ind_lin, ind_col)
                ):
                Viz += [(ind_lin, ind_col)]
    return Viz         


def obtem_casas_em_L(Lin: int, Col: int) -> list:
    """
    Recebe coordenadas e devolve uma lista com as coordenadas \n
    das casas na vizinhaça "L" da mesma 
    """
    List_L = []

    for dif_lin in range(-2,3): 
        if not(dif_lin == 0): 
            dif_col = (3 - abs(dif_lin))

            if(verif_coord((Lin + dif_lin), (Col + dif_col))):
                List_L += [((Lin + dif_lin), (Col + dif_col))]
            if(verif_coord((Lin + dif_lin), (Col - dif_col))):
                List_L += [((Lin + dif_lin), (Col - dif_col))]

    return List_L 


def obtem_movi_peao_jogador_branco(Lin: int, Col: int) -> list:
    if verif_coord(Lin - 1, Col):
        return(Lin - 1, Col)


def obtem_movi_peao_jogador_preto(Lin: int, Col: int) -> list:
    if verif_coord(Lin + 1, Col):
        return(Lin + 1, Col)


def obtem_movi_peao_come_jogador_branco(Lin: int, Col: int) -> list:
    List_aux = []
    for ind_col in range(Col - 1, Col + 2):
        if(
            ind_col != Col 
            and verif_coord(Lin - 1, ind_col)
            ):
            List_aux += [(Lin - 1, ind_col)]
    return List_aux


def obtem_movi_peao_come_jogador_preto(Lin: int, Col: int) -> list:
    List_aux = []
    for ind_col in range(Col - 1, Col + 2):
        if(
            ind_col != Col 
            and verif_coord(Lin + 1, ind_col)
            ):
            List_aux += [(Lin + 1, ind_col)]
    return List_aux

#------------------------------ 

def cria_tab() -> dict:
    Tab = {}

    for Lin in range(1,9):
        for Col in range(1,9):
            Tab[(Lin, Col)] = vazio()
    return Tab

def adiciona_pecas_tab(Tab: dict) -> dict: 
    Tab_copia = Tab.copy()

    for col in range(1,9):
        Tab_copia[(2, col)] = [peao(), preto(), por_mover()]
        Tab_copia[(7, col)] = [peao(), branco(), por_mover()]
        if col == 1 or col == 8:
            Tab_copia[(1, col)] = [torre(), preto(), por_mover()]
            Tab_copia[(8, col)] = [torre(), branco(), por_mover()]
        elif col == 2 or col == 7:
            Tab_copia[(1, col)] = [bispo(), preto(), por_mover()]
            Tab_copia[(8, col)] = [bispo(), branco(), por_mover()]
        elif col == 3 or col == 6:
            Tab_copia[(1, col)] = [cavalo(), preto(), por_mover()]
            Tab_copia[(8, col)] = [cavalo(), branco(), por_mover()]
        elif col == 4:
            Tab_copia[(1, col)] = [rainha(), preto(), por_mover()]
            Tab_copia[(8, col)] = [rainha(), branco(), por_mover()]
        else:
            Tab_copia[(1, col)] = [rei(), preto(), por_mover()]
            Tab_copia[(8, col)] = [rei(), branco(), por_mover()]
    
    return Tab_copia


def obtem_atributos(Lin: int, Col: int, Tab: dict) -> list:
    return Tab[(Lin, Col)]


def obtem_peca(Lin: int, Col: int, Tab: dict) -> list:
    return obtem_atributos(Lin, Col, Tab)[0]


def obtem_cor(Lin: int, Col: int, Tab: dict) -> list:
    return obtem_atributos(Lin, Col, Tab)[1]


def obtem_estado(Lin: int, Col: int, Tab: dict) -> list:
    return obtem_atributos(Lin, Col, Tab)[2]


def obtem_cor_quadrado(Lin, Col):
    if (Lin + Col) % 2:
        return branco()
    return preto()


def Tab_para_str(Tab):
    Tab_str = "\u001b[38;5;52m.____________________________________________________________________________________________________.\
     \n\u001b[38;5;52m| .________________________________________________________________________________________________. |\033[0m\
             \n"
    for linha in range(1,9):
            for lin_por_col in range(1,7):
                Tab_str += "\u001b[38;5;52m| |\033[0m"

                for coluna in range(1,9):

                    if lin_por_col == 6:   # cor das linhas de baixo
                        if linha == 8:
                            if verifica_branco(obtem_cor_quadrado(linha, coluna)):
                                    Tab_str += "\u001b[48;5;254m" + "\u001b[38;5;52m" + "____________" + "\033[0m"
                            else:
                                    Tab_str += "\u001b[48;5;234m" + "\u001b[38;5;52m" + "____________" + "\033[0m"
                        else:
                            if verifica_branco(obtem_cor_quadrado(linha, coluna)):
                                    Tab_str += "\u001b[48;5;254m" + "            " + "\033[0m"
                            else:
                                    Tab_str += "\u001b[48;5;234m" + "            " + "\033[0m"

                    else:
                        if verifica_vazio(obtem_atributos(linha, coluna, Tab)):
                            if verifica_branco(obtem_cor_quadrado(linha, coluna)):
                                Tab_str += "\u001b[48;5;254m" + "            " + "\033[0m"
                            else:
                                Tab_str += "\u001b[48;5;234m" + "            " + "\033[0m"
                        else:
                            if lin_por_col == 1:
                                if (
                                    verifica_peao(obtem_peca(linha, coluna, Tab))
                                    or verifica_torre(obtem_peca(linha, coluna, Tab))
                                    ):
                                    if verifica_branco(obtem_cor_quadrado(linha, coluna)):
                                        Tab_str += "\u001b[48;5;254m" + "            " + "\033[0m"
                                    else:
                                        Tab_str += "\u001b[48;5;234m" + "            " + "\033[0m"
                                elif verifica_cavalo(obtem_peca(linha, coluna, Tab)):
                                    if verifica_branco(obtem_cor_quadrado(linha, coluna)):
                                        if verifica_branco(obtem_cor(linha, coluna, Tab)):
                                            Tab_str += "\u001b[48;5;254m" + "\u001b[38;5;252m" + "    __      " + "\033[0m"
                                        else:
                                            Tab_str += "\u001b[48;5;254m" + "\u001b[38;5;52m" + "    __      " + "\033[0m"
                                    else:
                                        if verifica_branco(obtem_cor(linha, coluna, Tab)):
                                            Tab_str += "\u001b[48;5;234m" + "\u001b[38;5;252m" + "    __      " + "\033[0m"
                                        else:
                                            Tab_str += "\u001b[48;5;234m" + "\u001b[38;5;52m" + "    __      " + "\033[0m"
                                elif verifica_bispo(obtem_peca(linha, coluna, Tab)):
                                    if verifica_branco(obtem_cor_quadrado(linha, coluna)):
                                        if verifica_branco(obtem_cor(linha, coluna, Tab)):
                                            Tab_str += "\u001b[48;5;254m" + "\u001b[38;5;252m" + "      _     " + "\033[0m"
                                        else:
                                            Tab_str += "\u001b[48;5;254m" + "\u001b[38;5;52m" + "      _     " + "\033[0m"
                                    else:
                                        if verifica_branco(obtem_cor(linha, coluna, Tab)):
                                            Tab_str += "\u001b[48;5;234m" + "\u001b[38;5;252m" + "      _     " + "\033[0m"
                                        else:
                                            Tab_str += "\u001b[48;5;234m" + "\u001b[38;5;52m" + "      _     " + "\033[0m"
                                elif verifica_rei(obtem_peca(linha, coluna, Tab)):
                                    if verifica_branco(obtem_cor_quadrado(linha, coluna)):
                                        if verifica_branco(obtem_cor(linha, coluna, Tab)):
                                            Tab_str += "\u001b[48;5;254m" + "\u001b[38;5;252m" + "     +      " + "\033[0m"
                                        else:
                                            Tab_str += "\u001b[48;5;254m" + "\u001b[38;5;52m" + "     +      " + "\033[0m"
                                    else:
                                        if verifica_branco(obtem_cor(linha, coluna, Tab)):
                                            Tab_str += "\u001b[48;5;234m" + "\u001b[38;5;252m" + "     +      " + "\033[0m"
                                        else:
                                            Tab_str += "\u001b[48;5;234m" + "\u001b[38;5;52m" + "     +      " + "\033[0m"
                                else:
                                    if verifica_branco(obtem_cor_quadrado(linha, coluna)):
                                        if verifica_branco(obtem_cor(linha, coluna, Tab)):
                                            Tab_str += "\u001b[48;5;254m" + "\u001b[38;5;252m" + "     .      " + "\033[0m"
                                        else:
                                            Tab_str += "\u001b[48;5;254m" + "\u001b[38;5;52m" + "     .      " + "\033[0m"
                                    else:
                                        if verifica_branco(obtem_cor(linha, coluna, Tab)):
                                            Tab_str += "\u001b[48;5;234m" + "\u001b[38;5;252m" + "     .      " + "\033[0m"
                                        else:
                                            Tab_str += "\u001b[48;5;234m" + "\u001b[38;5;52m" + "     .      " + "\033[0m"

                            elif lin_por_col == 2:
                                if (
                                    verifica_rainha(obtem_peca(linha, coluna, Tab))
                                    or verifica_rei(obtem_peca(linha, coluna, Tab))
                                    ):
                                    if verifica_branco(obtem_cor_quadrado(linha, coluna)):
                                        if verifica_branco(obtem_cor(linha, coluna, Tab)):
                                            Tab_str += "\u001b[48;5;254m" + "\u001b[38;5;252m" + "   /\|/\    " + "\033[0m"
                                        else:
                                            Tab_str += "\u001b[48;5;254m" + "\u001b[38;5;52m" + "   /\|/\    " + "\033[0m"
                                    else:
                                        if verifica_branco(obtem_cor(linha, coluna, Tab)):
                                            Tab_str += "\u001b[48;5;234m" + "\u001b[38;5;252m" + "   /\|/\    " + "\033[0m"
                                        else:
                                            Tab_str += "\u001b[48;5;234m" + "\u001b[38;5;52m" + "   /\|/\    " + "\033[0m"
                                elif verifica_cavalo(obtem_peca(linha, coluna, Tab)):
                                    if verifica_branco(obtem_cor_quadrado(linha, coluna)):
                                        if verifica_branco(obtem_cor(linha, coluna, Tab)):
                                            Tab_str += "\u001b[48;5;254m" + "\u001b[38;5;252m" + "   /  \_    " + "\033[0m"
                                        else:
                                            Tab_str += "\u001b[48;5;254m" + "\u001b[38;5;52m" + "   /  \_    " + "\033[0m"
                                    else:
                                        if verifica_branco(obtem_cor(linha, coluna, Tab)):
                                            Tab_str += "\u001b[48;5;234m" + "\u001b[38;5;252m" + "   /  \_    " + "\033[0m"
                                        else:
                                            Tab_str += "\u001b[48;5;234m" + "\u001b[38;5;52m" + "   /  \_    " + "\033[0m"
                                elif verifica_bispo(obtem_peca(linha, coluna, Tab)):
                                    if verifica_branco(obtem_cor_quadrado(linha, coluna)):
                                        if verifica_branco(obtem_cor(linha, coluna, Tab)):
                                            Tab_str += "\u001b[48;5;254m" + "\u001b[38;5;252m" + "   /"+chr(92)+chr(92)+" \    " + "\033[0m"
                                        else:
                                            Tab_str += "\u001b[48;5;254m" + "\u001b[38;5;52m" + "   /"+chr(92)+chr(92)+" \    " + "\033[0m"
                                    else:
                                        if verifica_branco(obtem_cor(linha, coluna, Tab)):
                                            Tab_str += "\u001b[48;5;234m" + "\u001b[38;5;252m" + "   /"+chr(92)+chr(92)+" \    " + "\033[0m"
                                        else:
                                            Tab_str += "\u001b[48;5;234m" + "\u001b[38;5;52m" + "   /"+chr(92)+chr(92)+" \    " + "\033[0m"
                                elif verifica_peao(obtem_peca(linha, coluna, Tab)):
                                    if verifica_branco(obtem_cor_quadrado(linha, coluna)):
                                        if verifica_branco(obtem_cor(linha, coluna, Tab)):
                                            Tab_str += "\u001b[48;5;254m" + "\u001b[38;5;252m" + "     _      " + "\033[0m"
                                        else:
                                            Tab_str += "\u001b[48;5;254m" + "\u001b[38;5;52m" + "     _      " + "\033[0m"
                                    else:
                                        if verifica_branco(obtem_cor(linha, coluna, Tab)):
                                            Tab_str += "\u001b[48;5;234m" + "\u001b[38;5;252m" + "     _      " + "\033[0m"
                                        else:
                                            Tab_str += "\u001b[48;5;234m" + "\u001b[38;5;52m" + "     _      " + "\033[0m"
                                else:
                                    if verifica_branco(obtem_cor_quadrado(linha, coluna)):
                                        if verifica_branco(obtem_cor(linha, coluna, Tab)):
                                            Tab_str += "\u001b[48;5;254m" + "\u001b[38;5;252m" + "   |-_-|    " + "\033[0m"
                                        else:
                                            Tab_str += "\u001b[48;5;254m" + "\u001b[38;5;52m" + "   |-_-|    " + "\033[0m"
                                    else:
                                        if verifica_branco(obtem_cor(linha, coluna, Tab)):
                                            Tab_str += "\u001b[48;5;234m" + "\u001b[38;5;252m" + "   |-_-|    " + "\033[0m"
                                        else:
                                            Tab_str += "\u001b[48;5;234m" + "\u001b[38;5;52m" + "   |-_-|    " + "\033[0m"

                            elif lin_por_col == 3:
                                if (
                                    verifica_rainha(obtem_peca(linha, coluna, Tab))
                                    or verifica_rei(obtem_peca(linha, coluna, Tab))
                                    or verifica_bispo(obtem_peca(linha, coluna, Tab))
                                    ):
                                    if verifica_branco(obtem_cor_quadrado(linha, coluna)):
                                        if verifica_branco(obtem_cor(linha, coluna, Tab)):
                                            Tab_str += "\u001b[48;5;254m" + "\u001b[38;5;252m" + "   \   /    " + "\033[0m"
                                        else:
                                            Tab_str += "\u001b[48;5;254m" + "\u001b[38;5;52m" + "   \   /    " + "\033[0m"
                                    else:
                                        if verifica_branco(obtem_cor(linha, coluna, Tab)):
                                            Tab_str += "\u001b[48;5;234m" + "\u001b[38;5;252m" + "   \   /    " + "\033[0m"
                                        else:
                                            Tab_str += "\u001b[48;5;234m" + "\u001b[38;5;52m" + "   \   /    " + "\033[0m"
                                elif verifica_peao(obtem_peca(linha, coluna, Tab)):
                                    if verifica_branco(obtem_cor_quadrado(linha, coluna)):
                                        if verifica_branco(obtem_cor(linha, coluna, Tab)):
                                            Tab_str += "\u001b[48;5;254m" + "\u001b[38;5;252m" + "    ( )     " + "\033[0m"
                                        else:
                                            Tab_str += "\u001b[48;5;254m" + "\u001b[38;5;52m" + "    ( )     " + "\033[0m"
                                    else:
                                        if verifica_branco(obtem_cor(linha, coluna, Tab)):
                                            Tab_str += "\u001b[48;5;234m" + "\u001b[38;5;252m" + "    ( )     " + "\033[0m"
                                        else:
                                            Tab_str += "\u001b[48;5;234m" + "\u001b[38;5;52m" + "    ( )     " + "\033[0m"
                                elif verifica_torre(obtem_peca(linha, coluna, Tab)):
                                    if verifica_branco(obtem_cor_quadrado(linha, coluna)):
                                        if verifica_branco(obtem_cor(linha, coluna, Tab)):
                                            Tab_str += "\u001b[48;5;254m" + "\u001b[38;5;252m" + "   |   |    " + "\033[0m"
                                        else:
                                            Tab_str += "\u001b[48;5;254m" + "\u001b[38;5;52m" + "   |   |    " + "\033[0m"
                                    else:
                                        if verifica_branco(obtem_cor(linha, coluna, Tab)):
                                            Tab_str += "\u001b[48;5;234m" + "\u001b[38;5;252m" + "   |   |    " + "\033[0m"
                                        else:
                                            Tab_str += "\u001b[48;5;234m" + "\u001b[38;5;52m" + "   |   |    " + "\033[0m"
                                else:
                                    if verifica_branco(obtem_cor_quadrado(linha, coluna)):
                                        if verifica_branco(obtem_cor(linha, coluna, Tab)):
                                            Tab_str += "\u001b[48;5;254m" + "\u001b[38;5;252m" + "   \   _\   " + "\033[0m"
                                        else:
                                            Tab_str += "\u001b[48;5;254m" + "\u001b[38;5;52m" + "   \   _\   " + "\033[0m"
                                    else:
                                        if verifica_branco(obtem_cor(linha, coluna, Tab)):
                                            Tab_str += "\u001b[48;5;234m" + "\u001b[38;5;252m" + "   \   _\   " + "\033[0m"
                                        else:
                                            Tab_str += "\u001b[48;5;234m" + "\u001b[38;5;52m" + "   \   _\   " + "\033[0m"

                            elif lin_por_col == 4:
                                if (
                                    verifica_rainha(obtem_peca(linha, coluna, Tab))
                                    or verifica_peao(obtem_peca(linha, coluna, Tab))
                                    or verifica_bispo(obtem_peca(linha, coluna, Tab))
                                    ):
                                    if verifica_branco(obtem_cor_quadrado(linha, coluna)):
                                        if verifica_branco(obtem_cor(linha, coluna, Tab)):
                                            Tab_str += "\u001b[48;5;254m" + "\u001b[38;5;252m" + "    /B\     " + "\033[0m"
                                        else:
                                            Tab_str += "\u001b[48;5;254m" + "\u001b[38;5;52m" + "    /P\     " + "\033[0m"
                                    else:
                                        if verifica_branco(obtem_cor(linha, coluna, Tab)):
                                            Tab_str += "\u001b[48;5;234m" + "\u001b[38;5;252m" + "    /B\     " + "\033[0m"
                                        else:
                                            Tab_str += "\u001b[48;5;234m" + "\u001b[38;5;52m" + "    /P\     " + "\033[0m"
                                elif(
                                    verifica_rei(obtem_peca(linha, coluna, Tab))
                                    or verifica_torre(obtem_peca(linha, coluna, Tab))
                                    ):
                                    if verifica_branco(obtem_cor_quadrado(linha, coluna)):
                                        if verifica_branco(obtem_cor(linha, coluna, Tab)):
                                            Tab_str += "\u001b[48;5;254m" + "\u001b[38;5;252m" + "    |B|     " + "\033[0m"
                                        else:
                                            Tab_str += "\u001b[48;5;254m" + "\u001b[38;5;52m" + "    |P|     " + "\033[0m"
                                    else:
                                        if verifica_branco(obtem_cor(linha, coluna, Tab)):
                                            Tab_str += "\u001b[48;5;234m" + "\u001b[38;5;252m" + "    |B|     " + "\033[0m"
                                        else:
                                            Tab_str += "\u001b[48;5;234m" + "\u001b[38;5;52m" + "    |P|     " + "\033[0m"
                                else:
                                    if verifica_branco(obtem_cor_quadrado(linha, coluna)):
                                        if verifica_branco(obtem_cor(linha, coluna, Tab)):
                                            Tab_str += "\u001b[48;5;254m" + "\u001b[38;5;252m" + "    |B\     " + "\033[0m"
                                        else:
                                            Tab_str += "\u001b[48;5;254m" + "\u001b[38;5;52m" + "    |P\     " + "\033[0m"
                                    else:
                                        if verifica_branco(obtem_cor(linha, coluna, Tab)):
                                            Tab_str += "\u001b[48;5;234m" + "\u001b[38;5;252m" + "    |B\     " + "\033[0m"
                                        else:
                                            Tab_str += "\u001b[48;5;234m" + "\u001b[38;5;52m" + "    |P\     " + "\033[0m"
                            
                            else:
                                if (
                                    verifica_rainha(obtem_peca(linha, coluna, Tab))
                                    or verifica_peao(obtem_peca(linha, coluna, Tab))
                                    or verifica_bispo(obtem_peca(linha, coluna, Tab))
                                    ):
                                    if verifica_branco(obtem_cor_quadrado(linha, coluna)):
                                        if verifica_branco(obtem_cor(linha, coluna, Tab)):
                                            Tab_str += "\u001b[48;5;254m" + "\u001b[38;5;252m" + "   /___\    " + "\033[0m"
                                        else:
                                            Tab_str += "\u001b[48;5;254m" + "\u001b[38;5;52m" + "   /___\    " + "\033[0m"
                                    else:
                                        if verifica_branco(obtem_cor(linha, coluna, Tab)):
                                            Tab_str += "\u001b[48;5;234m" + "\u001b[38;5;252m" + "   /___\    " + "\033[0m"
                                        else:
                                            Tab_str += "\u001b[48;5;234m" + "\u001b[38;5;52m" + "   /___\    " + "\033[0m"
                                elif(
                                    verifica_rei(obtem_peca(linha, coluna, Tab))
                                    or verifica_torre(obtem_peca(linha, coluna, Tab))
                                    ):
                                    if verifica_branco(obtem_cor_quadrado(linha, coluna)):
                                        if verifica_branco(obtem_cor(linha, coluna, Tab)):
                                            Tab_str += "\u001b[48;5;254m" + "\u001b[38;5;252m" + "   |___|    " + "\033[0m"
                                        else:
                                            Tab_str += "\u001b[48;5;254m" + "\u001b[38;5;52m" + "   |___|    " + "\033[0m"
                                    else:
                                        if verifica_branco(obtem_cor(linha, coluna, Tab)):
                                            Tab_str += "\u001b[48;5;234m" + "\u001b[38;5;252m" + "   |___|    " + "\033[0m"
                                        else:
                                            Tab_str += "\u001b[48;5;234m" + "\u001b[38;5;52m" + "   |___|    " + "\033[0m"
                                else:
                                    if verifica_branco(obtem_cor_quadrado(linha, coluna)):
                                        if verifica_branco(obtem_cor(linha, coluna, Tab)):
                                            Tab_str += "\u001b[48;5;254m" + "\u001b[38;5;252m" + "   |___\    " + "\033[0m"
                                        else:
                                            Tab_str += "\u001b[48;5;254m" + "\u001b[38;5;52m" + "   |___\    " + "\033[0m"
                                    else:
                                        if verifica_branco(obtem_cor(linha, coluna, Tab)):
                                            Tab_str += "\u001b[48;5;234m" + "\u001b[38;5;252m" + "   |___\    " + "\033[0m"
                                        else:
                                            Tab_str += "\u001b[48;5;234m" + "\u001b[38;5;52m" + "   |___\    " + "\033[0m"
                Tab_str += "\u001b[38;5;52m| |\033[0m\n"
    Tab_str += "\u001b[38;5;52m|____________________________________________________________________________________________________|\033[0m"
    return Tab_str


def obtem_pecas_de_cor(Cor: str, Tab: dict) -> list:
    """
    Obtem todas as coordenadas das peças de cor "Cor"

    Returns: 
    lista de tuplos de coordenadas  
    """
    List_coord = []

    for Lin in range(1,9):
        for Col in range(1,9):
            if not(verifica_vazio(obtem_atributos(Lin, Col, Tab))):
                if obtem_cor(Lin, Col, Tab) == Cor:
                    List_coord += [(Lin, Col)]

    return List_coord


def obtem_coord_pecas(Tab: dict) -> list:
    """
    Obtem todas as coordenadas das peças do Tab

    Returns: 
    lista de tuplos de coordenadas  
    """
    List_coord = []

    for Lin in range(1,9):
        for Col in range(1,9):
            if not(verifica_vazio(obtem_atributos(Lin, Col, Tab))):
                List_coord += [(Lin, Col)]

    return List_coord


def coord_bispo_possiv(Lin: int, Col:int, Tab: dict) -> list:
    Coord_diag = obtem_diag(Lin, Col)
    todas_coord = obtem_coord_pecas(Tab)
    Cor = obtem_cor(Lin, Col, Tab)
    inf_esq = Coord_diag[0]
    inf_dir = Coord_diag[1]
    sup_esq = Coord_diag[2]
    sup_dir = Coord_diag[3]

    for coord in todas_coord:
        List_aux = []
        Cond = True
        Lin_aux = coord[0]
        Col_aux = coord[1]

        if coord in inf_esq:
            if obtem_cor(Lin_aux, Col_aux, Tab) == Cor:
                List_aux += [coord]
                if Lin_aux != 8 or Col_aux != 1:
                    while Cond:
                        if( 
                            Col_aux == 1
                            or Lin_aux == 8
                            ):
                            Cond = False
                        else:
                            Col_aux -= 1
                            Lin_aux += 1 
                            List_aux += [(Lin_aux, Col_aux)]
                for coord_aux in List_aux:
                    if coord_aux in inf_esq:
                        inf_esq.remove(coord_aux)
            else:
                if Lin_aux != 8 or Col_aux != 1:
                    while Cond:
                        if( 
                            Col_aux == 1
                            or Lin_aux == 8
                            ):
                            Cond = False
                        else:
                            Col_aux -= 1
                            Lin_aux += 1 
                            List_aux += [(Lin_aux, Col_aux)]
                for coord_aux in List_aux:
                    if coord_aux in inf_esq:
                        inf_esq.remove(coord_aux)

        elif coord in inf_dir:
            if obtem_cor(Lin_aux, Col_aux, Tab) == Cor:
                List_aux += [coord]
                if Lin_aux != 8 or Col_aux != 8:
                    while Cond:
                        if( 
                            Col_aux == 8
                            or Lin_aux == 8
                            ):
                            Cond = False
                        else:
                            Col_aux -= 1
                            Lin_aux += 1 
                            List_aux += [(Lin_aux, Col_aux)]
                for coord_aux in List_aux:
                    if coord_aux in inf_dir:
                        inf_dir.remove(coord_aux)
            else:
                if Lin_aux != 8 or Col_aux != 8:
                    while Cond:
                        if( 
                            Col_aux == 8
                            or Lin_aux == 8
                            ):
                            Cond = False
                        else:
                            Col_aux -= 1
                            Lin_aux += 1 
                            List_aux += [(Lin_aux, Col_aux)]
                for coord_aux in List_aux:
                    if coord_aux in inf_dir:
                        inf_dir.remove(coord_aux)

        elif coord in sup_esq:
            if obtem_cor(Lin_aux, Col_aux, Tab) == Cor:
                List_aux += [coord]
                if Lin_aux != 1 or Col_aux != 1:
                    while Cond:
                        if( 
                            Col_aux == 1
                            or Lin_aux == 1
                            ):
                            Cond = False
                        else:
                            Col_aux -= 1
                            Lin_aux += 1 
                            List_aux += [(Lin_aux, Col_aux)]
                for coord_aux in List_aux:
                    if coord_aux in sup_esq:
                        sup_esq.remove(coord_aux)
            else:
                if Lin_aux != 1 or Col_aux != 1:
                    while Cond:
                        if( 
                            Col_aux == 1
                            or Lin_aux == 1
                            ):
                            Cond = False
                        else:
                            Col_aux -= 1
                            Lin_aux += 1 
                            List_aux += [(Lin_aux, Col_aux)]
                for coord_aux in List_aux:
                    if coord_aux in sup_esq: 
                        sup_esq.remove(coord_aux)

        elif coord in sup_dir:
            if obtem_cor(Lin_aux, Col_aux, Tab) == Cor:
                List_aux += [coord]
                if Lin_aux != 1 or Col_aux != 8:
                    while Cond:
                        if( 
                            Col_aux == 8
                            or Lin_aux == 1
                            ):
                            Cond = False
                        else:
                            Col_aux -= 1
                            Lin_aux += 1 
                            List_aux += [(Lin_aux, Col_aux)]
                for coord_aux in List_aux:
                    if coord_aux in sup_dir:
                        sup_dir.remove(coord_aux)
            else:
                if Lin_aux != 1 or Col_aux != 8:
                    while Cond:
                        if( 
                            Col_aux == 8
                            or Lin_aux == 1
                            ):
                            Cond = False
                        else:
                            Col_aux -= 1
                            Lin_aux += 1 
                            List_aux += [(Lin_aux, Col_aux)]
                for coord_aux in List_aux:
                    if coord_aux in sup_dir:
                        sup_dir.remove(coord_aux)

        else:
            pass
    
    return inf_esq + inf_dir + sup_esq + sup_dir


def coord_cavalo_possiv(Lin: int, Col:int, Tab: dict) -> list:
    List_coord = obtem_casas_em_L(Lin, Col)
    List_aux = []
    Cor = obtem_cor(Lin, Col, Tab)

    for coord in List_coord:
        Lin_aux = coord[0]
        Col_aux = coord[1]
        if verifica_vazio(obtem_atributos(Lin_aux, Col_aux, Tab)):
            List_aux += [coord]
        else:
            if not(obtem_cor(Lin_aux, Col_aux, Tab) == Cor):
                List_aux += [coord]

    return  List_aux


def coord_torre_possiv(Lin: int, Col:int, Tab: dict) -> list:
    Coord_hori_vert = obtem_hori_vert(Lin, Col)
    todas_coord = obtem_coord_pecas(Tab)
    Cor = obtem_cor(Lin, Col, Tab)
    hor_esq = Coord_hori_vert[0]
    hor_dir = Coord_hori_vert[1]
    ver_bai = Coord_hori_vert[2]
    ver_cim = Coord_hori_vert[3]

    for coord in todas_coord:
        List_aux = []
        Lin_aux = coord[0]
        Col_aux = coord[1]

        if coord in hor_esq:
            if obtem_cor(Lin_aux, Col_aux, Tab) == Cor:
                List_aux += [coord]
                for ind_col in range(1, Col_aux):
                    List_aux += [(Lin_aux, ind_col)]
                for coord_aux in List_aux:
                    if coord_aux in hor_esq:
                        hor_esq.remove(coord_aux)
            else:
                for ind_col in range(1, Col_aux):
                    List_aux += [(Lin_aux, ind_col)]
                for coord_aux in List_aux:
                    if coord_aux in hor_esq:
                        hor_esq.remove(coord_aux)

        elif coord in hor_dir:
            if obtem_cor(Lin_aux, Col_aux, Tab) == Cor:
                List_aux += [coord]
                for ind_col in range(Col_aux + 1, 9):
                    List_aux += [(Lin_aux, ind_col)]
                for coord_aux in List_aux:
                    if coord_aux in hor_dir:
                        hor_dir.remove(coord_aux)
            else:
                for ind_col in range(Col_aux + 1, 9):
                    List_aux += [(Lin_aux, ind_col)]
                for coord_aux in List_aux:
                    if coord_aux in hor_dir:
                        hor_dir.remove(coord_aux)

        elif coord in ver_bai:
            if obtem_cor(Lin_aux, Col_aux, Tab) == Cor:
                List_aux += [coord]
                for ind_lin in range(1, Lin_aux):
                    List_aux += [(ind_lin, Col_aux)]
                for coord_aux in List_aux:
                    if coord_aux in ver_bai:
                        ver_bai.remove(coord_aux)
            else:
                for ind_lin in range(1, Lin_aux):
                    List_aux += [(ind_lin, Col_aux)]
                for coord_aux in List_aux:
                    if coord_aux in ver_bai:
                        ver_bai.remove(coord_aux)

        elif coord in ver_cim:
            if obtem_cor(Lin_aux, Col_aux, Tab) == Cor:
                List_aux += [coord]
                for ind_lin in range(Lin_aux + 1, 9):
                    List_aux += [(ind_lin, Col_aux)]
                for coord_aux in List_aux:
                    if coord_aux in ver_cim:
                        ver_cim.remove(coord_aux)
            else:
                for ind_lin in range(Lin_aux + 1, 9):
                    List_aux += [(ind_lin, Col_aux)]
                for coord_aux in List_aux:
                    if coord_aux in ver_cim:
                        ver_cim.remove(coord_aux)

        else:
            pass
    
    return hor_esq + hor_dir + ver_bai + ver_cim


def coord_rainha_possiv(Lin, Col, Tab):
    return coord_bispo_possiv(Lin, Col, Tab) + coord_torre_possiv(Lin, Col, Tab)


def coord_rei_possiv_sem_check(Lin, Col, Tab):
    List_coord = obtem_vizinhanca(Lin, Col)
    Cor = obtem_cor(Lin, Col, Tab)
    List_aux = []

    for coord in List_coord:
        Lin_aux = coord[0]
        Col_aux = coord[1]
        if verifica_vazio(obtem_atributos(Lin_aux, Col_aux, Tab)):
            List_aux += [coord]
        else:
            if not(obtem_cor(Lin_aux, Col_aux, Tab) == Cor):
                List_aux += [coord]

    return  List_aux


def coord_peao_possiv(Lin, Col, Tab):
    List_aux = []
    Cor = obtem_cor(Lin, Col, Tab)

    if verifica_branco(Cor):
        Coord_frente = obtem_movi_peao_jogador_branco(Lin, Col)
        List_coord_come = obtem_movi_peao_come_jogador_branco(Lin, Col)
        if verifica_vazio(obtem_atributos(Coord_frente[0], Coord_frente[1], Tab)):
            List_aux += [Coord_frente]
        for coord in List_coord_come:
            if(
               not(verifica_vazio(obtem_atributos(coord[0], coord[1], Tab))) 
               and obtem_cor(coord[0], coord[1], Tab) != Cor
               ):
                List_aux += [coord]
    else:
        Coord_frente = obtem_movi_peao_jogador_preto(Lin, Col)
        List_coord_come = obtem_movi_peao_come_jogador_preto(Lin, Col)
        if verifica_vazio(obtem_atributos(Coord_frente[0], Coord_frente[1], Tab)):
            List_aux += [Coord_frente]
        for coord in List_coord_come:
            if(
               not(verifica_vazio(obtem_atributos(coord[0], coord[1], Tab))) 
               and obtem_cor(coord[0], coord[1], Tab) != Cor
               ):
                List_aux += [coord]
        
    return List_aux


def coord_En_passant_possi(Lin, Col, Tab):
    List_aux = []
    Cor = obtem_cor(Lin, Col, Tab)

    if verifica_branco(Cor):
        List_coord_come = obtem_movi_peao_come_jogador_branco(Lin, Col)
        for coord in List_coord_come:
            if (
                not(verifica_vazio(obtem_atributos(coord[0] + 1, coord[1],Tab))) 
                and verifica_peao(obtem_peca(coord[0] + 1, coord[1],Tab)) 
                and verifica_preto(obtem_cor(coord[0] + 1, coord[1],Tab))
                and verifica_movido_uma_vez(obtem_estado(coord[0] + 1, coord[1],Tab))
                ):
                List_aux += [coord]

    else:
        List_coord_come = obtem_movi_peao_come_jogador_preto(Lin, Col)
        for coord in List_coord_come:
            if (
                not(verifica_vazio(obtem_atributos(coord[0] - 1, coord[1],Tab))) 
                and verifica_peao(obtem_peca(coord[0] - 1, coord[1],Tab))
                and verifica_branco(obtem_cor(coord[0] - 1, coord[1],Tab))
                and verifica_movido_uma_vez(obtem_estado(coord[0] - 1, coord[1],Tab))
                ):
                List_aux += [coord]

    return List_aux


def coord_prim_peao_possi(Lin, Col, Tab):
    List_aux = []

    if verifica_por_mover(obtem_estado(Lin, Col, Tab)):
        Cor = obtem_cor(Lin, Col, Tab)
    
        if verifica_branco(Cor):
            if verif_coord(Lin - 2, Col):
                if verifica_vazio(obtem_atributos(Lin - 2, Col, Tab)):
                    List_aux += [(Lin - 2, Col)]       
        else:
            if verif_coord(Lin + 2, Col):
                if verifica_vazio(obtem_atributos(Lin + 2, Col, Tab)):
                    List_aux += [(Lin + 2, Col)] 

    return List_aux

#-------------------------------------------------------------------------------

def coord_bispo_possiv_para_check(Lin: int, Col:int, Tab: dict) -> list:
    Coord_diag = obtem_diag(Lin, Col)
    todas_coord = obtem_coord_pecas(Tab)
    Cor = obtem_cor(Lin, Col, Tab)
    inf_esq = Coord_diag[0]
    inf_dir = Coord_diag[1]
    sup_esq = Coord_diag[2]
    sup_dir = Coord_diag[3]

    for coord in todas_coord:
        List_aux = []
        Cond = True
        Lin_aux = coord[0]
        Col_aux = coord[1]

        if coord in inf_esq:
            if Lin_aux != 8 or Col_aux != 1:
                while Cond:
                    if( 
                        Col_aux == 1
                        or Lin_aux == 8
                        ):
                        Cond = False
                    else:
                        Col_aux -= 1
                        Lin_aux += 1 
                        List_aux += [(Lin_aux, Col_aux)]
            for coord_aux in List_aux:
                if coord_aux in inf_esq:
                    inf_esq.remove(coord_aux)

        elif coord in inf_dir:
            if Lin_aux != 8 or Col_aux != 8:
                while Cond:
                    if( 
                        Col_aux == 8
                        or Lin_aux == 8
                        ):
                        Cond = False
                    else:
                        Col_aux -= 1
                        Lin_aux += 1 
                        List_aux += [(Lin_aux, Col_aux)]
            for coord_aux in List_aux:
                if coord_aux in inf_dir:
                    inf_dir.remove(coord_aux)

        elif coord in sup_esq:
            if Lin_aux != 1 or Col_aux != 1:
                while Cond:
                    if( 
                        Col_aux == 1
                        or Lin_aux == 1
                        ):
                        Cond = False
                    else:
                        Col_aux -= 1
                        Lin_aux += 1 
                        List_aux += [(Lin_aux, Col_aux)]
            for coord_aux in List_aux:
                if coord_aux in sup_esq: 
                    sup_esq.remove(coord_aux)

        elif coord in sup_dir:
            if Lin_aux != 1 or Col_aux != 8:
                while Cond:
                    if( 
                        Col_aux == 8
                        or Lin_aux == 1
                        ):
                        Cond = False
                    else:
                        Col_aux -= 1
                        Lin_aux += 1 
                        List_aux += [(Lin_aux, Col_aux)]
            for coord_aux in List_aux:
                if coord_aux in sup_dir:
                    sup_dir.remove(coord_aux)

        else:
            pass
    
    return inf_esq + inf_dir + sup_esq + sup_dir


def coord_torre_possiv_para_check(Lin: int, Col:int, Tab: dict) -> list:
    Coord_hori_vert = obtem_hori_vert(Lin, Col)
    todas_coord = obtem_coord_pecas(Tab)
    Cor = obtem_cor(Lin, Col, Tab)
    hor_esq = Coord_hori_vert[0]
    hor_dir = Coord_hori_vert[1]
    ver_bai = Coord_hori_vert[2]
    ver_cim = Coord_hori_vert[3]

    for coord in todas_coord:
        List_aux = []
        Lin_aux = coord[0]
        Col_aux = coord[1]

        if coord in hor_esq:
            for ind_col in range(1, Col_aux):
                List_aux += [(Lin_aux, ind_col)]
            for coord_aux in List_aux:
                if coord_aux in hor_esq:
                    hor_esq.remove(coord_aux)

        elif coord in hor_dir:
            for ind_col in range(Col_aux + 1, 9):
                List_aux += [(Lin_aux, ind_col)]
            for coord_aux in List_aux:
                if coord_aux in hor_dir:
                    hor_dir.remove(coord_aux)

        elif coord in ver_bai:
            for ind_lin in range(1, Lin_aux):
                List_aux += [(ind_lin, Col_aux)]
            for coord_aux in List_aux:
                if coord_aux in ver_bai:
                    ver_bai.remove(coord_aux)

        elif coord in ver_cim:
            for ind_lin in range(Lin_aux + 1, 9):
                List_aux += [(ind_lin, Col_aux)]
            for coord_aux in List_aux:
                if coord_aux in ver_cim:
                    ver_cim.remove(coord_aux)

        else:
            pass
    
    return hor_esq + hor_dir + ver_bai + ver_cim


def coord_rainha_possiv_para_check(Lin, Col, Tab):
    return coord_bispo_possiv_para_check(Lin, Col, Tab) + coord_torre_possiv_para_check(Lin, Col, Tab)

#----------------------------------------------------------------------------------

def posicoes_check(Cor: str, Tab: dict) -> list:
    Lista_final = []

    for lin in range(1,9):
        for col in range(1,9):
            if not(verifica_vazio(obtem_atributos(lin, col, Tab))):
                if obtem_cor(lin, col, Tab) != Cor:
                    if verifica_peao(obtem_peca(lin, col, Tab)):
                        if verifica_preto(Cor):
                            Lista_final += obtem_movi_peao_come_jogador_branco(lin, col)
                        else:
                            Lista_final += obtem_movi_peao_come_jogador_preto(lin, col)
                    elif verifica_torre(obtem_peca(lin, col, Tab)):
                        Lista_final += coord_torre_possiv_para_check(lin, col, Tab)
                    elif verifica_cavalo(obtem_peca(lin, col, Tab)):
                        Lista_final += obtem_casas_em_L(lin, col)
                    elif verifica_bispo(obtem_peca(lin, col, Tab)):
                        Lista_final += coord_bispo_possiv_para_check(lin, col, Tab)
                    elif verifica_rei(obtem_peca(lin, col, Tab)):
                        Lista_final += coord_rei_possiv_sem_check(lin, col, Tab)  
                    else:
                        Lista_final += coord_rainha_possiv_para_check(lin, col, Tab)

    return Lista_final


def verif_king_rook_esq(Lin, Col, Tab): # adicionar verificação de check
    List_aux = []
    Cor = obtem_cor(Lin, Col, Tab)
    List_posi_check = posicoes_check(Cor, Tab)

    if(
       verifica_por_mover(obtem_estado(Lin, Col, Tab)) 
       and verifica_torre(obtem_peca(Lin, 1, Tab)) 
       and verifica_por_mover(obtem_estado(Lin, 1, Tab))
       ):
        cond = 1
        for ind_col in range(2, Col):
            if verifica_vazio(obtem_atributos(Lin, ind_col, Tab)):
                cond *= 1
            else:
                cond *= 0
        if cond == 1:
            if (Lin,3) not in List_posi_check:
                List_aux += [(Lin,3)]
    return List_aux
    
    
def verif_king_rook_dir(Lin, Col, Tab): # adicionar verificação de check
    List_aux = []    
    Cor = obtem_cor(Lin, Col, Tab)
    List_posi_check = posicoes_check(Cor, Tab)
    
    if(
       verifica_por_mover(obtem_estado(Lin, Col, Tab)) 
       and verifica_torre(obtem_peca(Lin, 8, Tab)) 
       and verifica_por_mover(obtem_estado(Lin, 8, Tab))
       ):
        cond = 1
        for ind_col in range(Col + 1, 8):
            if verifica_vazio(obtem_atributos(Lin, ind_col, Tab)):
                cond *= 1
            else:
                cond *= 0
        if cond == 1:
            if (Lin,7) not in List_posi_check:
                List_aux += [(Lin,7)]

    return List_aux


def coord_rei_possiv_sem_check(Lin, Col, Tab):
    List_coord = obtem_vizinhanca(Lin, Col)
    Cor = obtem_cor(Lin, Col, Tab)
    List_posi_check = posicoes_check(Cor, Tab)
    List_aux = []

    for coord in List_coord:
        Lin_aux = coord[0]
        Col_aux = coord[1]
        if verifica_vazio(obtem_atributos(Lin_aux, Col_aux, Tab)):
            if coord not in List_posi_check:
                List_aux += [coord]
        else:
            if not(obtem_cor(Lin_aux, Col_aux, Tab) == Cor):
                if coord not in List_posi_check:
                    List_aux += [coord]

    return  List_aux

# print(Tab_para_str({(1, 1): ['torre', 'preto', 'por mover'], (1, 2): ['bispo', 'preto', 'por mover'], (1, 3): ['cavalo', 'preto', 'por mover'], (1, 4): ['rainha', 'preto', 'por mover'], (1, 5): ['rei', 'preto', 'por mover'], (1, 6): ['cavalo', 'preto', 'por mover'], (1, 7): ['bispo', 'preto', 'por mover'], (1, 8): ['torre', 'preto', 'por mover'], (2, 1): ['peao', 'preto', 'por mover'], (2, 2): ['peao', 'preto', 'por mover'], (2, 3): ['peao', 'preto', 'por mover'], (2, 4): ['peao', 'preto', 'por mover'], (2, 5): ['peao', 'preto', 'por mover'], (2, 6): ['peao', 'preto', 'por mover'], (2, 7): ['peao', 'preto', 'por mover'], (2, 8): ['peao', 'preto', 'por mover'], (3, 1): 'vazio', (3, 2): 'vazio', (3, 3): 'vazio', (3, 4): 'vazio', (3, 5): ['torre', 'preto', 'por mover'], (3, 6): 'vazio', (3, 7): 'vazio', (3, 8): 'vazio', (4, 1): 'vazio', (4, 2): 'vazio', (4, 3): 'vazio', (4, 4): 'vazio', (4, 5): 'vazio', (4, 6): 'vazio', (4, 7): 'vazio', (4, 8): 'vazio', (5, 1): 'vazio', (5, 2): 'vazio', (5, 3): 'vazio', (5, 4): 'vazio', (5, 5): 'vazio', (5, 6): 'vazio', (5, 7): 'vazio', (5, 8): 'vazio', (6, 1): 'vazio', (6, 2): 'vazio', (6, 3): 'vazio', (6, 4): 'vazio', (6, 5): 'vazio', (6, 6): 'vazio', (6, 7): 'vazio', (6, 8): 'vazio', (7, 1): ['peao', 'branco', 'por mover'], (7, 2): ['peao', 'branco', 'por mover'], (7, 3): ['peao', 'branco', 'por mover'], (7, 4): ['peao', 'branco', 'por mover'], (7, 5): 'vazio', (7, 6): ['peao', 'branco', 'por mover'], (7, 7): ['peao', 'branco', 'por mover'], (7, 8): ['peao', 'branco', 'por mover'], (8, 1): ['torre', 'branco', 'por mover'], (8, 2): ['bispo', 'branco', 'por mover'], (8, 3): ['cavalo', 'branco', 'por mover'], (8, 4): ['rainha', 'branco', 'por mover'], (8, 5): ['rei', 'branco', 'por mover'], (8, 6): ['cavalo', 'branco', 'por mover'], (8, 7): ['bispo', 'branco', 'por mover'], (8, 8): ['torre', 'branco', 'por mover']}))
print(posicoes_check(branco(), {(1, 1): ['torre', 'preto', 'por mover'], (1, 2): ['bispo', 'preto', 'por mover'], (1, 3): ['cavalo', 'preto', 'por mover'], (1, 4): ['rainha', 'preto', 'por mover'], (1, 5): ['rei', 'preto', 'por mover'], (1, 6): ['cavalo', 'preto', 'por mover'], (1, 7): ['bispo', 'preto', 'por mover'], (1, 8): ['torre', 'preto', 'por mover'], (2, 1): ['peao', 'preto', 'por mover'], (2, 2): ['peao', 'preto', 'por mover'], (2, 3): ['peao', 'preto', 'por mover'], (2, 4): ['peao', 'preto', 'por mover'], (2, 5): ['peao', 'preto', 'por mover'], (2, 6): ['peao', 'preto', 'por mover'], (2, 7): ['peao', 'preto', 'por mover'], (2, 8): ['peao', 'preto', 'por mover'], (3, 1): 'vazio', (3, 2): 'vazio', (3, 3): 'vazio', (3, 4): 'vazio', (3, 5): ['torre', 'preto', 'por mover'], (3, 6): 'vazio', (3, 7): 'vazio', (3, 8): 'vazio', (4, 1): 'vazio', (4, 2): 'vazio', (4, 3): 'vazio', (4, 4): 'vazio', (4, 5): 'vazio', (4, 6): 'vazio', (4, 7): 'vazio', (4, 8): 'vazio', (5, 1): 'vazio', (5, 2): 'vazio', (5, 3): 'vazio', (5, 4): 'vazio', (5, 5): 'vazio', (5, 6): 'vazio', (5, 7): 'vazio', (5, 8): 'vazio', (6, 1): 'vazio', (6, 2): 'vazio', (6, 3): 'vazio', (6, 4): 'vazio', (6, 5): 'vazio', (6, 6): 'vazio', (6, 7): 'vazio', (6, 8): 'vazio', (7, 1): ['peao', 'branco', 'por mover'], (7, 2): ['peao', 'branco', 'por mover'], (7, 3): ['peao', 'branco', 'por mover'], (7, 4): ['peao', 'branco', 'por mover'], (7, 5): 'vazio', (7, 6): ['peao', 'branco', 'por mover'], (7, 7): ['peao', 'branco', 'por mover'], (7, 8): ['peao', 'branco', 'por mover'], (8, 1): ['torre', 'branco', 'por mover'], (8, 2): ['bispo', 'branco', 'por mover'], (8, 3): ['cavalo', 'branco', 'por mover'], (8, 4): ['rainha', 'branco', 'por mover'], (8, 5): ['rei', 'branco', 'por mover'], (8, 6): ['cavalo', 'branco', 'por mover'], (8, 7): ['bispo', 'branco', 'por mover'], (8, 8): ['torre', 'branco', 'por mover']}))