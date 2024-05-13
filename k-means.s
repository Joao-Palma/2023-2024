
# IAC 2023/2024 k-means

# Grupo:
# Campus: TagusPark

# Autores:
# Ist1109242, João Palma

# Tecnico/ULisboa

# Variaveis em memoria
.data

#Input A - linha inclinada
n_points:    .word 9
points:      .word 0,0, 1,1, 2,2, 3,3, 4,4, 5,5, 6,6, 7,7 8,8

#Input B - Cruz
#n_points:    .word 5
#points:     .word 4,2, 5,1, 5,2, 5,3 6,2

#Input C
#n_points:    .word 23
#points: .word 0,0, 0,1, 0,2, 1,0, 1,1, 1,2, 1,3, 2,0, 2,1, 5,3, 6,2, 6,3, 6,4, 7,2, 7,3, 6,8, 6,9, 7,8, 8,7, 8,8, 8,9, 9,7, 9,8

#Input D
#n_points:    .word 30
#points:      .word 16, 1, 17, 2, 18, 6, 20, 3, 21, 1, 17, 4, 21, 7, 16, 4, 21, 6, 19, 6, 4, 24, 6, 24, 8, 23, 6, 26, 6, 26, 6, 23, 8, 25, 7, 26, 7, 20, 4, 21, 4, 10, 2, 10, 3, 11, 2, 12, 4, 13, 4, 9, 4, 9, 3, 8, 0, 10, 4, 10



# Valores de centroids e k a usar na 1a parte do projeto:
centroids:   .word 0,0
k:           .word 1

# Valores de centroids, k e L a usar na 2a parte do prejeto:
#centroids:   .word 0,0, 10,0, 0,10
#k:           .word 3
#L:           .word 10

# Abaixo devem ser declarados o vetor clusters (2a parte) e outras estruturas de dados
# que o grupo considere necessarias para a solucao:
#clusters:    




#Definicoes de cores a usar no projeto 

colors:      .word 0xff0000, 0x00ff00, 0x0000ff  # Cores dos pontos do cluster 0, 1, 2, etc.

.equ         black      0
.equ         white      0xffffff



# Codigo
 
.text
    # Chama funcao principal da 1a parte do projeto  

    jal mainSingleCluster

    # Descomentar na 2a parte do projeto:
    #jal mainKMeans
    
    #Termina o programa (chamando chamada sistema)
    li a7, 10
    ecall


### printPoint
# Pinta o ponto (x,y) na LED matrix com a cor passada por argumento
# Nota: a implementacao desta funcao ja' e' fornecida pelos docentes
# E' uma funcao auxiliar que deve ser chamada pelas funcoes seguintes que pintam a LED matrix.
# Argumentos:
# a0: x
# a1: y
# a2: cor

printPoint:
    li a3, LED_MATRIX_0_HEIGHT
    sub a1, a3, a1
    addi a1, a1, -1
    li a3, LED_MATRIX_0_WIDTH
    mul a3, a3, a1
    add a3, a3, a0
    slli a3, a3, 2
    li a0, LED_MATRIX_0_BASE
    add a3, a3, a0   # addr
    sw a2, 0(a3)
    jr ra
    

### cleanScreen
# Limpa todos os pontos do ecrã
# Argumentos: nenhum
# Retorno: nenhum

cleanScreen:
    
    li t0, 0
    li t1, 0
    li a2, black
    li t3, 32
    # save return adress to main function
    addi sp, sp, -4    
    sw ra , 0(sp)
    
    ForX:
        jal ra, ForY
        li t1, 0
        addi t0, t0, 1
        blt t0, t3, ForX 
        #end
        lw ra , 0(sp)
        addi sp, sp, 4
        jr ra
        
    ForY:
        add a0, t0, x0
        add a1, t1, x0
        addi sp, sp, -4
        sw ra , 0(sp)
        jal ra printPoint
        lw ra , 0(sp)
        addi sp, sp, 4
        addi t1, t1, 1 
        blt t1, t3, ForY
        jr ra

    
### printClusters
# Pinta os agrupamentos na LED matrix com a cor correspondente.
# Argumentos: nenhum
# Retorno: nenhum

printClusters:
    li t0, 0
    lw t2, n_points
    # save return adress to main function
    addi sp, sp, -4    
    sw ra , 0(sp)
    
    ForprintClusters:
        la t1, points
        slli t3, t0, 3
        add t3, t1, t3
        lw a0, 0(t3)
        lw a1, 4(t3)
        li a2, white
        jal printPoint
        addi t0, t0, 1
        blt t0, t2, ForprintClusters
    
    lw ra , 0(sp)
    addi sp, sp, 4
    jr ra
    


### printCentroids
# Pinta os centroides na LED matrix
# Nota: deve ser usada a cor preta (black) para todos os centroides
# Argumentos: nenhum
# Retorno: nenhum

printCentroids:
    li t0, 0
    lw t2, k
    # save return adress to main function
    addi sp, sp, -4    
    sw ra , 0(sp)
    
    ForprintCentroids:
        la t1, centroids
        slli t3, t0, 3
        add t3, t1, t3
        lw a0, 0(t3)
        lw a1, 4(t3)
        la t1, colors
        slli t3, t0, 2
        add t3, t1, t3
        lw a2, 0(t3)
        jal printPoint
        addi t0, t0, 1
        blt t0, t2, ForprintCentroids
    
    lw ra , 0(sp)
    addi sp, sp, 4
    jr ra
    

### calculateCentroids
# Calcula os k centroides, a partir da distribuicao atual de pontos associados a cada agrupamento (cluster)
# Argumentos: nenhum
# Retorno: nenhum

calculateCentroids:
    li t0, 0
    lw t2, n_points
    li t4, 0 # sum of x coord
    li t5, 0 # sum of y coord
    # save return adress to main function
    addi sp, sp, -4    
    sw ra , 0(sp)
    
    ForcalculateCentroids:
        la t1, points
        slli t3, t0, 3
        add t3, t1, t3
        lw t6, 0(t3)
        add t4, t4, t6
        lw t6, 4(t3)
        add t5, t5, t6
        addi t0, t0, 1
        blt t0, t2, ForcalculateCentroids
    div t4, t4, t2 
    div t5, t5, t2
    la t1, centroids
    sw t4, 0(t1)
    sw t5, 4(t1)
    lw ra , 0(sp)
    addi sp, sp, 4
    jr ra


### mainSingleCluster
# Funcao principal da 1a parte do projeto.
# Argumentos: nenhum
# Retorno: nenhum

mainSingleCluster:
    
    addi sp, sp, -4
    sw ra, 0(sp)

    #1. Coloca k=1 (caso nao esteja a 1)
    # POR IMPLEMENTAR (1a parte)

    jal ra, cleanScreen

    jal ra, printClusters

    jal ra, calculateCentroids
    # POR IMPLEMENTAR (1a parte)

    jal ra printCentroids
    # POR IMPLEMENTAR (1a parte)

    lw ra, 0(sp)
    addi sp, sp, 4
    jr ra



### manhattanDistance
# Calcula a distancia de Manhattan entre (x0,y0) e (x1,y1)
# Argumentos:
# a0, a1: x0, y0
# a2, a3: x1, y1
# Retorno:
# a0: distance

manhattanDistance:
    # POR IMPLEMENTAR (2a parte)
    jr ra


### nearestCluster
# Determina o centroide mais perto de um dado ponto (x,y).
# Argumentos:
# a0, a1: (x, y) point
# Retorno:
# a0: cluster index

nearestCluster:
    # POR IMPLEMENTAR (2a parte)
    jr ra


### mainKMeans
# Executa o algoritmo *k-means*.
# Argumentos: nenhum
# Retorno: nenhum

mainKMeans:  
    # POR IMPLEMENTAR (2a parte)
    jr ra