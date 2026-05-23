import pandas as pd

# Extract
df = pd.read_csv("clientes.csv")
# Remover espaços em branco dos nomes das colunas
df.columns = df.columns.str.strip()

#Transform
def classificar_cliente(balance):
    if balance >= 5000:
        return "Classificação: Premium"
    elif balance >=1000:
        return "Classificação: Intermediário"
    else:
        return "Classificação: Básico"

def recomendacao(name, balance, age):
    if balance >= 5000 and age >= 55:
        return f"Recomendação: Talvez seja interessante começar a investir na sua aposentadoria,{name}"
    elif balance >= 5000 and age < 55:
        return f"Recomendação: Você tem condições de fazer bons investimentos,{name}!"
    else:
        return "Recomendação: Educação financeira"

# Cria nova coluna de categoria
df["categoria"] = df["balance"].apply(classificar_cliente)
# Cria nova coluna de recomendação
df["recomendacao"] = df.apply(
    lambda row: recomendacao(row["name"], row["balance"], row["age"]),
    axis=1
)

#Load
df.to_csv("clientes_transformados.csv", index=False)

print(df)

