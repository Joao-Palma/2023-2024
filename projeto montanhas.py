def eh_territorio(arg: any) -> bool:
    """
    Verifica se o argumento é um território válido.

    Args:
        arg: O argumento a ser verificado.

    Returns:
        bool: True se o argumento for um território válido, False caso contrário.
    """

    if (type(arg) != tuple or len(arg) < 1 or len(arg) > 26
    ):  # verifica que o argumento é um tuplo e que tem pelo menos 1 elemento/coluna e não mais do que 26
        return False
    
    if type(arg[0]) == tuple:   # verifica que os elementos do argumento (colunas) são tuplos 

        if len(arg[0]) < 1 or len(arg[0]) > 99:   # verifica que as colunas do terreno têm pelo menos 1 elemento/linha e no maximo 99
            return False
        
        for coluna in arg:  # vai passar por todas as colunas do terreno
        
            if type(coluna) != tuple:   # verifica se a coluna não é um tuplo
                return False
            
            for elemento_coluna in coluna:

                if (type(elemento_coluna) != int or (elemento_coluna != 1 and elemento_coluna != 0)
                ):  # dentro da coluna que está a ser avaliada verifica se os seus elementos são do tipo inteiro com o valor vazio (0) ou se tem uma montanha (1)    
                    return False
                
        for ind_coluna in range(len(arg) - 1):    # passa pelo indice de todas as colunas (menos a ultima para não causar index error)

            if (len(arg[ind_coluna]) != len(arg[ind_coluna + 1])):   # verifica que o comprimento de uma coluna é igual ao da coluna seguinte 
                return False
            
        return True
    
    else:  # caso o argumento seja apenas uma coluna e não esteja esta coluna contida num tuplo
        return False


def obtem_ultima_intersecao(t: tuple) -> tuple:
    """
    Recebe um território e devolve a intersecao do extremo superior direito do território.

    Args:
        t: O território do qual se deseja obter a interseção do extremo superior direito.

    Returns:
        tuple: A interseção do extremo superior direito do território.
    """ 

    if eh_territorio(t):
        return (chr(64 + len(t)), len(t[0]))    # verifica o número de colunas e obtem o a letra correspondente à ultima e o número da ultima linha


def eh_intersecao(arg: any) -> bool:
    """
    Recebe um argumento e devolve True se o seu argumento corresponde a uma interseção e False caso contrario.

    Args:
        arg: O argumento a ser verificado.

    Returns:
        bool: True se o argumento corresponde a uma interseção, False caso contrário.
    """

    if (
        type(arg) != tuple
        or len(arg) != 2
        or type(arg[0]) != str
        or type(arg[1]) != int
        or len(arg[0]) != 1
        or arg[0] < "A"
        or arg[0] > "Z"
        or arg[1] < 1
        or arg[1] > 99
    ):    # verifica se a interseção não tem apenas 2 elementos de um caracter ou que estes não são uma letra maiuscula nem número inteiro maior que 0 e menor que 100
        return False
    
    return True


def eh_intersecao_valida(t:tuple, i:tuple) -> bool:
    """
    Recebe um território e uma interseção, e devolve True se a
    interseção corresponde a uma interseção do território, e False caso contrário.

    Args:
        t: O território a ser verificado.
        i: A interseção a ser verificada.

    Returns:
        bool: True se a interseção corresponde a uma interseção válida no território, False caso contrário.
    """

    if (len(t) < ord(i[0]) - 64 or len(t[0]) < i[1]
    ):  # verifica se a ind_coluna e a linha da interceção se encontram dentro dos limites do território
        return False
    
    return True


def eh_intersecao_livre(t:tuple, i:tuple) -> bool:
    """
    Recebe um território e uma interseção do território, e devolve True se a interseção corresponde a uma interseção livre (não ocupada por montanhas) dentro do território e False caso contrário.

    Args:
        t: O território a ser verificado.
        i: A interseção a ser verificada.

    Returns:
        bool: True se a interseção corresponde a uma interseção livre, False caso contrário.
    """

    if t[ord(i[0]) - 65][i[1] - 1] == 1:  # obtem as cordenadas da interseção e verifica se o seu conteudo é um 1 (não esta vazio)
        return False
    
    return True


def obtem_intersecoes_adjacentes(t:tuple, i:tuple) -> tuple:
    """
    Recebe um território e uma interseção do território, e devolve o tuplo formado pelas interseções válidas adjacentes à interseção em ordem de leitura de um território.

    Args:
        t: O território a ser verificado.
        i: A interseção da qual se desejam obter as interseções adjacentes.

    Returns:
        tuple: O tuplo contendo as interseções adjacentes válidas à interseção dada.
    """

    i_adja = ()
    index_coluna = ord(i[0]) - 65
    index_linha = i[1] - 1

    if index_linha != 0:  # verifica se existe alguma linha abaixo da interseção
        i_adja += ((i[0], index_linha),)  # interseção abaixo

    if index_coluna != 0:  # verifica se existe alguma ind_coluna à esquerda da interseção
        i_adja += ((chr(index_coluna + 64), index_linha + 1),)     # interseção à esquerda

    if index_coluna != len(t) - 1:  # verifica se existe alguma ind_coluna à direita da interseção
        i_adja += ((chr(index_coluna + 66), index_linha + 1),)     # interseção à direita

    if index_linha != len(t[0]) - 1:    # verifica se existe alguma linha em cima da interseção
        i_adja += ((i[0], index_linha + 2),)    # interseção em cima

    return i_adja


def ordena_intersecoes(tup:tuple) -> tuple:
    """
    Recebe um tuplo de interseções (potencialmente vazio) e devolve um tuplo contendo as mesmas interseções ordenadas de acordo com a ordem de leitura do território.

    Args:
        tup: O tuplo de interseções a ser ordenado.

    Returns:
        tuple: O tuplo contendo as interseções ordenadas.
    """

    def ordem_por_linhas(tup:tuple) -> int:
        """
        Função auxiliar que devolve o número da linha da interseção

        Args:
            tup: O tuplo de interseções a ser ordenado.

        Returns:
            int: O número da linha da interseção.
        """

        return tup[1]

    lst_ord_por_colunas = sorted(tup)    # ordena o tuplo por colunas (esquerda para a direita)

    return tuple(sorted(lst_ord_por_colunas, key=ordem_por_linhas))    # ordena e devolve o tuplo com as colunas organizadas em relação as linhas (baixo para cima)


def territorio_para_str(t:tuple) -> str:
    """
    Recebe um território e devolve a cadeia de caracteres que o representa (a representação externa ou representação “para os nossos olhos”).

    Args:
        t: O território a ser representado como uma cadeia de caracteres.

    Returns:
        str: A representação do território em forma de cadeia de caracteres.
    """

    str_territorio = ""
    str_letr_coluns = "   "

    if not eh_territorio(t):  # verifica a validade do input
        raise ValueError("territorio_para_str: argumento invalido")
    
    for ind_colun in range(len(t)):    # passa pelos indices de todas as ind_colunas (tuplos) do terreno

        if ind_colun != len(t) - 1:
            str_letr_coluns += chr(65 + ind_colun) + " "    # adiciona a letra indicadora da ind_coluna e um espaço

        else:  # se a coluna for a ultima não se adiciona um espaço
            str_letr_coluns += chr(65 + ind_colun)
    
    str_territorio += str_letr_coluns + "\n"    # adiciona o nome das ind_colunas ao string "final" e muda de linha

    for elem_linha in range(len(t[0]), 0, -1):    # vai passsar pelas linhas de baixo para cima
        
        if elem_linha < 10:  # verifica se o número tem 1 dígito para adicionar um espaço a mais, depois adiciona o número da linha atual
            str_territorio += " " + str(elem_linha)

        else:  # caso tenho o número tenha 2 digitos não adiciona espaço
            str_territorio += str(elem_linha)

        for ind_coluna in range(len(t)):    # dentro da linha que está a ser avaliada vai passar por todas as ind_colunas

            if t[ind_coluna][elem_linha - 1] == 1:  # caso o elemento da linha e ind_coluna atual seja 1(montanha) adiciona um espaço e X
                str_territorio += " X"

            else:  # caso o elemento da linha e ind_coluna atual seja 0 adiciona um espaço e .
                str_territorio += " ."

        if elem_linha < 10:  # verifica se o número tem 1 dígito para adicionar um espaço a mais, depois adiciona o número da linha atual e muda de linha
            str_territorio += "  " + str(elem_linha) + "\n"

        else:  # caso tenho o número tenha 2 digitos não adiciona o espaço extra e muda de linha
            str_territorio += " " + str(elem_linha) + "\n"

    str_territorio += str_letr_coluns   # por fim volta a adicionar o indicador de ind_colunas

    return str_territorio


def obtem_cadeia(t:tuple, i:tuple) -> tuple:
    """
    Recebe um território e uma interseção do território (ocupada por uma montanha ou livre),\n e devolve o tuplo formado por todas as interseções que estão conectadas (e do mesmo tipo) a essa interseção, ordenadas.

    Args:
        t: O território do qual se deseja obter as interseções conectadas.
        i: A interseção da qual se deseja começar a busca.

    Returns:
        tuple: O tuplo contendo as interseções conectadas (do mesmo tipo) à interseção dada, ordenadas.
    """

    if (
        not eh_territorio(t) 
        or not eh_intersecao(i) 
        or not eh_intersecao_valida(t, i)
    ):
        raise ValueError("obtem_cadeia: argumentos invalidos")

    valor_i = t[ord(i[0]) - 65][i[1] - 1]
    tup_adj_aux = ()
    tup_adj_i = ()
    tup_adj_atuais = ()
    tup_cadei = (i,)

    for i_adja in obtem_intersecoes_adjacentes(t, i):   # passa por todas as interseções 

        if (t[ord(i_adja[0]) - 65][i_adja[1] - 1] == valor_i
        ):    # verifica se o valor da interseção a ser avaliada é igual ao valor da interseção fornecida 
            tup_adj_i += (i_adja,)
            tup_cadei += (i_adja,)

    tup_adj_atuais = tup_adj_i

    while (tup_adj_atuais):  # verifica que ainda existem interseções adjacentes a analisar

        for (elem) in (tup_adj_atuais):  # escolhe uma interseção das adjacentes aos pontos da cadeia

            for adja in obtem_intersecoes_adjacentes(t, elem):  # recolhe as interseções adjacentes a esta

                if t[ord(adja[0]) - 65][adja[1] - 1] == valor_i:  # avalia se esta interseção tem o mesmo valor que a interseção recebida
                    
                    if adja not in tup_cadei:  # caso esta interseção ainda não esteja no conjunto da cadeias adicionamo-la 
                        tup_cadei += (adja,)
                        tup_adj_aux += (adja,)  # adiciona esta interseção para ser verificada no proximo ciclo while

        tup_adj_atuais = tup_adj_aux
        tup_adj_aux = ()

    return ordena_intersecoes(tup_cadei)


def obtem_vale(t:tuple, i:tuple) -> tuple:
    """
    Recebe um território e uma interseção do território ocupada por uma montanha, e devolve o tuplo (potencialmente vazio) formado por todas as interseções que formam parte do vale da montanha da interseção fornecida como argumento, ordenadas.

    Args:
        t: O território que contém a montanha e o vale.
        i: A interseção ocupada por uma montanha a partir da qual se deseja encontrar os vale.

    Returns:
        tuple: O tuplo contendo as interseções que formam parte do vale da montanha.
    """

    if (
        not eh_territorio(t)
        or not eh_intersecao(i)
        or not eh_intersecao_valida(t, i)
        or t[ord(i[0]) - 65][i[1] - 1] != 1
    ): 
        raise ValueError("obtem_vale: argumentos invalidos")
    
    cadeia = obtem_cadeia(t, i)  # obtém a cadeia da montanha fornecida
    val_adj = ()

    for inter in cadeia:  # passa pelas interseção da cadeia

        for inter_adj in obtem_intersecoes_adjacentes(t, inter):    # passa pelas interseções adjacentes à interseção anterior
            
            if t[ord(inter_adj[0]) - 65][inter_adj[1] - 1] == 0:

                if inter_adj not in val_adj:  # caso o vale não esteja ainda no tuplo dos vales
                    val_adj += (inter_adj,)

    return ordena_intersecoes(val_adj)  # devolve o conjunto de vales organizados


def verifica_conexao(t:tuple, i1:tuple, i2:tuple) -> bool:
    """
    Recebe um território e duas interseções do território e devolve True se as duas interseções estão conectadas e False caso contrário.

    Args:
        t: O território a ser verificado.
        i1: A primeira interseção.
        i2: A segunda interseção.

    Returns:
        bool: True se as duas interseções estão conectadas, False caso contrário.
    """

    if (
        not eh_territorio(t)
        or not eh_intersecao(i1)
        or not eh_intersecao(i2)
        or not eh_intersecao_valida(t, i1)
        or not eh_intersecao_valida(t, i2)
    ):
        raise ValueError("verifica_conexao: argumentos invalidos")
    
    int_adjs = obtem_cadeia(t, i1)  # cria tuplo com todas as interseções conectadas a i1
    
    if i2 in int_adjs:
        return True
    
    return False


def calcula_numero_montanhas(t:tuple) -> int:
    """
    Recebe um território e devolve o número de interseções ocupadas por montanhas no território.

    Args:
        t: O território a ser verificado.

    Returns:
        int: O número de interseções ocupadas por montanhas no território.
    """

    if not eh_territorio(t):
        raise ValueError("calcula_numero_montanhas: argumento invalido")
    
    cont = 0
    
    for coluna in t:  # passa por todas as colunas do território

        for elem in coluna:  # passa por todos os elementos da coluna
        
            if elem == 1:
                cont += 1  # adiciona 1 à contagem de montanhas

    return cont


def aux_obtem_monts(t:tuple) -> tuple:  # função auxiliar
    """
    Recebe um território e devolve um tuplo com todas as montanhas.

    Args:
        t: O território a ser verificado.

    Returns:
        tuple: O tuplo que contem todas as montanhas.
    """
    tup_todos_mont = ()

    for ind_coluna in range(len(t)):  # passa por todos os indices de colunas do território
        
        for ind_linha in range(len(t[ind_coluna])):  # passa pelos índices de linhas da coluna a ser avaliada

            if t[ind_coluna][ind_linha] == 1:  # verifica se esta interseção tem valor 1
                tup_todos_mont += ((chr(65 + ind_coluna), ind_linha + 1),)  # adiciona as coordenadas da interseção em formato (str,int) ao tuplo com todas as montanhas

    return ordena_intersecoes(tup_todos_mont)  # ordena o tuplo


def calcula_numero_cadeias_montanhas(t:tuple) -> int:
    """
    Recebe um território e devolve o número total de cadeias de montanhas.

    Args:
        t: O território a ser verificado.

    Returns:
        int: O número total de cadeias de montanhas.
    """

    if not eh_territorio(t):
        raise ValueError("calcula_numero_cadeias_montanhas: argumento invalido")
    
    mont_em_cade = ()
    cont_cadei = 0
    tup_todos_mont = aux_obtem_monts(t)
    
    for mont in tup_todos_mont:  # passa por todas as montanhas do terreno
        
        if mont not in mont_em_cade:  # caso a montanha não pertença a nenhuma das cadeias analizadas
            mont_em_cade += obtem_cadeia(t, mont)  # adiciona-se a cadeia de montanhas ao tuplo com as cadeias já analizadas
            cont_cadei += 1  # adicionamos 1 à contagem das cadeias

            if mont_em_cade == tup_todos_mont:  # caso os elementos das cadeias avaliadas sejam todas as montanhas acabamos o ciclo for
                break

    return cont_cadei


def calcula_tamanho_vales(t:tuple) -> int:
    """
    Recebe um território e devolve o número total de interseções diferentes que formam todos os vales do território.

    Args:
        t: O território a ser verificado.

    Returns:
        int: O número total de interseções que formam todos os vales do território
    """

    if not eh_territorio(t):
        raise ValueError("calcula_tamanho_vales: argumento invalido")
    
    cont_vales = 0
    tup_todos_vales = ()
    tup_todas_mont = aux_obtem_monts(t)
    
    for mont in tup_todas_mont:  # passa por todas as montanhas do terreno
    
        for inter in obtem_vale(t, mont):  # passa pelos vales da montanha a ser avaliada
            
            if inter not in tup_todos_vales:  # caso este vale ainda não tivesse sido encontrado
                tup_todos_vales += (inter,)  # adiciona este vale ao tuplo com todos os vales
                cont_vales += 1  # aumenta a contagem de vales

    return cont_vales