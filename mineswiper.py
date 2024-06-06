from math import sqrt
from random import choice
from os import system

# minesweeper


#--------------- Conteudo da peça

def mina():
    return "mina"


def verifica_mina(Obj):
    return Obj == mina()


def vazio():
    return "vazio"


def verifica_vazio(Obj):
    return Obj == vazio()

#--------------- Estado da peça 

def por_ver():
    return "por ver"


def verifica_por_ver(Obj):
    return Obj == por_ver()


def visto():
    return "visto"


def verifica_visto(Obj):
    return Obj == visto()


def bandeira():
    return "bandeira"


def verifica_bandeira(Obj):
    return Obj == bandeira()


def adj_vazio():
    return "adj_vazio"


def verifica_adj_vazio(Obj):
    return Obj == adj_vazio()

#--------------- Caracteristicas das posiçoes

def obtem_estado(Lin, Col, Tab):
    return Tab[(Lin, Col)][1]


def obtem_conteudo(Lin, Col, Tab):
    return Tab[(Lin, Col)][0]


def obtem_minas_viz(Lin, Col, Tab):
    return Tab[(Lin, Col)][2]


def obtem_atributos(Lin, Col, Tab):
    return Tab[(Lin, Col)]

#---------------

def cria_tab(Tam):
    Tab = {}
    for ind_lin in range(1, Tam + 1):
        for ind_col in range(1, Tam + 1):
            Tab[(ind_lin,ind_col)] = [vazio(), por_ver(), 0]

    return Tab


def verif_coord(Tam, Lin, Col):
    return (
            type(Col) == int
            and type(Lin) == int
            and Col > 0 
            and Lin > 0 
            and Col <= Tam 
            and Lin <= Tam
            )


def vizinhanca(Lin, Col, Tam):
    Viz = []
    for ind_lin in range(Lin - 1, Lin + 2):
        for ind_col in range(Col - 1, Col + 2):
            if (
                (ind_lin != Lin or ind_col != Col) 
                and verif_coord(Tam, ind_lin, ind_col)
                ):
                Viz += [(ind_lin, ind_col)]
    return Viz            


def vizinhanca_reduzida(Lin, Col, Tam):
    Viz = []
    if verif_coord(Tam, Lin - 1, Col):
        Viz += [(Lin - 1, Col)]
    if verif_coord(Tam, Lin, Col - 1):
        Viz += [(Lin, Col - 1)]
    if verif_coord(Tam, Lin, Col + 1):
        Viz += [(Lin, Col + 1)]
    if verif_coord(Tam, Lin + 1, Col):
        Viz += [(Lin + 1, Col)]
    return Viz

def adiciona_contagem_minas(Tab):
    Tab_copia = Tab.copy()
    Tam = int(sqrt(len(Tab)))
    List_cord_viz = []
    Atributos = []

    for ind_lin in range(1, Tam + 1):
        for ind_col in range(1, Tam + 1):
            Atributos = Tab[(ind_lin,ind_col)]
            if verifica_mina(Atributos[0]):
                List_cord_viz += vizinhanca(ind_lin, ind_col, Tam)

    for coord in List_cord_viz:
        Cont_antes = obtem_minas_viz(coord[0], coord[1], Tab_copia)
        Atributos = obtem_atributos(coord[0], coord[1], Tab_copia)
        Tab_copia[(coord[0], coord[1])] = Atributos[0:2] + [Cont_antes + 1]
    
    return Tab_copia


def adiciona_minas(Tab):
    Tab_copia = Tab.copy()
    Tam = int(sqrt(len(Tab)))
    List_coord = list(Tab_copia)

    if Tam == 10:
        Quanti = 10
    elif Tam == 18:
        Quanti = 40
    else:
        Quanti = 99
    
    for quantidade_de_minas in range(Quanti):
        Coord_mina = choice(List_coord)
        List_coord.remove(Coord_mina)
        Atributos = obtem_atributos(Coord_mina[0], Coord_mina[1], Tab_copia)
        Tab_copia[Coord_mina] = [mina()] + Atributos[1:] 

    return Tab_copia


def tab_para_str(Tab):
    Tam = int(sqrt(len(Tab)))
    Tab_str = "        "

    for ind_col in range(1, Tam + 1):   # numeros de cima 
        Tab_str += "  " + chr(64 + ind_col) + " "

    Tab_str += "\n        ."    # inicio da linha de cima 

    for ind_col in range(1, Tam + 1):   # linha de cima 
        if ind_col != Tam:
            Tab_str += "___ "
        else:
            Tab_str += "___."

    Tab_str += "\n"

    for ind_lin in range(1, Tam + 1):   # linhas do tab
        if ind_lin < 10:
            Tab_str += "      " + str(ind_lin) + "	|"
        else:
            Tab_str += "     " + str(ind_lin)+ "	|"

        for ind_col in range(1, Tam + 1):  # parte de cima de cada linha 
            if verifica_por_ver(obtem_estado(ind_lin, ind_col, Tab)):
                Tab_str += " _ |"
            elif(
                verifica_visto(obtem_estado(ind_lin, ind_col, Tab)) 
                and verifica_mina(obtem_conteudo(ind_lin, ind_col, Tab))
                ):    
                Tab_str += " ó*|"
            elif(
                verifica_visto(obtem_estado(ind_lin, ind_col, Tab)) 
                and obtem_minas_viz(ind_lin, ind_col, Tab) == 0
                ):
                Tab_str += "   |"
            elif verifica_bandeira(obtem_estado(ind_lin, ind_col, Tab)):
                Tab_str += " |p|"
            else:
                Tab_str += " " + str(obtem_minas_viz(ind_lin, ind_col, Tab)) + " |"

        Tab_str += " " + str(ind_lin) + "\n" + "        |"

        for ind_col in range(1, Tam + 1):   # parte de baixo de cada linha 
            Tab_str += "___|"
        
        Tab_str += "\n"
        
    Tab_str += "        *"   # inicio linha de baixo

    for ind_col in range(1, Tam + 1):   # linha de baixo
        if ind_col != Tam:
            Tab_str += "    "
        else:
            Tab_str += "   *"

    Tab_str += "\n        "

    for ind_col in range(1, Tam + 1):   # numeros de baixo
        Tab_str += "  " + chr(64 + ind_col) + " "

    return Tab_str

def varifica_fim(Tab, Tam):
    Cont = 0

    if Tam == 10:
        Quanti = 10
    elif Tam == 18:
        Quanti = 40
    else:
        Quanti = 99

    List_coord = list(Tab)
    for coord in List_coord:
        if verifica_por_ver(obtem_estado(coord[0], coord[1], Tab)) or verifica_bandeira(obtem_estado(coord[0], coord[1], Tab)):
            Cont += 1 

    return Cont == Quanti


def jogada(Lin, Col, Tab):  

    Tab_copia = Tab.copy()
    Atributos = obtem_atributos(Lin, Col, Tab_copia)
    Tam = int(sqrt(len(Tab)))

    Tab_copia[(Lin, Col)] = [Atributos[0]] + [visto()] + [Atributos[2]]

    if obtem_minas_viz(Lin, Col, Tab_copia) == 0:
        Vizinhanca = vizinhanca_reduzida(Lin, Col, Tam)

        for coord in Vizinhanca:

            if(
                obtem_minas_viz(coord[0], coord[1], Tab_copia) == 0 
                and verifica_por_ver(obtem_estado(coord[0], coord[1], Tab_copia))
                ):
                Tab_copia[(coord[0], coord[1])] = [Atributos[0]] + [visto()] + [Atributos[2]]
                Vizinhanca_da_Viz = vizinhanca_reduzida(coord[0], coord[1], Tam)
                for ele in Vizinhanca_da_Viz:
                    if ele not in Vizinhanca:
                        Vizinhanca += [ele]

            elif(
                obtem_minas_viz(coord[0], coord[1], Tab_copia) != 0 
                and verifica_por_ver(obtem_estado(coord[0], coord[1], Tab_copia))
                ):
                Atributos_viz = obtem_atributos(coord[0], coord[1], Tab_copia)
                Tab_copia[(coord[0], coord[1])] = [Atributos_viz[0]] + [visto()] + [Atributos_viz[2]]
    
    return Tab_copia
                

def str_para_coord(Str):
    if(
       ord(Str[-1]) >= 97 
       and ord(Str[-1]) <= 122
       ):
        return (int(Str[:-1]), int(ord(Str[-1])-96))
    else:
        return (int(Str[:-1]), int(ord(Str[-1])-64))
    

def clear():
    system("clear") # if windows put cls in clear    
    

def comeca_jogo():
    clear()
    print("\t      ___     _____     _____-----------_____     _____     ___\
          \n\t     .-__*---*_____*---*------| <*º*> |------*---*_____*---*__-.\
          \n\t   ./*        -----                               -----    _   *\.\
          \n\t   /*   __    __ __ ___  __ ____                         _/ *   *\ \
          \n\t   |    ||\  /|| || ||"+chr(92)+chr(92)+" || ||      _       _  _  _     /  \     |\
          \n\t*-|     ||"+chr(92)+chr(92)+"//|| || || "+chr(92)+chr(92)+"|| ||--   (_'|  |||_)|_ |_)   |    |     |-*\
          \n\t   |    || \/ || || ||  \|| ||__    _)\/\/||  |_ |\     \__/     |\
          \n\t  *\.  ______________________________________________________  ./*\
          \n\t   *\.________________________________________________________./*\
          \n\t        *\---------------______/|*º*|\______--------------/* \n\n\
          \t\t.__________________________________.\
          \n\t\t\t |        _ ___ _     _  _  _  _  |\
          \n\t\t\t|  | |\ |(_  | |_)| ||  | ||_ (_   |\
          \n\t\t\t|  | | \| _) | |\ |_||_ |_||_  _)  |\
          \n\t\t\t |__________________´_____________|\
          \n\t\t\t*                                 *\
          \n\t=>Escolha as coordenadas do espaço que quer libertar da seguinte forma: LC\
          \n\t\tCom L sendo o numero da linha e C oa letra da coluna ex.: =>12A\
          \n\t\tSe quiserem por uma bandeira adicionam um B ex.: B12A\n")
    
    Dif = str(input("\t\t\tEscolhe uma das dificuldades do jogo\
                    \n\t\t\t     facil | media | dificil\n=>" ))

    if Dif == "facil" or Dif == "FACIL":
        Tab = adiciona_contagem_minas(adiciona_minas(cria_tab(10)))
    elif Dif == "media" or Dif == "MEDIA":
        Tab = adiciona_contagem_minas(adiciona_minas(cria_tab(18)))
    elif Dif == "dificil" or Dif == "DIFICIL":
        Tab = adiciona_contagem_minas(adiciona_minas(cria_tab(24)))
    else:
        print("dificuldade não definida")
        comeca_jogo()
    
    clear()
    jogo(Tab)


def jogo(Tab):
    Tam = int(sqrt(len(Tab)))
    Condi = True

    while Condi:

        if varifica_fim(Tab, Tam):
            print("\t\t\t.____________________________.\
                  \n\t\t\t |     _      _  _  _ ___ _ |\
                  \n\t\t\t| \  /|_ |\ ||  |_ (_  | |_  |\
                  \n\t\t\t|  \/ |_ | \||_ |_  _) | |_  |\
                  \n\t\t\t |__________________________|\
                  \n\t\t\t*                            *")
            Condi = False

        else:
            print(tab_para_str(Tab) + "\n")
            Coord_str = str(input("=>"))

            if Coord_str[0] == "B" or Coord_str[0] == "b":
                try:
                    Coord = str_para_coord(Coord_str[1:])
                except ValueError:
                    print("coordenada não valida")
                    clear()
                    jogo(Tab)

                if verifica_bandeira(obtem_estado(Coord[0], Coord[1], Tab)):
                    Atributos = obtem_atributos(Coord[0], Coord[1], Tab)
                    Tab[(Coord[0], Coord[1])] = [Atributos[0]] + [por_ver()] + [Atributos[2]]
                    clear()
                    jogo(Tab)
                else:
                    if verifica_por_ver(obtem_estado(Coord[0], Coord[1], Tab)):
                        Atributos = obtem_atributos(Coord[0], Coord[1], Tab)
                        Tab[(Coord[0], Coord[1])] = [Atributos[0]] + [bandeira()] + [Atributos[2]]
                        jogo(Tab)
                    else:
                        print("coordenada não valida")
                        clear()
                        jogo(Tab)


            else:
                try:
                    Coord = str_para_coord(Coord_str)
                except ValueError:
                    clear()
                    print("coordenada não valida")
                    jogo(Tab)

                if not(verif_coord(Tam, Coord[0], Coord[1])):
                    clear()
                    print("coordenada não valida")
                    jogo(Tab)

                elif verifica_bandeira(obtem_estado(Coord[0], Coord[1], Tab)):
                    clear()
                    print("coordenada não valida")
                    jogo(Tab)

                elif verifica_mina(obtem_conteudo(Coord[0], Coord[1], Tab)):
                    Atributos = obtem_atributos(Coord[0], Coord[1], Tab)
                    Tab[(Coord[0], Coord[1])] = [Atributos[0]] + [visto()] + [Atributos[2]]
                    clear()
                    print(tab_para_str(Tab) + "\n")
                    print("\t\t\t.____________________________.\
                          \n\t\t\t |  _  _  _  _  _  _ ___  _ |\
                          \n\t\t\t|  |_)|_ |_)| \|_ (_  |  |_  |\
                          \n\t\t\t|  |  |_ |\ |_/|_  _) |  |_  |\
                          \n\t\t\t |__________________________|\
                          \n\t\t\t*                            *")
                    Condi = False

                elif verifica_visto(obtem_estado(Coord[0], Coord[1], Tab)):
                    clear()
                    print("coordenada não valida")
                    jogo(Tab)

                else:
                    Tab1 = jogada(Coord[0], Coord[1], Tab)
                    clear()
                    jogo(Tab1)
                

comeca_jogo()
