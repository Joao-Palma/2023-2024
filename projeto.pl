
% IST1109242 Joao Palma
:- use_module(library(clpfd)).
:- set_prolog_flag(answer_write_options,[max_depth(0)]).
:- ["puzzlesAcampar.pl"].
% Segue-se o codigo

%---------------------------------------------------------

vizinhanca((L,C), V):- 
/*
Devolve Uma lista com a vizinhanca (pontos acima, abaixo, a esquerda e direita) 
do ponto com as coordenadas (L,C).
*/ 
    Linha_cim is L - 1,
    Linha_bai is L + 1,
    Colun_esq is C - 1,
    Colun_dir is C + 1,
    V = [(Linha_cim,C), (L,Colun_esq), (L,Colun_dir), (Linha_bai,C)].

%---------------------------------------------------------

vizinhancaAlargada((L,C), V):-
/*
Devolve Uma lista com a vizinhanca (pontos acima, abaixo, a esquerda, a direita e as 
diagonais) do ponto com as coordenadas (L,C).
*/ 
    Linha_cim is L - 1,
    Linha_bai is L + 1,
    Colun_esq is C - 1,
    Colun_dir is C + 1,
    V = [(Linha_cim,Colun_esq), (Linha_cim,C), (Linha_cim,Colun_dir), (L,Colun_esq), 
        (L,Colun_dir), (Linha_bai,Colun_esq), (Linha_bai,C), (Linha_bai,Colun_dir)].

%---------------------------------------------------------

avaliaLinha(Lin, IndL, LCord, O):-
/*
Recebe uma linha dum tabuleiro e devolve uma lista com todas as posicoes do objeto (O).
*/ 
    length(Lin, Comp),
    Sub is Comp + 1 ,
    avaliaLinha1(Lin, Comp, Sub, IndL, LCord, O, []).

avaliaLinha1([],_,_,_,LAux,_,LAux).

avaliaLinha1([_|T], Comp, Sub, IndL, LCord, O, LAux):-
    O == -1, !, % caso especial para o predicado todasCelulas(T, Tc)
    Col is abs(Comp - Sub),    % calculo para obter o indice da coluna
    append(LAux, [(IndL,Col)], LAux1),
    Comp1 is Comp - 1,
    avaliaLinha1(T, Comp1, Sub, IndL, LCord, O, LAux1).

avaliaLinha1([H|T], Comp, Sub, IndL, LCord, O, LAux):-
    var(O), 
    var(H), !,  % o elemento e o objeto (O) sao os dois variaveis livres
    Col is abs(Comp - Sub),
    append(LAux,[(IndL,Col)], LAux1),
    Comp1 is Comp - 1,
    avaliaLinha1(T, Comp1, Sub, IndL, LCord, O, LAux1).

avaliaLinha1([_|T], Comp, Sub, IndL, LCord, O, LAux):-
    var(O), !,  % o elemento e o objeto (O) nao sao iguais
    Comp1 is Comp - 1,
    avaliaLinha1(T, Comp1, Sub, IndL, LCord, O, LAux).

avaliaLinha1([H|T], Comp, Sub, IndL, LCord, O, LAux):-
    atom(O),
    var(H), !,  % o elemento e o objeto (O) nao sao iguais
    Comp1 is Comp - 1,
    avaliaLinha1(T, Comp1, Sub, IndL, LCord, O, LAux).

avaliaLinha1([H|T], Comp, Sub, IndL, LCord, O, LAux):-
    H == O,!,   % o elemento e o objeto (O) sao iguais 
    Col is abs(Comp - Sub),    
    append(LAux, [(IndL,Col)], LAux1),
    Comp1 is Comp - 1,
    avaliaLinha1(T, Comp1, Sub, IndL, LCord, O, LAux1).

avaliaLinha1([_|T], Comp, Sub, IndL, LCord, O, LAux):-
    Comp1 is Comp - 1,  % o elemento e o objeto (O) nao sao iguais e sao ambos nao variaveis
    avaliaLinha1(T, Comp1, Sub, IndL, LCord, O, LAux).

%----------

todasCelulas(T, Tc):-
/*
Devolve Uma lista com as coordenadas de todas as celulas do tabuleiro.
*/ 
    todasCelulas1(T, Tc, -1, [], 1).    

todasCelulas1([], TcAux,_,TcAux,_).

todasCelulas1([H|T], Tc, O, TcAux, IndL):-
    avaliaLinha(H, IndL, LCord, O),
    IndL1 is IndL + 1,
    append(TcAux, LCord, TcAux1),
    todasCelulas1(T, Tc, O, TcAux1, IndL1).

%---------------------------------------------------------

todasCelulas(T, Tc, O):-
/*
Devolve Uma lista com as coordenadas de todas as celulas do tabuleiro com o objeto O.
*/ 
    todasCelulas2(T, Tc, O, [], 1).

todasCelulas2([],TcAux,_,TcAux,_).

todasCelulas2([H|T], Tc, O, TcAux, IndL):-
    avaliaLinha(H, IndL, LCord, O),
    IndL1 is IndL + 1,
    append(TcAux, LCord, TcAux1),
    todasCelulas2(T, Tc, O, TcAux1, IndL1).

%---------------------------------------------------------

contaObjlin(Lin, O, Res):-
/*
Devolve o numero de objetos numa linha.
*/ 
    contaObjlin(Lin, O, Res, 0).

contaObjlin([],_, ResAux, ResAux).

contaObjlin([H|T], O, Res, ResAux):-
    var(H),
    var(O), !,  
    ResAux1 is ResAux + 1,
    contaObjlin(T, O, Res, ResAux1).

contaObjlin([H|T], O, Res, ResAux):-
    var(H), !,
    contaObjlin(T, O, Res, ResAux).

contaObjlin([H|T], O, Res, ResAux):-
    atom(H),
    var(O), !,
    contaObjlin(T, O, Res, ResAux).

contaObjlin([H|T], O, Res, ResAux):-
    atom(H),
    atom(O),
    H == O, !,
    ResAux1 is ResAux + 1,
    contaObjlin(T, O, Res, ResAux1).

contaObjlin([_|T], O, Res, ResAux):-
    % caso o objeto H seja diferente do objeto (O) e ambos nao sejam variaveis livres
    contaObjlin(T, O, Res, ResAux).

%----------

avaliaMatriz(Tab, List, O):-
/*
Devolve Uma lista com o numero de objetos (O) por linha da linha 1 a ultima.
*/ 
    avaliaMatriz1(Tab, List, O, []).

avaliaMatriz1([], ListAux,_, ListAux).

avaliaMatriz1([H|T], List, O, ListAux):-
    contaObjlin(H, O, NumObjNaLin),
    append(ListAux, [NumObjNaLin], ListAux1), 
    avaliaMatriz1(T, List, O, ListAux1).

%----------

calculaObjectosTabuleiro(T, ContLin, ContCol, O):-
/*
Devolve duas listas com o numero de objetos (O) por linhas e por colunas.
*/ 
    calculaObjectosTabuleiro1(T, ContLin, ContCol, O, [], []).
    
calculaObjectosTabuleiro1([], AuxL, AuxC,_, AuxL, AuxC).

calculaObjectosTabuleiro1(T, ContLin, ContCol, O, _, _):-
    avaliaMatriz(T, ListaNumObjLin, O),    % verifica o numero de objetos (O) nas linhas
    transpose(T, Transpose),
    avaliaMatriz(Transpose, ListaNumObjCol, O),     % verifica o numero de objetos (O) nas colunas
    calculaObjectosTabuleiro1([], ContLin, ContCol, O, ListaNumObjLin, ListaNumObjCol).

%---------------------------------------------------------

celulaVazia(Tab, (L, C)):-
/*
Devolve true caso o objeto nas coordenadas (L, C) tenham uma relva ou uma variavel livre.
*/ 
    % verificacao se a coordenada pertence ao tab
    length(Tab, Comp),
    (L > Comp;
     L =< 0;
     C > Comp;
     C =< 0), !.    

celulaVazia(Tab, (L, C)):-
    nth1(L, Tab, Lin),
    nth1(C, Lin, Ele),
    (var(Ele);
    Ele == r).    % verifica se a celula esta vazia (ou com relva)

%---------------------------------------------------------

subNaLis(List, Subs, Posi, Res):-
/*
Devolve uma lista com a posicao (Posi) da lista (List) substituida pela Subs.
*/ 
    subNaLis1(List, Subs, Posi, Res, [], []).

subNaLis1(_,_, 0, ResAux,_, ResAux).

subNaLis1([H|T], Subs, Posi, Res, ListAnteriorAPosi, ResAux):-
    % quando o elemento H for o elemento da posicao (Posi) e o elemento 
    % for uma var ou uma lista faz-se a substituicao
    Posi == 1,
    (var(H);
    is_list(H)), !,
    append(ResAux, T, ResAux1),
    append([Subs], ResAux1, ResAux2),
    append(ListAnteriorAPosi, ResAux2, ResAux3),
    Posi1 is Posi - 1,
    subNaLis1([T], Subs, Posi1, Res, ListAnteriorAPosi, ResAux3).

subNaLis1([H|T], _, Posi, Res, ListAnteriorAPosi, _):-
    % quando o elemento H for o elemento a substituir e o elemento
    % nao for uma var nao se faz substituicao
    Posi == 1,
    (atom(H);
    is_list(H)), !,
    append(ListAnteriorAPosi, [H|T], ResAux3),
    Posi1 is Posi - 1,
    subNaLis1([T], _, Posi1, Res, ListAnteriorAPosi, ResAux3).

subNaLis1([H|T], Subs, Posi, Res, ListAnteriorAPosi, _):-
    % emquanto H nao e o elemento a substituir
    Posi1 is Posi - 1,
    append(ListAnteriorAPosi, [H], ListAnteriorAPosi1), % adicionar H a lista dos elementos Anteriores
    subNaLis1(T, Subs, Posi1, Res, ListAnteriorAPosi1, _).

%----------

insereObjectoCelula(Tab, TouR, (L, C)):-
/*
Insere uma tenda ou relva na posicao de coordenadas (L, C).
*/ 
    nth1(L, Tab, Lin),
    subNaLis(Lin, TouR, C, LinComSub),
    subNaLis(Tab, LinComSub, L, TabComSub),
    Tab = TabComSub.

%---------------------------------------------------------

subsnaLin(Lin, TouR, C1, C2, Res):-
/*
Devolve uma lista com os elementos da posicao C1 a C2 da lista (Lin) substituidos
por relvas ou tendas.
*/ 
    Cont is C2 - C1 + 1,    % quantos elemetos substituir a partir do elemento na posicao C1
    IndSub is C1,   % coordenada do atual elemento a substituir 
    subsnaLin1(TouR, Res, Lin, Cont, IndSub).

subsnaLin1(_, Aux, Aux, 0,_).

subsnaLin1(TouR, Res, Aux, Cont, IndSub):-
    subNaLis(Aux, TouR, IndSub, LinComSub),
    Cont1 is Cont - 1,
    IndSub1 is IndSub + 1,
    subsnaLin1(TouR, Res, LinComSub, Cont1, IndSub1).

%----------

insereObjectoEntrePosicoes(Tab, TouR, (L, C1), (L, C2)):-
/*
Atualiza o tabuleiro com relvas ou tendas nas posicoes de C1 a C2 da linha de indice L.
*/ 
    nth1(L, Tab, Lin),
    subsnaLin(Lin, TouR, C1, C2, LinComSubs),
    subNaLis(Tab, LinComSubs, L, TabComSub),
    Tab = TabComSub.
    
%---------------------------------------------------------

subListCompComRelva(Tab, LisComVal, Res):-
/*
Recebe um tabuleiro e uma lista com o numero de tendas esperadas nas suas linhas,
caso o numero de tendas da linha correspoda ao numero indicado 
na lista o resto das variaveis livres nessa linha vao ser substituidas por relvas.
*/ 
    length(Tab, Comp),  % quantidade de elementos na linha
    subListCompComRelva1(Tab, LisComVal, Res, [], Comp).

subListCompComRelva1([],_, TabAux, TabAux,_).
    
subListCompComRelva1([H1|T1], [H|T], Res, TabAux, Comp):-
    % caso o numero de tendas na linha nao seja igual ao (H) numero total 
    contaObjlin(H1, t, Num),
    H =\= Num, !,
    append(TabAux, [H1], TabAux1),
    subListCompComRelva1(T1, T, Res, TabAux1, Comp).

subListCompComRelva1([H1|T1], [H|T], Res, TabAux, Comp):-
    % caso o numero de tendas na linha seja igual ao (H) numero total 
    contaObjlin(H1, t, Num),
    H == Num, !,
    subsnaLin(H1, r, 1, Comp, LinAlt), % substitui os espacos livres da linha inteira com relvas
    append(TabAux, [LinAlt], TabAux1),
    subListCompComRelva1(T1, T, Res, TabAux1, Comp).

%----------

relva((Tab, LisLin, LisCol)):-
/*
Recebe um tabuleiro e duas lista com o numero de tendas esperadas nas suas linhas/colunas,
caso o numero de tendas da linha/coluna correspoda ao numero indicado 
na lista o resto das variaveis livres nessa linha/coluna vao ser substituidas por relvas.
*/ 
    subListCompComRelva(Tab, LisLin, TabComLin),
    transpose(TabComLin, TabTran),
    subListCompComRelva(TabTran, LisCol, TabComSubsTran),
    transpose(TabComSubsTran, TabComSubs),    
    Tab = TabComSubs.   

%---------------------------------------------------------

vizinhancasDeTodos(List, Res):-
/*
Recece uma lista de cordenadas (list) e devolve uma lista com todas as vizinhancas 
de todos os pontos da lista.
*/ 
    vizinhancasDeTodos1(List, Res, []).

vizinhancasDeTodos1([], Aux, Aux).

vizinhancasDeTodos1([H|T], Res, Aux):-
    vizinhanca(H, Viz),
    append(Aux, Viz, Aux1),
    vizinhancasDeTodos1(T, Res, Aux1).

%----------

retiraCordComuns(ListMaisCord, List2, Res):-
/*
recebe duas listas devolve uma lista com os elementos da ListMaisCord que nao 
aparecem na List2.
*/ 
    retiraCordComuns1(ListMaisCord, List2, Res, []).

retiraCordComuns1([],_, Aux, Aux).

retiraCordComuns1([H|T], List2, Res, Aux):-
    \+ member(H, List2), !, 
    append(Aux, [H], Aux1),
    retiraCordComuns1(T, List2, Res, Aux1).

retiraCordComuns1([_|T], List2, Res, Aux):-
    retiraCordComuns1(T, List2, Res, Aux).

%----------

insereRelvas(_, []).

insereRelvas(Tab, [(L, C)|T]):-
/*
recebe uma lista de coordenadas (L, C) e substitui esses pontos com relvas.
*/ 
    insereObjectoCelula(Tab, r, (L, C)), !,
    insereRelvas(Tab, T).

insereRelvas(Tab, r, [(_, _)|T]):-
    insereRelvas(Tab, T).

%----------

inacessiveis(Tab):-
/*
Recebe um tabuleiro e insere relva em todos os pontos que nao pertencem a vizinhanca 
das arvores do tabuleiro.
*/ 
    todasCelulas(Tab, CordObj, a),
    vizinhancasDeTodos(CordObj, CordViz),
    todasCelulas(Tab, CordTab),
    retiraCordComuns(CordTab, CordViz, CordInace),
    insereRelvas(Tab, CordInace).

%---------------------------------------------------------

veriTab(Tab, LisComVal, Res):-
/*
Recebe um tabuleiro e uma lista com a quantidades de tendas que cada linha tem que ter,
caso o valor da lista coincida com a quantidade de tendas e variaveis livres da linha 
os pontos com variaveis livres vao ser substituidos por tendas.
*/ 
    length(Tab,Comp),
    veriTab1(Tab, LisComVal, Res, [], Comp).

veriTab1([],_, TabAux, TabAux,_).
    
veriTab1([H1|T1], [H|T], Res, TabAux, Comp):-
    contaObjlin(H1,_, Num1),
    contaObjlin(H1,t, Num2),
    H =\= Num1 + Num2, !,   % o numero de tendas e espacos livres nao coincide
    append(TabAux, [H1], TabAux1),
    veriTab1(T1, T, Res, TabAux1, Comp).

veriTab1([H1|T1], [H|T], Res, TabAux, Comp):-
    contaObjlin(H1,_, Num1),
    contaObjlin(H1,t, Num2),
    H =:= Num1 + Num2, !,   % o numero de tendas e espacos livres coincide
    subsnaLin(H1, t, 1, Comp, LinAlt),
    append(TabAux, [LinAlt], TabAux1),
    veriTab1(T1, T, Res, TabAux1, Comp).

%----------

aproveita((Tab, LisLin, LisCol)):-
/*
Recebe o tabuleiro e insere tendas em todas as linhas e colunas as quais faltavam 
colocar X tendas e que tinham exactamente X posicoes livres.
*/ 
    veriTab(Tab, LisLin, TabSubLin),
    transpose(Tab, TabTran),
    veriTab(TabTran, LisCol, TabSubColTran),
    transpose(TabSubColTran, TabSubCol),
    TabSubLin = TabSubCol,
    Tab = TabSubLin.

%---------------------------------------------------------

verifEinsereRelva(Tab, [(L,C)|T]):-
/*
Verifica se as coordenadas pertencem ao tabuleiro e caso estejam vazias uma relva 
e inserida. 
*/ 
    length(Tab, Comp),
    verifEinsereRelva(Tab, [(L,C)|T], Comp).

verifEinsereRelva(_, [],_).

verifEinsereRelva(Tab, [(L,C)|T], Comp):-   
% verifica que as coordenadas estao dentro do tabuleiro
    (L > Comp;
     L =< 0;
     C > Comp;
     C =< 0), !,
    verifEinsereRelva(Tab, T, Comp). 

verifEinsereRelva(Tab, [(L,C)|T], Comp):-
    insereObjectoCelula(Tab, r, (L, C)),
    verifEinsereRelva(Tab, T, Comp).

%----------

insereRelvasNaViz(_, []).

insereRelvasNaViz(Tab, [(L,C)|T]):-
/*
recebe uma coordenada e devolve a vizinhanca da mesma ao predicado verifEinsereRelva.
*/ 
    vizinhancaAlargada((L,C), Viz),
    verifEinsereRelva(Tab, Viz),
    insereRelvasNaViz(Tab, T).

%----------

limpaVizinhancas((Tab,_,_)):-
/*
Insere relvas a volta de todas as tendas do tabuleiro.
*/ 
    todasCelulas(Tab, CordObj, t),
    insereRelvasNaViz(Tab, CordObj).

%---------------------------------------------------------

    
validaUniHip(Viz, Tab):-
/*
verifica que existe apenas um espaco livre ou uma tenda na vizinhanca 
para inserir uma tenda no espaco vazio.
*/ 
    validaUniHip1(Viz, Tab, []).

validaUniHip1([], Tab, [(L, C)|T]):-
    length([(L, C)|T], N),
    N == 1, !,
    insereObjectoCelula(Tab, t, (L, C)).

validaUniHip1([],_,_).

validaUniHip1([(L, C)|T], Tab, Aux):-
    nth1(L, Tab, Lin),
    nth1(C, Lin, Ele),
    (var(Ele);
     Ele == t), !,
    append(Aux, [(L, C)], Aux1),
    validaUniHip1(T, Tab, Aux1).

validaUniHip1([(_,_)|T], Tab, Aux):-
    validaUniHip1(T, Tab, Aux).

%----------

veriVizArvs([],_).

veriVizArvs([(L, C)|T], Tab):-
/*
recebe uma lista de coordenadas e devolve as vizinhancas das mesmas ao predicado 
validaUniHip.
*/ 
    vizinhanca((L, C), Viz),
    validaUniHip(Viz, Tab),
    veriVizArvs(T, Tab).

%----------

unicaHipotese((Tab,_,_)):-
/*
verifica se existem arvores com apenas uma posicao na sua vizinhanca que tenha uma variavel livre,
nesse caso insere uma tenda.
*/ 
    todasCelulas(Tab, CordObj, a),
    veriVizArvs(CordObj, Tab).

%--------------------------------------------------------- 

valida(LArv, LTen):-
/*
verifica que existe o mesmo numero de tendas e arvores.
*/ 
    length(LArv, N),
    length(LTen, N1),
    N == N1, 
    vizinhancasDeTodos(LArv, VizArvores),
    retiraCordComuns(LTen, VizArvores, Res),
    length(Res, NTendasSemArvore), !,
    NTendasSemArvore == 0.

%---------------------------------------------------------

verifica(Tab, NAntes, NDepois):-
/*
Verifica se o numero de espacos vazios e o mesmo antes e depois de serem aplicados predicados ao tabuleiro
caso seja e aleatoriamente posta uma tenda no tabuleiro. 
*/     
    NAntes =:= NDepois, !,
    todasCelulas(Tab, TodasVar,_),
    member((L,C), TodasVar),
    insereObjectoCelula(Tab, t, (L,C)).


verifica(_, NAntes, NDepois):-
    NAntes =\= NDepois, !.

%----------

resolve((Tab, LisLin, LisCol)):-
/*
Resolve o puzzle. 
*/ 
    inacessiveis(Tab),
    relva((Tab, LisLin, LisCol)),
    aproveita((Tab, LisLin, LisCol)),
    limpaVizinhancas((Tab, LisLin, LisCol)),
    todasCelulas(Tab, LArv, a),
    resolve((Tab, LisLin, LisCol),LArv).


resolve((Tab,_,_),LArv):-   
% verifica se o puzzle foi resolvido corretamente
    todasCelulas(Tab, LTen, t),
    valida(LArv, LTen).

resolve((Tab, LisLin, LisCol),LArv):-   
% aplica os predicados anteriores e verifica se o tabuleiro esta ou nao a sofrer alguma mudanca
    todasCelulas(Tab, TodasVarAntes,_),
    length(TodasVarAntes, NAntes),
    unicaHipotese((Tab, LisLin, LisCol)),
    aproveita((Tab, LisLin, LisCol)),
    relva((Tab, LisLin, LisCol)), 
    limpaVizinhancas((Tab, LisLin, LisCol)),
    todasCelulas(Tab, TodasVarDepois,_),
    length(TodasVarDepois, NDepois),
    verifica(Tab, NAntes, NDepois),
    resolve((Tab, LisLin, LisCol),LArv).

%---------------------------------------------------------



    