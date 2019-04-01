
import matplotlib.pyplot as plt
import pandas as pd
from os import listdir

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

# le o arquivo csv inserido assim que um nome correto for digitado
arquivos = []
for arq in listdir():
    if '.csv' in arq:
        arquivos.append(arq)

for i in range(len(arquivos)):
    print(i, [arquivos[i]])

while True:
    try:
        f = pd.read_csv(arquivos[int(input("Digite o indice do CSV:\n"))])
    except OSError as e:
        print("Arquivo nao encontrado")
    except IndexError:
        print("Indice nao existente")
    else:
        break
# imprime os nomes coletados das colunas
a = 0
validos = []
for col in f:
    validos.append(a)
    print(a, col.split())
    a += 1

i = tentaIndice("Digite o indice que sera plotado em X:\n", validos)
j = tentaIndice("Agora digite o indice que sera plotado em Y:\n", validos)

# plota os valores
x = f[f.columns[i]]
y = f[f.columns[j]]
plt.plot(x, y)
plt.xlabel(f.columns[i])
plt.ylabel(f.columns[j])
plt.show()
