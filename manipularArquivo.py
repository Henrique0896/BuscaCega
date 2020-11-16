def lerArquivo(name, name2):
    try:
        estado = []
        arquivo = open(name, 'r')
        for i in arquivo:
            linha = i.split()
            temp = []
            for j in range(len(linha)):
                temp.append( int(linha[j]) )
            estado.append(temp)
        estado2 = []
        arquivo = open(name2, 'r')
        for i in arquivo:
            linha = i.split()
            temp = []
            for j in range(len(linha)):
                temp.append( int(linha[j]) )
            estado2.append(temp)
    except ValueError:
        print('Erro ao tentar manipular arquivo {}'.format(ValueError))
    finally:
        arquivo.close()
    return str(estado), str(estado2)

def escreverArquivo(name, caminho, caminho2):
    try:
        arquivo = open(name, 'w')
        arquivo.write("Usando Busca em Largura:\n")
        for i in range( len(caminho) ):
            str1 = str(caminho[i][2])
            str2 = str(caminho[i][5])
            str3 = str(caminho[i][8])
            str4 = str(caminho[i][13])
            str5 = str(caminho[i][16])
            str6 = str(caminho[i][19])
            str7 = str(caminho[i][24])
            str8 = str(caminho[i][27])
            str9 = str(caminho[i][30])

            arquivo.write("Estado: %d\n" %(i+1))

            arquivo.write(str1)
            arquivo.write(' ')
            arquivo.write(str2)
            arquivo.write(' ')
            arquivo.write(str3)
            arquivo.write('\n')
            arquivo.write(str4)
            arquivo.write(' ')
            arquivo.write(str5)
            arquivo.write(' ')
            arquivo.write(str6)
            arquivo.write('\n')
            arquivo.write(str7)
            arquivo.write(' ')
            arquivo.write(str8)
            arquivo.write(' ')
            arquivo.write(str9)
            arquivo.write("\n")
            arquivo.write("\n")

        arquivo.write("Usando Busca em Profundidade Limitada Iterativa:\n")
        for i in range( len(caminho2) ):
            str1 = str(caminho2[i][2])
            str2 = str(caminho2[i][5])
            str3 = str(caminho2[i][8])
            str4 = str(caminho2[i][13])
            str5 = str(caminho2[i][16])
            str6 = str(caminho2[i][19])
            str7 = str(caminho2[i][24])
            str8 = str(caminho2[i][27])
            str9 = str(caminho2[i][30])

            arquivo.write("Estado: %d\n" %(i+1))

            arquivo.write(str1)
            arquivo.write(' ')
            arquivo.write(str2)
            arquivo.write(' ')
            arquivo.write(str3)
            arquivo.write('\n')
            arquivo.write(str4)
            arquivo.write(' ')
            arquivo.write(str5)
            arquivo.write(' ')
            arquivo.write(str6)
            arquivo.write('\n')
            arquivo.write(str7)
            arquivo.write(' ')
            arquivo.write(str8)
            arquivo.write(' ')
            arquivo.write(str9)
            arquivo.write("\n")
            arquivo.write("\n")
    except ValueError:
        print('Erro ao tentar manipular arquivo {}'.format(ValueError))
    finally:
        arquivo.close()
    