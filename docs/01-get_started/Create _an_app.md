# Create an app

[Fonte](https://docs.streamlit.io/library/get-started/create-an-app)

Se você chegou até aqui, é provável que você tenha instalado o Streamlit e executado o básico em nosso guia de conceitos principais. Se não, agora é um bom momento para dar uma olhada.

A forma mais fácil de aprender a usar o Streamlit é experimentar as coisas por si mesmo. Ao ler este guia, teste cada método. Enquanto o aplicativo estiver em execução, sempre que você adicionar um novo elemento ao script e salvar, a interface do usuário do Streamlit perguntará se você deseja executar novamente o aplicativo e visualizar as alterações. Isso permite que você trabalhe em um loop interativo rápido: você escreve algum código, salva, revisa a saída, escreve mais e assim por diante, até ficar feliz com os resultados. O objetivo é usar o Streamlit para criar um aplicativo interativo para seus dados ou modelo e usar o Streamlit para revisar, depurar, aperfeiçoar e compartilhar seu código.

Neste guia, você usará os principais recursos do Streamlit para criar um aplicativo interativo; explorando um conjunto de dados público do Uber para coletas e devoluções em Nova York. Quando terminar, você saberá como buscar e armazenar em cache dados, desenhar gráficos, plotar informações em um mapa e usar widgets interativos, como um controle deslizante, para filtrar resultados.

## Crie seu primeiro aplicativo

O Streamlit é mais do que apenas uma maneira de criar aplicativos de dados, é também uma comunidade de criadores que compartilham seus aplicativos e ideias e ajudam uns aos outros a melhorar seu trabalho. Por favor, junte-se a nós no fórum da comunidade. Nós adoramos ouvir suas perguntas, ideias e ajudá-lo a resolver seus bugs - pare por hoje!

1. O primeiro passo é criar um novo script Python. Vamos chamá-lo `uber_pickups.py`.

2. Abra o `uber_pickups.py` no seu IDE ou editor de texto favorito e adicione estas linhas:
```
    import streamlit as st 
    import pandas as pd 
    import numpy as np 
```
3. Cada bom aplicativo tem um título, então vamos adicionar um:
```
    st.title('Uber pickup in NYC')
```
4. Agora é altura de executar o Streamlit a partir da linha de comandos:

``` 
    streamlit run uber_pickups.py 
```
> Sabia que também pode passar um URL para o streamlit run? Isto é óptimo quando combinado com o GitHub Gists. Por exemplo:
```
streamlit run https://raw.githubusercontent.com/novais04/steamlit/main/docs/01-get_started/uber_pickups.p
```
5. Como de costume, o aplicativo deve abrir automaticamente em uma nova guia no seu navegador.
   
## Buscando alguns dados
Agora que você tem um aplicativo, a próxima coisa que você precisa fazer é buscar o conjunto de dados do Uber para coletas e devoluções em Nova York.

1 . Vamos começar por escrever uma função para carregar os dados. Adicione este código ao seu programa:
```
DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data 
```

Você notará que __load_data__\ é uma função antiga que baixa alguns dados, os coloca em um dataframe Pandas e converte a coluna de data de texto para data. A função aceita um único parâmetro (__nrows__), que especifica o número de linhas que você deseja carregar no dataframe.

2. Agora vamos testar a função e rever o resultado. Por baixo da sua função, adicione estas linhas:



Você verá alguns botões no canto superior direito do seu aplicativo perguntando se deseja executar novamente o aplicativo. Escolha Sempre executar novamente e você verá suas alterações automaticamente sempre que salvar.

Ok, isso é decepcionante...

Acontece que leva muito tempo para baixar dados e carregar 10.000 linhas em um dataframe. Converter a coluna date em datetime também não é um trabalho rápido. Você não quer recarregar os dados cada vez que o aplicativo é atualizado - felizmente o Streamlit permite que você armazene os dados em cache.
