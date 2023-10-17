# Show progress
import streamlit as st
import time


st.title("Show progress 📊")

st.markdown('''
    ## Mostrar progresso
    Ao adicionar cálculos de execução longa a um aplicativo, você pode usar `st.progress()` para exibir o status em tempo real.

    Primeiro, vamos importar o tempo. Vamos usar o método `time.sleep()` para simular um cálculo de longa duração:           
''')

'Starting a long computation...'

# add placeholder
latest_itereration = st.empty()
bar = st.progress(0)

for i in range(100):
    # Atualize a barra de progresso com cada iteração.
    latest_itereration.text(f"Iteration {i+1}")
    bar.progress(i + 1)
    time.sleep(0.1)
    
'Concluído!!!'
    