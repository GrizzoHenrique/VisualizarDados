import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('clientes-v3-preparado.csv')
print(df.head(20).to_string())

# Gráfico de Barras
plt.figure(figsize=(10,6))
df['nivel_educacao'].value_counts().plot(kind='bar', color='#2feb1a')# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html#pandas
plt.title('Divisão de Escolaridade - 1')
plt.xlabel('Nível de Educação')
plt.ylabel('Quantidade')
plt.xticks(rotation = 0)
plt.show()

x = df['nivel_educacao'].value_counts().index.astype(str).tolist()
y = df['nivel_educacao'].value_counts().values.tolist()

plt.figure(figsize=(10,6))
plt.bar(x, y, color='#a713d4')
plt.title('Divisão de Escolaridade - 2')
plt.xlabel('Nivel de Educação')
plt.ylabel('Quantidade')

# Gráfico de Pizza
plt.figure(figsize=(10, 6))
plt.pie(y, labels= x,autopct='%.1F%%', startangle= 90)
plt.title('Distribuição de Nivel de Educação')
plt.show()

# Gráfico de Dispersão
plt.hexbin(df['idade'],df['salario'], gridsize=40, cmap='Blues') # https://matplotlib.org/stable/users/explain/colors/colormaps.html
plt.colorbar(label='Contagem dentro do Bin')
plt.xlabel('idade')
plt.ylabel('Salário')
plt.title('Dispersão de Idade e Salário')
plt.show()

# Criar o Gráfico de pizza
plt.figure(figsize=(8,8))
