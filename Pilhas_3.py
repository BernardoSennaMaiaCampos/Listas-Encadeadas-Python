pilha_a = [1, 2, 3] # primeira pilha
pilha_b = [1, 2, 3] # segunda  -
pilha_c = [1, 2, 4] # terceira -

def pilhasIguais(pilha1, pilha2): # função para ver se duas pilhas são iguais
    return pilha1 == pilha2 # confere se as pilhas são iguais, se for igual, retorna um booleno True, se não for igual, retorna um booleano falso
print(pilhasIguais(pilha_a, pilha_b))  
print(pilhasIguais(pilha_a, pilha_c))  