import numpy as np

def soma(va: float, vb: float):
    ''' Função que retorna a soma entre dois valores
    '''
    return va + vb

def sub(va: float, vb: float):
    ''' Função que retorna a subtração entre dois valores
    '''
    return va - vb

def multiplicacao(va: float, vb: float):
    ''' Função que retorna a multiplicação entre dois valores
    '''
    return va * vb

def divisao(va: float, vb: float):
    ''' Função que retorna a divisão entre dois valores
    '''
    
    if vb == 0:
        return np.inf

    return va / vb

def media_lista_valores(v:list):
    ''' Função que retorna a média entre N valores
    '''
    l=[]
    
    for i in v:
        if isinstance(i, (int, float)):
            l.append(i)
    
    if len(l) == 0:
        return 0
    
    
    return np.mean(l)
        
