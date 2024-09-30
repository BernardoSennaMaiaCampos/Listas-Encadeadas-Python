maiorElemento = [3, 5, 1, 9, 2]

def maior_elemento(pilha): # Função para retornar o maior elemento da pilha
    if not pilha: # confere se a pilha está vazia
        return None  # retorna 'None' se a pilha estiver vazia
    return max(pilha) # a pilha não estando vazia, retorna o maior elemento
print(maior_elemento(maiorElemento))  

