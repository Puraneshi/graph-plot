
import matplotlib.pyplot as plt
import pandas as pd
from os import listdir

'''
Resumo do código:
f = pd.read_csv("arquivo.csv")  <- carrega o csv na memória
x = f["coluna_i"]               <- lista de valores de x
y = f["coluna_j"]               <- lista de valores de y
plt.plot(x, y)                  <- cria o grafico com cada par x,y
plt.show()                      <- exibe o gráfico
O resto do código serve para evitar erros de entrada, adicionar legendas ao gráfico e etc
'''
# funcao para coletar o indice correto
def tentaIndice(frase, validos):
    while True:
        try:
            e = int(input(frase))
        except ValueError:
            print("Digite um numero valido")
        else:
            try:
                validos[e]
            except IndexError:
                print("Indice nao existe")
            else:
                break
    return e

# encontra e exibe os arquivos csv na pasta
arquivos = []
for arq in listdir():
    if '.csv' in arq:
        arquivos.append(arq)

for i in range(len(arquivos)):
    print(i, [arquivos[i]])

# pede ao usuario o indice do csv até que um valido seja indicado
while True:
    try:
        f = pd.read_csv(arquivos[int(input("Digite o indice do CSV:\n"))])
    except OSError as e:
        print("Arquivo nao encontrado")
    except IndexError:
        print("Indice nao existente")
    else:
        break

# imprime os nomes das colunas presentes no arquivo
a = 0
validos = []
for col in f:
    validos.append(a)
    print(a, col.split())
    a += 1

# recebe input do usuário para valores de x e y
i = tentaIndice("Digite o indice que sera plotado em X:\n", validos)
j = tentaIndice("Agora digite o indice que sera plotado em Y:\n", validos)

# plota os valores
x = f[f.columns[i]]
y = f[f.columns[j]]
plt.plot(x, y)
# muda o nome dos eixos
plt.xlabel(f.columns[i])
plt.ylabel(f.columns[j])
# exibe gráfico
plt.show()
