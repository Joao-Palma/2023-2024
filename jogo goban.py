# TAD intersecao #

def cria_intersecao(col: any,lin: any)-> tuple:
    """
    Recebe uma letra maiúscula e um inteiro correspondentes à coluna e à linha da interseção do tabuleiro e devolve a interseção correspondente.

    Args:
        col: Uma letra maiúscula entre 'A' e 'S' representando a coluna da interseção do tabuleiro.
        lin: Um inteiro entre 1 e 19 representando a linha da interseção do tabuleiro.

    Returns:
        tuple: Um tuplo (col, lin) representando a interseção do tabuleiro, onde col é uma string e lin é um inteiro.

    Raises:
        ValueError: Se os argumentos não estiverem de acordo com os requisitos.

    Exemplo:
        >>> cria_intersecao('C', 5)
        ('C', 5)
    """

    if (
        type(lin) != int
        or type(col) != str
        or len(col) > 1
        or  col < "A"
        or  col > "S"
        or  lin < 1
        or  lin > 19
    ):  # verifica se a coluna é uma letra maiuscula entre A e S e que a linha é um inteiro entre 1 e 19 
        raise ValueError("cria_intersecao: argumentos invalidos")
    
    return (col,lin)
    

def obtem_col(i: tuple) -> str:
    """
    Recebe uma interseção i e devolve a sua coluna.
    
    Args:
        i (tuple): Interseção do tabuleiro

    Returns:
        str: Uma string que representa a coluna da interseção.

    Exemplo:
        >>> obtem_col(('B', 7))
        'B'
    """

    return i[0]


def obtem_lin(i: tuple) -> int:
    """
    Recebe uma interseção i e devolve a sua linha.
    
    Args:
        i (tuple): Interseção do tabuleiro

    Returns:
        int: valor inteiro da linha da interseção

    Exemplo:
        >>> obtem_col(('B', 7))
        7    
    """

    return i[1]


def eh_intersecao(arg: any) -> bool:
    """
    Recebe um argumento devolve True caso este seja uma intersecao
    e False caso contrário.
    
    Args:
        arg: Argumento que vai ser validado

    Returns:
        bool: True caso o arg seja uma interseção válida False caso contrário 

    Exemplos:
        >>> eh_intersecao(('B', 7))
        True
        >>> eh_intersecao(('Z', 30))
        False
        >>> eh_intersecao('A1')
        False
    """

    if type(arg) != tuple: 
        return False
    
    try:    # verifica se os elementos do tuplo são válidos 
        cria_intersecao(obtem_col(arg),obtem_lin(arg))
        return True
    except ValueError:
        return False


def intersecoes_iguais(i1: any,i2: any) -> bool:
    """
    Recebe duas interseções e devolve True apenas se i1 e i2 forem interseções
    iguais, e False caso contrário.

    Args:
        i1: Uma interseção do tabuleiro
        i2: Uma interseção do tabuleiro

    Returns:
        bool: True caso as interseções sejam iguais False caso contrário
    
    Exemplos:
        >>> intersecoes_iguais(('B', 7), ('B', 7))
        True
        >>> intersecoes_iguais(('C', 5), ('D', 5))
        False
        >>> intersecoes_iguais(('A', 1), ('B', 1))
        False
    """
    
    if (
        eh_intersecao(i1) 
        and 
        eh_intersecao(i2)
        ):   # verifica que as interseções são validas
        pass
    else:
        return False
    
    if (
        obtem_col(i1) == obtem_col(i2) 
        and 
        obtem_lin(i1) == obtem_lin(i2)
        ):  # verifica se as colunas is linhas são iguais nas duas interseções
        return True
    
    return False


def intersecao_para_str(i: tuple) -> str:
    """
    Recebe uma interseção e devolve a cadeia de caracteres que a representa.
    
    Args:
        i (tuple): O tuplo que representa a interseção

    Returns:
        str: O string que representa a interseção

    Exemplo:
        >>> intersecao_para_str(('B', 7))
        'B7'
    """

    return obtem_col(i) + str(obtem_lin(i))


def str_para_intersecao(s: str) -> tuple:
    """
    Recebe uma cadeia e devolve a interseção que a representa.
    
    Args:
        s (str): O string que representa a interseção

    Returns:
        tuple: O tuplo que representa a interseção

    Exemplo:
        >>> str_para_intersecao('B7')
        ('B', 7)
    """

    return cria_intersecao(s[0],int(s[1:]))


def obtem_intersecoes_adjacentes(i: tuple, l:tuple) -> tuple:
    """
    devolve um tuplo com as interseções adjacentes
    à interseção i de acordo com a ordem de leitura em que l corresponde à interseção
    superior direita do tabuleiro de Go.

    Args:
        i (tuple): A interseção da qual se desejam obter as interseções adjacentes.
        l (tuple): A interseção do canto superior direito

    Returns:
        tuple: O tuplo contendo as interseções adjacentes válidas à interseção dada.

    Exemplo:
        >>> obtem_intersecoes_adjacentes(('B', 7), ('S', 19))
        (('B', 6), ('A', 7), ('C', 7), ('B', 8))
    """

    tup_inters_adja = ()

    if obtem_lin(i) != 1:   # verifica se existe alguma linha abaixo da interseção
        tup_inters_adja += (cria_intersecao(obtem_col(i),obtem_lin(i) - 1),)    # interseção abaixo

    if obtem_col(i) != "A":    # verifica se existe alguma coluna à esquerda da interseção
        tup_inters_adja += (cria_intersecao(chr(ord(obtem_col(i)) - 1),obtem_lin(i)),)    # interseção à esquerda

    if obtem_col(i) != obtem_col(l):    # verifica se existe alguma coluna à direita da interseção
        tup_inters_adja += (cria_intersecao(chr(ord(obtem_col(i)) + 1),obtem_lin(i)),)    # interseção à direita

    if obtem_lin(i) != obtem_lin(l):    # verifica se existe alguma linha em cima da interseção
        tup_inters_adja += (cria_intersecao(obtem_col(i),obtem_lin(i) + 1),)    # interseção em cima

    return tup_inters_adja


def ordena_intersecoes(t: tuple) -> tuple:
    """
    Recebe um tuplo de interseções (potencialmente vazio) e devolve um tuplo contendo as mesmas interseções ordenadas de acordo com a ordem de leitura do  tabuleiro de Go.

    Args:
        t (tuple): O tuplo de interseções a ser ordenado.

    Returns:
        tuple: O tuplo contendo as interseções ordenadas.

    Exemplo:
        >>> ordena_intersecoes((('C', 5), ('A', 7), ('D', 5)))
        (('A', 7), ('C', 5), ('D', 5))
    """

    def ordem_por_linhas(t:tuple) -> int:
        """
        Função auxiliar que devolve o número da linha da interseção

        Args:
            t (tuple): O tuplo de interseções a ser ordenado.

        Returns:
            int: O número da linha da interseção.
        """

        return obtem_lin(t)

    lst_ord_por_colunas = sorted(t)    # ordena o tuplo por colunas (esquerda para a direita)

    return tuple(sorted(lst_ord_por_colunas, key=ordem_por_linhas))    # ordena e devolve o tuplo com as colunas organizadas em relação as linhas (baixo para cima)


# TAD pedra #

def cria_pedra_branca() -> str:
    """
    Cria e retorna uma pedra branca.

    Returns:
        str: Uma string representando uma pedra branca.

    Exemplo:
        >>> pedra = cria_pedra_branca()
        >>> print(pedra)
        'branca'
    """
    return "branca"


def cria_pedra_preta() -> str:
    """
    Cria e retorna uma pedra preta.

    Returns:
        str: Uma string representando uma pedra preta.

    Exemplo:
        >>> pedra = cria_pedra_preta()
        >>> print(pedra)
        'preta'
    """

    return "preta"


def cria_pedra_neutra() -> str:
    """
    Cria e retorna uma pedra neutra.

    Returns:
        str: Uma string representando uma pedra neutra.

    Exemplo:
        >>> pedra = cria_pedra_neutra()
        >>> print(pedra)
        'neutra'
    """
        
    return "neutra"


def eh_pedra(arg: any) -> bool:
    """
    Verifica se o argumento é uma pedra válida (branca, neutra ou preta).

    Args:
        arg: O argumento a ser verificado.

    Returns:
        bool: True se o argumento for uma pedra válida, False caso contrário.

    Exemplo:
        >>> pedra_branca = cria_pedra_branca()
        >>> pedra_neutra = cria_pedra_neutra()
        >>> pedra_preta = cria_pedra_preta()

        >>> eh_pedra(pedra_branca)
        True
        >>> eh_pedra(pedra_neutra)
        True
        >>> eh_pedra(pedra_preta)
        True
        >>> eh_pedra("outra_coisa")
        False
    """

    if arg in (cria_pedra_branca(), cria_pedra_neutra(), cria_pedra_preta()): 
        return True

    return False 


def eh_pedra_branca(arg: any) -> bool:
    """
    Verifica se o argumento é uma pedra branca.

    Args:
        arg: O argumento a ser verificado.

    Returns:
        bool: True se o argumento for uma pedra branca, False caso contrário.

    Exemplo:
        >>> pedra_branca = cria_pedra_branca()
        >>> outra_pedra_branca = cria_pedra_branca()

        >>> eh_pedra_branca(pedra_branca)
        True
        >>> eh_pedra_branca(outra_pedra_branca)
        True
        >>> eh_pedra_branca(cria_pedra_neutra())
        False
        >>> eh_pedra_branca("outra_coisa")
        False
    """

    if arg == cria_pedra_branca():
        return True
    
    return False


def eh_pedra_preta(arg: any) -> bool:
    """
    Verifica se o argumento é uma pedra preta.

    Args:
        arg: O argumento a ser verificado.

    Returns:
        bool: True se o argumento for uma pedra preta, False caso contrário.

    Exemplo:
        >>> pedra_preta = cria_pedra_preta()
        >>> outra_pedra_preta = cria_pedra_preta()

        >>> eh_pedra_preta(pedra_preta)
        True
        >>> eh_pedra_preta(outra_pedra_preta)
        True
        >>> eh_pedra_preta(cria_pedra_neutra())
        False
        >>> eh_pedra_preta("outra_coisa")
        False
    """
    if arg == cria_pedra_preta():
        return True
    
    return False


def pedras_iguais(p1,p2) -> bool:
    """
    Verifica se duas pedras são iguais.

    Args:
        p1: A primeira pedra.
        p2: A segunda pedra.

    Returns:
        bool: True se as duas pedras forem iguais, False caso contrário.

    Exemplo:
        >>> pedra_branca = cria_pedra_branca()
        >>> outra_pedra_branca = cria_pedra_branca()
        >>> pedra_neutra = cria_pedra_neutra()
        
        >>> pedras_iguais(pedra_branca, outra_pedra_branca)
        True
        >>> pedras_iguais(pedra_branca, pedra_neutra)
        False
    """
    if p1 == p2:
        return True
    
    return False

def pedra_para_str(p) -> str:
    """
    Converte uma pedra em uma representação de string.

    Args:
        p: A pedra a ser convertido.

    Returns:
        str: A representação em string da pedra.

    Exemplo:
        >>> pedra_branca = cria_pedra_branca()
        >>> pedra_preta = cria_pedra_preta()
        >>> pedra_neutra = cria_pedra_neutra()

        >>> pedra_para_str(pedra_branca)
        'O'
        >>> pedra_para_str(pedra_preta)
        'X'
        >>> pedra_para_str(pedra_neutra)
        '.'
    """
    if eh_pedra_branca(p):
        return "O"
    
    if eh_pedra_preta(p):
        return "X"
    
    if pedras_iguais(p,cria_pedra_neutra()):
        return "."

def eh_pedra_jogador(p) -> bool:
    """
    Verifica se a pedra é uma pedra de jogador (branca ou preta).

    Args:
        p: A pedra a ser verificado.

    Returns:
        bool: True se a pedra for uma pedra de jogador (branca ou preta), False caso contrário.

    Exemplo:
        >>> pedra_branca = cria_pedra_branca()
        >>> pedra_preta = cria_pedra_preta()
        >>> pedra_neutra = cria_pedra_neutra()
        
        >>> eh_pedra_jogador(pedra_branca)
        True
        >>> eh_pedra_jogador(pedra_preta)
        True
        >>> eh_pedra_jogador(pedra_neutra)
        False
        >>> eh_pedra_jogador("outra_coisa")
        False
    """
    if eh_pedra_preta(p) or eh_pedra_branca(p):
        return True
    
    return False

# TAD goban #

def cria_goban_vazio(n: int) -> dict:
    """
    Cria um tabuleiro vazio com um tamanho especificado.

    Args:
        n (int): Tamanho do tabuleiro. Deve ser 9, 13 ou 19.

    Returns:
        dict: Um dicionário representando o Goban vazio com interseções e pedras neutras.

    Raises:
        ValueError: Se o tamanho do tabuleiro não for 9, 13 ou 19.
    """
    if type(n) != int or n not in (9, 13, 19):    # verifica que o taboleiro tem um dos tamanhos validos e que n é inteiro
        raise ValueError("cria_goban_vazio: argumento invalido")
    
    goban = {}

    for linhas in range (1, n+1):   # cria as linhas
        for colunas in range (1, n+1):  # cria as colunas 
            goban[cria_intersecao(chr(colunas+64),linhas)] = cria_pedra_neutra()    # adicona um chave ao goban com valor de uma pedra neutra linha a linha

    return goban


def cria_goban(n: int, ib: tuple, ip: tuple) -> dict:
    """
    Cria um tabuleiro com o tamanho especificado, com pedras brancas e pretas nas interseções especificadas.

    Args:
        n (int): Tamanho do tabuleiro. Deve ser 9, 13 ou 19.
        ib (tuple): Tuplo contendo interseções para pedras brancas.
        ip (tuple): Tuplo contendo interseções para pedras pretas.

    Returns:
        dict: O tabuleiro com as interseções especificadas.

    Raises:
        ValueError: Se o tamanho do tabuleiro não for 9, 13 ou 19, se alguma interseção não estiver no tabuleiro ou se houverem interseções repetidas nos tuplos ib e ip.
    """
    try:
        goban = cria_goban_vazio(n)     # verifica que n é um tamanho válido
    except ValueError:
        raise ValueError('cria_goban: argumentos invalidos')
    
    if (type(ib) != tuple 
        or type(ip) != tuple 
        or len(set(ib)) != len(ib) 
        or len(set(ip)) != len(ip)
        ):  # verifica que ib e ip são ambos tuplos e não tem interseções repetidas
        raise ValueError('cria_goban: argumentos invalidos')

    for intersecao in ib:
        if intersecao in ip:    # verifica que não há interseções iguais nos tuplos ib e ip
            raise ValueError('cria_goban: argumentos invalidos')
        if not eh_intersecao_valida(goban,intersecao):   # verifica que a interseção é uma chave do dicionário goban
            raise ValueError('cria_goban: argumentos invalidos')
        goban[intersecao] = cria_pedra_branca()    # modifica o valor da chave (interseção) do tuplo 

    for intersecao in ip:
        if not eh_intersecao_valida(goban,intersecao):   # verifica que a interseção é uma chave do dicionário goban    
            raise ValueError('cria_goban: argumentos invalidos')
        goban[intersecao] = cria_pedra_preta()    # modifica o valor da chave (interseção) do tuplo 

    return goban


def cria_copia_goban(g: dict) -> dict:
    """
    Cria uma cópia do tabuleiro.

    Args:
        g (dict): O Goban original a ser copiado.

    Returns:
        dict: Uma cópia do tabuleiro original.
    """
    tup_todas = todas_as_intersecoes(g)    # obtem todas as interseções do tabuleiro
    dct_copia = {}  

    for inter in tup_todas:
        dct_copia[inter] = g[inter]    # copia a pedra que está na interseção do tabuleiro original 

    return dct_copia


def obtem_ultima_intersecao(g: dict) -> tuple:
    """
    Obtém a última interseção do tabuleiro com base no tamanho do tabuleiro.

    Args:
        g (dict): O tabuleiro do qual se deseja obter a última interseção.

    Returns:
        tuple: A última interseção do tabuleiro.
    """
    if len(g) / 9  == 9:    # se a divizão por 9 for igual a 9 logo o tabuleiro tem dimensão 9x9
        return cria_intersecao("I", 9)      # ultima interseção do tabuleiro 9x9
    
    if len(g) / 13  == 13:  # se a divizão por 13 for igual a 13 logo o tabuleiro tem dimensão 13x13
        return cria_intersecao("M", 13)      # ultima interseção do tabuleiro 13x13
    
    if len(g) / 19  == 19:  # se a divizão por 19 for igual a 19 logo o tabuleiro tem dimensão 19x19
        return cria_intersecao("S", 19)      # ultima interseção do tabuleiro 19x19


def obtem_pedra(g: dict, i: tuple) -> str:
    """
    Obtém o tipo de pedra em uma interseção específica no tabuleiro.

    Args:
        g (dict): O Goban no qual se deseja obter a pedra.
        i (tuple): Um tuplo da interseção.

    Returns:
        str: O tipo de pedra na interseção.
    """
    return g[i]


def obtem_cadeia(g: dict, i: tuple) -> tuple:
    """
    Obtém uma cadeia de pedras do mesmo tipo conectadas num tabuleiro a partir de uma interseção.

    Args:
        g (dict): O Goban no qual a interseção e a cadeia estão localizadas.
        i (tuple): a interseção inicial.

    Returns:
        tuple: Um tuplo com as interseções da cadeia.
    """
    pedra_i = obtem_pedra(g,i)
    tup_cadeia = (i,)
    tup_adj_atuais = ()    # interseções a serem avaliadas
    tup_adj_aux = ()
    tup_adj_i = ()     # interseções adjacentes a i com o seu valor 

    for intersecao in obtem_intersecoes_adjacentes(i, obtem_ultima_intersecao(g)):   # passa pelas interseções adjacentes a i 
        if pedras_iguais(obtem_pedra(g, intersecao), pedra_i):    # verifica que estas interseções são do mesmo "tipo" que a original
            tup_adj_i += (intersecao,)
            tup_cadeia += (intersecao,)

    tup_adj_atuais = tup_adj_i

    while (tup_adj_atuais):  # enquanto existirem interseções a serem avaliadas
        for intersecao in tup_adj_atuais:
            for inter_adj in obtem_intersecoes_adjacentes(intersecao, obtem_ultima_intersecao(g)):   # procurar as interseções adjacentes à que esta a ser analizada
                if pedras_iguais(obtem_pedra(g, inter_adj), pedra_i):  # verifica que a pedra tem o mesmo valor da pedra fornecida
                    if inter_adj not in tup_cadeia:   # verifica que a pedra ainda não esta na cadeia 
                        tup_cadeia += (inter_adj,)    
                        tup_adj_aux += (inter_adj,)    # adiciona ao tuplo dos quee cão ser adicionados ao proximo ciclo for

        tup_adj_atuais = tup_adj_aux    # atualiza as interseções a serem avaliadas
        tup_adj_aux = ()   

    return ordena_intersecoes(tup_cadeia)


def coloca_pedra(g: dict, i: tuple, p: str) -> dict:
    """
    Coloca uma pedra de um tipo específico numa interseção do tabuleiro.

    Args:
        g (dict): O tabuleiro no qual a pedra será colocada.
        i (tuple): A interseção na qual a pedra será colocada.
        p (str): O tipo de pedra a ser colocada.

    Returns:
        dict: O taboleiro atualizado com a pedra colocada na interseção especificada.
    """
    if eh_pedra_branca(p):
        g[i] = cria_pedra_branca()

    if eh_pedra_preta(p):
        g[i] = cria_pedra_preta()

    return g


def remove_pedra(g: dict, i: tuple) -> dict:
    """
    Remove uma pedra de uma interseção do tabuleiro, tornando a interseção neutra.

    Args:
        g (dict): O tabuleiro do qual a pedra será removida.
        i (tuple): A interseção da qual a pedra será removida.

    Returns:
        dict: O tabuleiro atualizado com a pedra removida.
    """
    g[i] = cria_pedra_neutra()

    return g

def remove_cadeia(g: dict, i: tuple):
    """
    Remove uma cadeia de pedras do tabuleiro.

    Args:
        g (dict): O tabuleiro do qual a cadeia de pedras será removida.
        i (tuple): Um tuplo com as interseções da cadeia a ser removida.

    Returns:
        dict: O tabuleriro atualizado com a cadeia de pedras removida.
    """
    for elementos in i:    # para cada elemento da cadeia
        remove_pedra(g, elementos)

    return g


def eh_goban(arg: any) -> bool:
    """
    Verifica se o argumento é um taboleiro válido.

    Args:
        arg (any): O objeto a ser verificado.

    Returns:
        bool: True se o argumento é um tabuleiro válido, False caso contrário.
    """
    if (type(arg) != dict 
        or len(arg) not in (81,169,361) 
        ):  # verifica que o goban tem a representação predefinida e um tamanho válido
        return False 
    
    for intersecao in arg:
        if not eh_intersecao(intersecao):
            return False
        if not eh_pedra(obtem_pedra(arg, intersecao)):
            return False
    return True
        
        
def eh_intersecao_valida(g: dict, i: tuple) -> bool:
    """
    Verifica se a interseção pertence ao tabuleiro.

    Args:
        g (dict): O tabuleiro no qual a interseção deve ser válida.
        i (tuple): A interseção a ser verificada.

    Returns:
        bool: True se a interseção é válida, False caso contrário.
    """
    if (
        not eh_goban(g) 
        or not eh_intersecao(i) 
        or obtem_col(i) > obtem_col(obtem_ultima_intersecao(g))    # verifica se a coluna é maior que a coluna da ultima interseção
        or obtem_lin(i) > obtem_lin(obtem_ultima_intersecao(g))    # verifica se a linah é maior que a linah da ultima interseção
        ):
        return False
    return True


def todas_as_intersecoes(g: dict) -> tuple:
    """
    função auxiliar que devolve todas as interseções de um tabuleiro

    Args:
        g (dict): tabuleiro do jogo 

    Returs:
        tuple: tuplo com todas as interseções do tabuleiro
    """
    
    n = obtem_lin(obtem_ultima_intersecao(g))   # dimensão do tabuleiro
    
    tup_final = ()

    for linhas in range (1, n+1):   # cria as linhas
        for colunas in range (1, n+1):   # cria as colunas 
            tup_final += (cria_intersecao(chr(colunas+64),linhas),)    # adiciona a interseção 

    return tup_final


def gobans_iguais(g1: dict, g2: dict) -> bool:
    """
    Verifica se dois tabuleiros são iguais com base nas suas representações em dicionário.

    Args:
        g1 (dict): O primeiro tabuleiro a ser comparado.
        g2 (dict): O segundo tabuleiro a ser comparado.

    Returns:
        bool: True se os dois tabuleiros tiverem a mesma configuração, False caso contrário.
    """
    if not intersecoes_iguais(obtem_ultima_intersecao(g1),obtem_ultima_intersecao(g2)):  # verifica que tem o mesmo comprimento antes: obtem_ultima_intersecao(g1) != obtem_ultima_intersecao(g2)
        return False
    
    inter_gs = todas_as_intersecoes(g1)

    for inter in inter_gs:
        if not pedras_iguais(obtem_pedra(g1,inter),obtem_pedra(g2,inter)):
            return False
    return True


def goban_para_str(g: dict) -> str:
    """
    Converte um tabuleiro do jogo numa representação em formato de string para exibição.

    Args:
        g (dict): O tabuleiro a ser convertido em string.

    Returns:
        str: A em formato de string do tabuleiro.
    """
    str_goban = ""
    str_letr_coluns = "   "

    for ind_coluna in range(ord(obtem_col(obtem_ultima_intersecao(g))) - 64):    # passa pelos indices de todas as ind_colunas (tuplos) do terreno
        if ind_coluna != ord(obtem_col(obtem_ultima_intersecao(g))) - 65:
            str_letr_coluns += chr(65 + ind_coluna) + " "    # adiciona a letra indicadora da ind_coluna e um espaço
        else:  # se a coluna for a ultima não se adiciona um espaço
            str_letr_coluns += chr(65 + ind_coluna)
    
    str_goban += str_letr_coluns + "\n"    # adiciona o nome das colunas ao string "final" e muda de linha

    for linha in range(obtem_lin(obtem_ultima_intersecao(g)), 0, -1):    # vai passsar pelas linhas de baixo para cima
        if linha < 10:  # verifica se o número da linha tem 1 dígito para adicionar um espaço a mais, depois adiciona o número da linha atual
            str_goban += " " + str(linha)
        else:  # caso tenho o número tenha 2 digitos não adiciona espaço
            str_goban += str(linha)
        for coluna in range(ord(obtem_col(obtem_ultima_intersecao(g))) - 64):   # para cada elemento da linha (de colunas diferentes) verifica qual o seu valor para adicionar "X", "O" ou "."
            if eh_pedra_preta(obtem_pedra(g, cria_intersecao(chr(65 + coluna),linha))):
                str_goban += " X"
            if eh_pedra_branca(obtem_pedra(g, cria_intersecao(chr(65 + coluna),linha))):
                str_goban += " O"
            if pedras_iguais(obtem_pedra(g, cria_intersecao(chr(65 + coluna),linha)),cria_pedra_neutra()):
                str_goban += " ."

        if linha < 10:  # verifica se o número tem 1 dígito para adicionar um espaço a mais, depois adiciona o número da linha atual e muda de linha
            str_goban += "  " + str(linha) + "\n"
        else:  # caso tenho o número tenha 2 digitos não adiciona o espaço extra e muda de linha
            str_goban += " " + str(linha) + "\n"

    str_goban += str_letr_coluns   # por fim volta a adicionar o indicador de ind_colunas

    return str_goban


def obtem_territorios(g: dict) -> tuple:
    """
    Obtém os territórios dum dado tabuleiro.

    Args:
        g (dict): O tabuleiro do jogo no qual os territórios serão identificados.

    Returns:
        tuple: O tuplo de tuplos de cadeias de interseções que representam os territórios do jogo.
    """
    lst_pedra_neu = []
    lst_todos = []

    for intersecao in todas_as_intersecoes(g):    # adiciona à lista todas as pedras neutras
        if pedras_iguais(obtem_pedra(g, intersecao),cria_pedra_neutra()):
            lst_pedra_neu += [intersecao]

    while lst_pedra_neu:    # enquanto ainda houverem pedras a serem analizadas
        for intersecao in lst_pedra_neu:
            cadeia_inter = obtem_cadeia(g, intersecao)    
            if cadeia_inter not in lst_todos:    # verifica que a interseção não pertence a nenhum território que já foi analizado !!!!!!!!
                lst_todos += [cadeia_inter]      # adiciona o território num tuplo ao tuplo final
                for intersecao in cadeia_inter:
                    lst_pedra_neu.remove(intersecao)    # retira as interseções da cadeia da lista das pedras neutras a serem analizadas


    for ind_tuplo in range(len(lst_todos)-1):   # para ordenar os territórios

        if obtem_lin(lst_todos[ind_tuplo][0]) > obtem_lin(lst_todos[ind_tuplo+1][0]):   # compara as linhas da primeira interseção dos terrenos
            lst_todos[ind_tuplo], lst_todos[ind_tuplo+1] = lst_todos[ind_tuplo+1], lst_todos[ind_tuplo]

        if obtem_lin(lst_todos[ind_tuplo][0]) == obtem_lin(lst_todos[ind_tuplo+1][0]):  # caso as linhas sejam iguais
            if obtem_col(lst_todos[ind_tuplo][0]) > obtem_col(lst_todos[ind_tuplo+1][0]):   # compara as colunas da primeira interseção dos terrenos
                lst_todos[ind_tuplo], lst_todos[ind_tuplo+1] = lst_todos[ind_tuplo+1], lst_todos[ind_tuplo]


    return tuple(lst_todos)


def obtem_adjacentes_diferentes(g: dict, t: tuple) -> tuple:
    """
    Obtém as interseções adjacentes com tipos diferentes das interseções especificadas.

    Args:
        g (dict): O tabuleiro do jogo.
        t (tuple): um tuplo de tuplos de interseções.

    Returns:
        tuple: Um tuplo de interseções adjacentes com tipos diferentes do território.
    """
    tup_adja = ()

    for intersecao in t:  
        for inter_adj in obtem_intersecoes_adjacentes(intersecao, obtem_ultima_intersecao(g)):    # interseções adjacentes às de t 
            if eh_pedra_jogador(obtem_pedra(g, intersecao)):    # caso a interseção de t for preta ou branca e a adjacente for neutra adiciona-se
                if pedras_iguais(obtem_pedra(g, inter_adj),cria_pedra_neutra()) and inter_adj not in tup_adja:
                    tup_adja += (inter_adj,)

            else:   # caso a interseção de t for neutra e a adjacente for preta ou branca adiciona-se
                if eh_pedra_jogador(obtem_pedra(g, inter_adj)) and inter_adj not in tup_adja:
                    tup_adja += (inter_adj,)

    return ordena_intersecoes(tup_adja)


def jogada(g: dict, i: tuple, p) -> dict:
    """
    Realiza uma jogada, atualizando o tabuleiro.

    Args:
        g (dict): O tabuleiro atual do jogo.
        i (tuple): Um tuplo da interseção onde a jogada será realizada.
        p: A pedra (branca ou preta) a ser colocada na interseção.

    Returns:
        dict: O tabuleiro atualizado após a jogada.
    """
    num_de_terre = len(obtem_territorios(g))

    remove_pedra(g, i)
    coloca_pedra(g, i, p)
    
    tup_adj_i = obtem_intersecoes_adjacentes(i, obtem_ultima_intersecao(g))    # tuplo de interseções adjacentes a i
    tup_adj_i_oposto = ()   # tuplo de interseções adjacentes a i do tipo oposto 
    cad_adj_i_oposto = ()   # cadeias de interseções do tipo oposto a i

    for adjacente_a_i in tup_adj_i:    # obtem as interseções adjacentes do tipo oposto à interseção fornecida 
        if obtem_pedra(g, adjacente_a_i) not in (p, cria_pedra_neutra()):
            tup_adj_i_oposto += (adjacente_a_i,)

    for adjacentes_a_i_tipo_oposto in tup_adj_i_oposto:      # obtem as cadeias de interseções adjacentes a i com tipo oposto 
        cadeia_adj_oposto = obtem_cadeia(g, adjacentes_a_i_tipo_oposto)
        if cadeia_adj_oposto not in cad_adj_i_oposto:   # caso a cadia ainda não tenha sido analizada 
            cad_adj_i_oposto += (cadeia_adj_oposto,)

    for cadeia in cad_adj_i_oposto:

        tup_adj_a_cad = ()
        condicao = True
        
        for inter_cad in cadeia:    # interseções da cadeia
            tup_adj_a_cad += obtem_intersecoes_adjacentes(inter_cad, obtem_ultima_intersecao(g))    # interseções adjacentes à cadeia
        for inter_adj in tup_adj_a_cad:
            if pedras_iguais(obtem_pedra(g, inter_adj),cria_pedra_neutra()):   # tem uma liberdade 
                condicao = False    
        
        if condicao:    # se a cadeia não tiver liberdades 
            remove_cadeia(g, cadeia)

    if num_de_terre != len(obtem_territorios(g)):   # caso o número de terrenos diminuir 
        if obtem_adjacentes_diferentes(g,obtem_cadeia(g,i)) == ():  # e a cadeia da interseção fornecida não tenha liberdades (suicídio)
            remove_cadeia(g, obtem_cadeia(g,i))

    return g


def obtem_pedras_jogadores(g: dict) -> tuple:
    """
    Conta o número de interseções ocupadas por pedras dos jogadores branco e preto.

    Args:
        g (dict): O tabuleiro atual do jogo.

    Returns:
        tuple: Um tuplo de dois inteiros representando o número de interseções ocupadas por pedras brancas e pretas, respetivamente.
    """
    conta_brancas = 0
    conta_pretas = 0

    for intersecao in todas_as_intersecoes(g):    # para todas as interseções do tabuleiro 
        if eh_pedra_branca(obtem_pedra(g,intersecao)):  # se a interseção tiver uma pedra branca  
            conta_brancas += 1
        if eh_pedra_preta(obtem_pedra(g,intersecao)):  # se a interseção tiver uma pedra preta 
            conta_pretas += 1            

    return (conta_brancas,conta_pretas)

#------------------------------#

def calcula_pontos(g: dict) -> tuple:
    """
    Calcula os pontos dos jogadores branco e preto.

    Args:
        g (dict): O tabuleiro atual do jogo.

    Returns:
        tuple: Um tuplo de dois inteiros representando os pontos do jogador branco e preto, respectivamente.
    """
    pontos_branco = obtem_pedras_jogadores(g)[0]
    pontos_pretas = obtem_pedras_jogadores(g)[1] 
    tup_territorios = obtem_territorios(g)

   
    for territorio in tup_territorios:

        brancas = 0
        pretas = 0
        fronterira = obtem_adjacentes_diferentes(g,territorio)

        for inter in fronterira:
            if eh_pedra_branca(obtem_pedra(g, inter)):  # cajo a interseção seja uma pedra branca
                brancas += 1
            if eh_pedra_preta(obtem_pedra(g, inter)):   # cajo a interseção seja uma pedra branca
                pretas += 1

        if brancas == 0 and pretas != 0:    # caso o território seja das peças brancas
            pontos_pretas += len(territorio)
        if brancas != 0 and pretas == 0:    # caso o território seja das peças pretas
            pontos_branco += len(territorio)
    
    return (pontos_branco, pontos_pretas)

    
def eh_jogada_legal(g: dict, i: tuple, p, l: dict) -> bool:
    """
    Verifica se uma jogada é legal.

    Args:
        g (dict): O tabuleiro atual do jogo.
        i (tuple): A interseção na qual a jogada será feita.
        p: A pedra do jogador que está a jogar.
        l (dict): O estado do tabuleiro após a última jogada.

    Returns:
        bool: True se a jogada for legal, False caso contrário.
    """
    copia_g = cria_copia_goban(g)

    if eh_pedra_branca(p):  # verifica que jogador está a jogar
        indice = 0
    else:
        indice = 1

    if obtem_pedra(g, i) != cria_pedra_neutra():    # caso a interseção ja tenha uma pedra de jogador 
        return False
    pedras_antes = obtem_pedras_jogadores(copia_g)[indice]  # quantidade de pedras do jogador antes de fazer a jogada 
    pontos_antes = calcula_pontos(copia_g)[indice]
    pontos_depois = calcula_pontos(jogada(copia_g,i,p))[indice]

    if gobans_iguais(copia_g,l):   # caso do KO
        return False

    if pontos_depois - pontos_antes < 0:    # verifica alguns dos casos de "suicídio"
        return False
    
    if pontos_depois - pontos_antes == 0 and pedras_antes == obtem_pedras_jogadores(copia_g)[indice]:   # um caso de "suicídio" 
        return False
    
    return True


def turno_jogador(g: dict, p, l: dict) -> bool:
    """
    Realiza o turno de um jogador.

    Args:
        g (dict): O tabuleiro atual do jogo.
        p: A pedra do jogador atual.
        l (dict): O estado do tabuleiro após a última jogada.

    Returns:
        bool: True se o jogador fez uma jogada válida, False se optou por passar.
    """
    while True: 
        resposta = input(f"Escreva uma intersecao ou 'P' para passar [{pedra_para_str(p)}]:")

        if resposta == "P":
            return False
        
        try:
            if eh_intersecao_valida(g,str_para_intersecao(resposta)):   # verifica se a interseção é válida
                if eh_jogada_legal(g,str_para_intersecao(resposta),p,l):    # caso a jogada seja válida faz a jogada
                    jogada(g,str_para_intersecao(resposta),p)
                    return True
        except ValueError:     
            pass


def go(n: int, tb: tuple, tp: tuple) -> bool:
    """
    Inicia e executa um jogo de Go com tabuleiro de tamanho 'n' e posições iniciais de peças.
    
    Args:
        n (int): Tamanho do tabuleiro (9, 13, ou 19).
        tb (tuple): Tuplo com posições iniciais das pedras brancas.
        tp (tuple): Tuplo com posições iniciais das pedras pretas.
        
    Returns:
        bool: True se as pedras brancas ganharem, False se as pretas ganharem.
        
    Raises:
        ValueError: Se os argumentos forem inválidos.
    """    
    ib = ()
    ip = ()
    
    if type(tb) != tuple or type(tp) != tuple:    # verifica que o tb e tp são argumentos do tipo certo
        raise ValueError('go: argumentos invalidos')


    for elementos in tb:    # para cada uma das interesções 
        try:    # tenta transformar na representação interna
            ib += ((str_para_intersecao(elementos)),)
        except ValueError:
            raise ValueError('go: argumentos invalidos')
        except TypeError:
            raise ValueError('go: argumentos invalidos')


    for elementos in tp:    # para cada uma das interesções 
        try:    # tenta transformar na representação interna
            ip += ((str_para_intersecao(elementos)),)
        except ValueError:
            raise ValueError('go: argumentos invalidos')
        except TypeError:
            raise ValueError('go: argumentos invalidos')
            
    try:
        if not eh_goban(cria_goban(n,ib,ip)): # verifica que n é válido
            raise ValueError('go: argumentos invalidos')
        else:
            g = cria_goban(n,ib,ip)
    except ValueError:
        raise ValueError('go: argumentos invalidos')           
    
    condi_p = True  
    condi_b = True
    conta_jogadas = 0
    copia_g_b, copia_g_p = cria_copia_goban(g), cria_copia_goban(g)

    while condi_b or condi_p:

        print("Branco (O) tem",calcula_pontos(g)[0],"pontos")
        print("Preto (X) tem",calcula_pontos(g)[1],"pontos")
        print(goban_para_str(g))
        
        if conta_jogadas % 2 == 0:  # pretas jogam primeiro e em jogadas impares
            condi_p = turno_jogador(g, cria_pedra_preta(),copia_g_p)
            copia_g_p = cria_copia_goban(g)    # uma copia da jogada pois na proxima rodada (deste jogador) esta vai ser o tabuleiro que não pode ser repetido
        else:
            condi_b = turno_jogador(g, cria_pedra_branca(),copia_g_b)
            copia_g_b = cria_copia_goban(g)    # uma copia da jogada pois na proxima rodada (deste jogador) esta vai ser o tabuleiro que não pode ser repetido

        conta_jogadas += 1

    print("Branco (O) tem",calcula_pontos(g)[0],"pontos")
    print("Preto (X) tem",calcula_pontos(g)[1],"pontos")
    print(goban_para_str(g))

    if calcula_pontos(g)[0] >= calcula_pontos(g)[1]:    # caso o branco tenha mais pontos
        return True    # ganha o branco
    elif calcula_pontos(g)[0] < calcula_pontos(g)[1]:   # caso o preto tenha mais pontos
        return False    # ganha o preto

    