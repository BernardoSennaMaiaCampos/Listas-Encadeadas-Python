pilhaInvertida = [1.5, 2.3, 3.4, 4.5]

def inverterPilha(pilha): # função para inverter a pilha
    pilhaSequencia = [] # uma lista vazia para ser a pilha
    
 
    for num in pilha: # percorre os elementos dentro da pilha
        pilhaSequencia.append(num) # empilha cada elemento
    
   
    while pilhaSequencia: # enquanto percorre a pilha...
        print(pilhaSequencia.pop()) # ...remve e imprime o primeiro elemento da pilha
inverterPilha(pilhaInvertida)