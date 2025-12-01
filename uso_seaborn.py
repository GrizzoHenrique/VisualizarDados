import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df= pd.read_csv('clientes-v3-preparado.csv')
print(df.head().to_string())

# Gráfico de Dispersão
sns.jointplot(x='idade',y='salario',data=df,kind ='scatter')#[''sacatter','hist','hex','kde','reg','resid']
plt.show()

# Gráfico de densidade
plt.figure(figsize=(10, 6))
sns.kdeplot(
    data=df,
    x='salario',
    fill=True,
    color='#a713d4'
)
plt.title('Densidade Salários')
plt.xlabel('Salario')
plt.show()

# Gráfico de Pairplot - Dispersão e Histograma
sns.pairplot(df[['idade','salario','anos_experiencia','nivel_educacao_cod']]) #https://seaborn.pydata.org/tutorial/color_palettes.html
plt.show()

# Gráfico de Regressão
sns.regplot(x='idade',y='salario', data=df, color='#f0e80a', scatter_kws={'alpha':0.5, 'color':'#f0850a'})
plt.title('Regressão de Salário por Idade')
plt.xlabel('Idade')
plt.ylabel('Salário')
plt.show()

# Gráfico countplot com hue
sns.countplot(x='estado_civil', hue='nivel_educacao', data=df, palette='pastel')
plt.xlabel('Estado Civil')
plt.ylabel('Quantidade de Clientes')
plt.legend(title='Nivel de Educação')
plt.show()
