from prints import printNoLargura, printNoProfundidade

def mover(estado):
    movimentos = []
    est = eval(estado)
    i = 0
    j = 0
    while 0 not in est[i]: i += 1
    j = est[i].index(0)
    
    if j>0: #mover o 0 para esquerda
        est[i][j], est[i][j-1] = est[i][j-1], est[i][j] 
        movimentos.append(str(est))
        est[i][j], est[i][j-1] = est[i][j-1], est[i][j]

    if i>0: #mover o 0 para cima
        est[i][j], est[i-1][j] = est[i-1][j], est[i][j]  
        movimentos.append(str(est))
        est[i][j], est[i-1][j] = est[i-1][j], est[i][j]

    if j<2: #mover o 0 para direita
        est[i][j], est[i][j+1] = est[i][j+1], est[i][j] 
        movimentos.append(str(est))
        est[i][j], est[i][j+1] = est[i][j+1], est[i][j]
    
    if i<2: #mover o 0 para baixo 
        est[i][j], est[i+1][j] = est[i+1][j], est[i][j] 
        movimentos.append(str(est))
        est[i][j], est[i+1][j] = est[i+1][j], est[i][j]
        
    return movimentos

def buscaLargura(inicial,final): #recebe estado inicial e final
    nosExpandidos = 0
    fila = [[inicial]] #Estado nó inicial na borda
    while True: #Estrutura de repetição
        if not fila: raise Exception # Se a fila estiver vazia retorna falha
        caminho = fila[0] #tem a primeira lista da fila
        fila = fila[1:] #removendo o primeiro elemento da fila
        fimCaminho = caminho[-1] #tem o ultimo nó de caminho
        printNoLargura(fimCaminho, nosExpandidos)
        if fimCaminho == final: break #Se fimCaminho = objetivo então saia do laço
        for movimento in mover(fimCaminho): #Para cada movimento
            fila.append(caminho + [movimento]) #Insere caminho mais movimento
        nosExpandidos+=1
    return caminho #retorne caminho




#Declaração de variável global
noExp = 0

def buscaProfundidadeLimitada(inicial,final,limite): #recebe estado inicial e final
    profundidade = 0 #profundidade começa com 0
    pilha = [[inicial]] #Estado nó inicial na borda
    global noExp
    while True: #Estrutura de repetição
        if not pilha: return None
        else:
            caminho = pilha[-1] #caminho recebe a ultima lista da pilha
            pilha = pilha[:-1] #removendo o ultimo elemento da pilha
            fimCaminho = caminho[-1] #fimCaminho tem o ultimo nó de caminho
            printNoProfundidade(fimCaminho, noExp)
            if fimCaminho == final: break #Se fimCaminho = objetivo então saia do laço
            if profundidade >= limite: continue #Se profundidade é maior que limite volta topo
            for movimento in mover(fimCaminho): #Para cada movimento
                pilha.append(caminho + [movimento]) #Insere caminho mais movimento
            profundidade+=1
            noExp+=1
    return caminho #retorne caminho

    
def buscaProfundidadeLI(inicial,final): #recebe estado inicial e final
    limite = 0
    while True: #Estrutura de repetição
        caminho = buscaProfundidadeLimitada(inicial,final,limite)
        if caminho: break
        limite +=1
    return caminho #retorne caminho


     

           