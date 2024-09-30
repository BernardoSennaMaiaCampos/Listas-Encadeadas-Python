inteiros = [2, 4, 5, 6, 3, 8, 1, 7, 10, 12, 11, 14, 9, 16, 18] # pilha com os inteiros

def TPilha(vetor): # função para receber um vetor de inteiros
    pilha = [] # uma lista vazia para ser a pilha
    
    for numero in vetor: # percorre os números no vetor
        if numero % 2 == 0: # confere se o número é par 
            pilha.append(numero) # o número sendo par, é adicionado a pilha
        else:  
            if pilha:  # caso o número não seja par...
                pilha.pop() # ... o número é retirado da pilha
    
   
    while pilha: # enquanto percorre a pilha
        print(pilha.pop()) # esvazia e imprime os inteiros da pilha
TPilha(inteiros)