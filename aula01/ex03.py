import pandas as pd
import matplotlib.pyplot as plt

dados = {
    "Produto" : ["Mesa", "Travesseiro", "Aspirador de Pó"],
    "Preço": [500.00, 35.50, 120.00],
    "Quantidade": [2, 6, 1] 
}

df = pd.DataFrame(dados)

print(df)

# plt.bar(dados["Produto"], dados["Preço"], width=0.5, color="#a5ba00")
# plt.title("Preço dos Produtos")
# plt.xlabel("Produto")
# plt.ylabel("Preço")

plt.bar(dados["Produto"], dados["Quantidade"], width=0.5, color="#a5ba00")
plt.title("Quantidade dos Produtos")
plt.xlabel("Produto")
plt.ylabel("Quantidade")

plt.show()