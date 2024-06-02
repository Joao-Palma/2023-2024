
# IAC 2023/2024 k-means

# Campus: TagusPark

# Autor:
# João Palma

# Tecnico/ULisboa

.data

#Input A - linha inclinada
#n_points:    .word 9
#points:      .word 0,0, 1,1, 2,2, 3,3, 4,4, 5,5, 6,6, 7,7 8,8

#Input B - Cruz
#n_points:    .word 5
#points:     .word 4,2, 5,1, 5,2, 5,3 6,2

#Input C
#n_points:    .word 23
#points: .word 0,0, 0,1, 0,2, 1,0, 1,1, 1,2, 1,3, 2,0, 2,1, 5,3, 6,2, 6,3, 6,4, 7,2, 7,3, 6,8, 6,9, 7,8, 8,7, 8,8, 8,9, 9,7, 9,8

#Input D
n_points:    .word 30
points:      .word 16, 1, 17, 2, 18, 6, 20, 3, 21, 1, 17, 4, 21, 7, 16, 4, 21, 6, 19, 6, 4, 24, 6, 24, 8, 23, 6, 26, 6, 26, 6, 23, 8, 25, 7, 26, 7, 20, 4, 21, 4, 10, 2, 10, 3, 11, 2, 12, 4, 13, 4, 9, 4, 9, 3, 8, 0, 10, 4, 10 


#centroids:   .word 0, 0, 4, 4, 3, 2
#k:           .word 3

centroids:   .word 8,16, 20,4, 31,0
k:           .word 3
#L:           .word 10

clusters:    .zero 120    # number of points * 4

# empty at the start will be filed with numbers form 0 to k-1 
# to identify the cluster a point in the index i (0 to n_points-1) belongs to 

#Definicoes de cores a usar no projeto 
colors:      .word 0xff0000, 0x00ff00, 0x0000ff  # Cores dos pontos do cluster 0, 1, 2, etc.

.equ         black      0
.equ         white      0xffffff



# Codigo
 
.text
    # Chama funcao principal da 1a parte do projeto  
    
    ### nearestCluster
# Determina o centroide mais perto de um dado ponto (x,y).
# Argumentos:
# a0, a1: (x, y) point
# Retorno:
# a0: cluster index
    
    jal cleanScreen
     
    jal mainKMeans 

    jal printClusters
    
    jal printCentroids

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
    li a2, white
    li t3, 32
    # save return adress to main function
    addi sp, sp, -4    
    sw ra , 0(sp)
    
    ForX:
        jal ra, ForY
        li t1, 0
        addi t0, t0, 1
        blt t0, t3, ForX # while i < 32
        
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
        blt t1, t3, ForY # while j < 32
        jr ra

    
### printClusters
# Pinta os agrupamentos na LED matrix com a cor correspondente.
# Argumentos: nenhum
# Retorno: nenhum

printClusters:
    li t0, 0
    lw t2, n_points
    # t3 is used to save offsets
    # t4 is used to save colours
    # t5 is used to save the index of the cluster the point belongs to
    # save return adress to main function
    addi sp, sp, -4    
    sw ra , 0(sp)
    
    ForprintClusters:
        la t1, points
        slli t3, t0, 3
        add t3, t1, t3
        lw a0, 0(t3)
        lw a1, 4(t3)
        
        la t1, clusters
        slli t3, t0, 2
        add t3, t1, t3
        lw t5, 0(t3)
        
        la t4, colors
        li t3, 0
        bne t5, t3, printpass
        lw a2, 0(t4)
        printpass:
        addi t3, t3, 1
        bne t5, t3, printpass1
        lw a2, 4(t4)
        printpass1:
        addi t3, t3, 1
        bne t5, t3, printpass3
        lw a2, 8(t4)
        printpass3:
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
        slli t3, t0, 2
        li a2, black
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
    # save return adress to main function and other registers 
    addi sp, sp, -16
    sw s0 , 0(sp)
    sw s1 , 4(sp)
    sw s2 , 8(sp)
    sw ra , 12(sp)
    
    li s0, 0 # index 0 to k-1
    lw s1, k # number of clusters
    li s2, 0 # counts the number of points in the sum
    li t0, 0 # index 0 to npoints-1
    # t1 is used to save the adress of the points, clusters and centroids
    lw t2, n_points
    # t3 is used to calculate the ofsets 
    li t4, 0 # sum of x coord
    li t5, 0 # sum of y coord
    # t6 is used to temporarily house values 
    
    
    OuterforcalculateCentroids:
        li s2, 0 # reset
        li t0, 0 # reset 
        ForcalculateCentroids:
            bgt t0, t2, secondpart
            la t1, clusters
            slli t3, t0, 2    
            add t3, t1, t3    # t3 = t1 + 4
            lw t6, 0(t3)    # index of the cluster the point in the index t0 belongs
            beq t6, s0, cond    # if the point belongs to the cluster with the index s0
            addi t0, t0, 1    # t0++
            j ForcalculateCentroids
            cond:
            addi s2, s2, 1 # s2++
            la t1, points
            slli t3, t0, 3
            add t3, t1, t3
            lw t6, 0(t3)    # t6 = t3[0]
            add t4, t4, t6    # t4 += t6
            lw t6, 4(t3)    # t6 = t3[1]
            add t5, t5, t6    # t5 += t6
            addi t0, t0, 1    # t0++
            j ForcalculateCentroids
        secondpart:
        bnez s2, nomemptycluster  # there are points in the centroids cluster
        jal initializeCentroids    # OPTIMIZATION when there are centroids that are isolated 
        # (the cluster is empty)refresh centroids
        j endofCalcCentroid    # skip the rest of the process
        nomemptycluster:
        div t4, t4, s2
        div t5, t5, s2
        # saves the centroid in the index s0 (lines below)
        la t1, centroids
        slli t3, s0, 3
        add t3, t1, t3
        lw t1, 0(t3)
        bne t1, t4, diferentcentroid1
        addi s5, s5, 1
        diferentcentroid1:
        sw t4, 0(t3)
        lw t1, 4(t3)
        bne t1, t5, diferentcentroid2
        addi s5, s5, 1
        diferentcentroid2:
        sw t5, 4(t3)
        
        centroidstaysthesame:
        addi s0, s0, 1    # increments cluster index
        bne s0, s1, OuterforcalculateCentroids    # if s0 != k do cicle again
    
    endofCalcCentroid:
    
    lw s0 , 0(sp)
    lw s1 , 4(sp)
    lw s2 , 8(sp)
    lw ra , 12(sp)
    addi sp, sp, 16
    
    jr ra


### mainSingleCluster
# Funcao principal da 1a parte do projeto.
# Argumentos: nenhum
# Retorno: nenhum

mainSingleCluster:
    
    addi sp, sp, -4
    sw ra, 0(sp)

    jal ra, cleanScreen

    jal ra, printClusters

    jal ra, calculateCentroids

    jal ra printCentroids

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
    
    addi sp, sp, -12
    sw t0, 0(sp)
    sw t1, 4(sp)
    sw t2, 8(sp)
    
    li, t2, -1
    
    sub t0, a0, a2
    bgez t0, positiveNum1 # if the sub is positive
    mul t0, t0, t2
    positiveNum1:
    sub t1, a1, a3
    bgez t1, positiveNum2 # if the sub is positive
    mul t1, t1, t2
    positiveNum2:
    add a0, t0, t1
    
    lw t0, 0(sp)
    lw t1, 4(sp)
    lw t2, 8(sp)
    addi sp, sp, 12
    
    jr ra
    
### nearestCluster
# Determina o centroide mais perto de um dado ponto (x,y).
# Argumentos:
# a0, a1: (x, y) point
# Retorno:
# a0: cluster index

nearestCluster:
    
    addi sp, sp, -28
    sw t0, 0(sp)
    sw t1, 4(sp)
    sw t2, 8(sp)
    sw t3, 12(sp)
    sw t4, 16(sp)
    sw t5, 20(sp)
    sw ra, 24(sp)
    
    lw t0, k
    la t1, centroids    # centroid "pointer"
    add t3, x0, a0    # save the x coordinate
    # t4 is going to be the offset / offset stack pointer
    li t5, 62 # t5 is going to be the biggest distance
    # default to the biggest distance
    
    fornearestCluster: 
        addi t0, t0, -1    # k--
        add a0, x0, t3    # set a0 to x
        slli t4, t0, 3    # offset 
        add t4, t1, t4    # offset the pointer
        lw a2, 0(t4)    # centroid x
        lw a3, 4(t4)    # centroid y
        jal ra, manhattanDistance    # calculate distance
        bge a0, t5, pass
        add t5, x0, a0    # save de distance
        add t2, x0, t0    # save the index
        pass:
        bgtz t0, fornearestCluster # while (k >= 0)
    add a0, x0, t2
    
    lw t0, 0(sp)
    lw t1, 4(sp)
    lw t2, 8(sp)
    lw t3, 12(sp)
    lw t4, 16(sp)
    lw t5, 20(sp)
    lw ra, 24(sp)
    addi sp, sp, 28
    
    jr ra
    


### initializeCentroids
# pseudoramdomly generates coordenates for the initial centroids
# using Linear Congruential Generator 
# Argumentos: nenhum
# Retorno: nenhum

initializeCentroids:
    
    li t0, 31    # the values can vary from 0 to 31
    lw t1, k
    slli t1, t1, 1    
    addi t1, t1, -1    # number of numbers to generate -1
    # t2 is used to gain time (so that the clock can change)
    # t3 is going to hold the random number
    li t4, 0    #index
    # t5 is going to be used to house the centroids aderess
    # t6 is used for the offset and special case
    
    randomLoop:
    li a7, 30
    ecall    # get number from clock
    
    li t2, 100000 
    rem a0, a0, t2    # gets the last 5 digits of the clock value
    # does operations to randomize the value
    add t3, t3, a0
    li t2, 443
    mul t3, t3, t2
    li t2, 5201
    add t3, t3, t2
    li t2, 3744
    rem t3, t3, t2
    
    rem t3, t3, t0    # so the number is betwen 0 and 31
    bgtz t3, positive # if the random number is negative
    addi t6, x0, -1
    mul t3, t3, t6
    li t6, 0
    positive:
    la t5, centroids    
    slli t6, t4, 2
    add t5, t5, t6
    sw t3, (0)t5
    li t2, 1000
    loopToMakeTime:    
    # loop so the clock value has time to get a substantial change
    addi t2, t2, -1
    bnez t2, loopToMakeTime
    addi t4, t4, 1
    bge t1, t4, randomLoop
    
    jr ra

### calculatesClusters
# calculates the clusters that each point exists
# Argumentos: nenhum
# Retorno: nenhum

CalcClusters:
    
    addi sp, sp, -4
    sw ra, 0(sp)

    li t1, 0
    lw t2, n_points
    # t3 is used to store the adress to the points and clusters vectors
    
    forCalcClusters:
        la t3, points
        slli t4, t1, 3
        add t4, t3, t4
        lw a0, 0(t4) 
        lw a1, 4(t4)   
        jal nearestCluster  
        la t3, clusters
        slli t4, t1, 2    
        add t3, t3, t4 
        sw a0, 0(t3)   
        addi t1, t1, 1
        bne t1, t2, forCalcClusters
        
    lw ra, 0(sp)
    addi sp, sp, 4
    jr ra


### mainKMeans
# Executa o algoritmo *k-means*.
# Argumentos: nenhum
# Retorno: nenhum

mainKMeans:  
    
    addi sp, sp, -4
    sw ra, 0(sp)
    
    jal initializeCentroids
    
    lw s4, k
    slli s4, s4, 1
    li s5, 0    # only if s5 = 2*k the program ends (the centroids aren't changing)
        
    jal CalcClusters    
    
    forMainKMeans:
        
        li s5, 0
         
        jal calculateCentroids
        
        jal CalcClusters
        
        bne s4, s5, forMainKMeans
 
    lw ra, 0(sp)
    addi sp, sp, 4
    jr ra
