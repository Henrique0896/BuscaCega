from buscas import buscaLargura, buscaProfundidadeLI
from manipularArquivo import lerArquivo, escreverArquivo

estadoInicial, estadoFinal = lerArquivo('estadoInicial.txt', 'estadoFinal.txt')

caminho = buscaLargura(estadoInicial, estadoFinal)

caminho2 = buscaProfundidadeLI(estadoInicial, estadoFinal)

escreverArquivo('caminho.txt', caminho, caminho2)