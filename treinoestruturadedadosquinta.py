#treino estrutura de dados quintafeira

#buscalinear

def busca_linear(lista, alvo): 
    for i in range(len(lista)):
        if lista[i] == alvo:
            return i
    return -1
    
lista = [10, 24, 35, 42, 55, 60]    
alvo = 10
resultado = busca_linear(lista, alvo)

if resultado != -1:
    print(f"Elemento encontrado na posiçao: {resultado}")
else:
    print("Elemento nao encontrado")    

#------------------------------------------------------------
#busca binaria so pode ser usada em listas ordenadas

def busca_binaria(lista,alvo):
    esquerda = 0 
    direita = len(lista) - 1
    
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            esquerda =  meio + 1
        else:
            direita = meio - 1
            
        return -1
        
    lista = [10, 24, 35, 42, 55, 60]
    alvo = 16
    resultado = busca_binaria(lista, alvo)
    
    if resultado != -1:
        print(f"Elemento encontrado na posiçao: {resultado}")
    else:
        print("Elemento nao encontrado")
    
        
        
        