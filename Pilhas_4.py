placasCarros = ['1', '2', '3', '4', '5'] # placas dos carros

def estacionamento(placas): # função para administração de um estacionamento
    pilha = [] # uma lista vazia para ser a pilha

    def estacionar(placa): # função para adicionar uma placa de carro na pilha
        pilha.append(placa) # adiciona uma placa de carro na pilha

    def saida(placa): # função para retirar uma placa de carro na pilha
        if placa not in pilha: # confere se tem determinada placa na pilha
            return "Carro não encontrado." # se não tiver a placa do carro na pilha, ele retorna 'Carro não encontrado'
        
        pilhaTemporaria = [] # uma lista vazia temporaria para ser a pilha de placas dos carros que precisarão sair para que um carro específico possa sair
        while pilha and pilha[-1] != placa: # percorre a pilha até encontrar a placa do carro que irá sair
            pilhaTemporaria.append(pilha.pop()) # então remove os carros necessários para o carro poder sair
        
        if pilha:
            pilha.pop()  # remove o carro que precisa sair
        pilhaTemporaria.reverse() # reorganiza a lista de pilhas na ordem original
        return pilhaTemporaria # retorna a lista vazia temporaria para ser a pilha de placas dos carros que precisaraão sair para que um carro específico possa sair

    
    for p in placas: # percorre a pilha de placas de carros
        estacionar(p) # adiciona as placas dos carros ao estacionamento

    carrosSair = placas[1] # determina o carro que irá sair, como no caso está placa[1], o carro a sair é o 2, pois é a posição que ele está na pilha placasCarro, sendo assim necessário sair os carros '3', '4', '5'
    sequenciaSair = saida(carrosSair)
    print(f"Carros que devem ser retirados para o carro {carrosSair} sair: {sequenciaSair}")
estacionamento(placasCarros)