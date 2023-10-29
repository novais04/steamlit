import streamlit as st
import time
import numpy as np

st.set_page_config(
    page_title="Plotting Demo",
    page_icon="📈"
)

st.title("Plotiing Demo")
st.sidebar.header("Plotting Demo")
st.markdown('''
Esta demonstração ilustra uma combinação de plotagem e animação com `Streamlit`. 
Estamos gerando um monte de números aleatórios em um loop para 5 segundos. 
### Divirta-se com isso!
''')
progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()
last_row = np.random.randn(1,1)
chart = st.line_chart(last_row)

for i in range(1, 101):
    new_rows = last_row[-1,:] + np.random.randn(5,1).cumsum(axis=0)
    status_text.text("%i%% Complete" % i)
    chart.add_rows(new_rows)
    progress_bar.progress(i)
    last_row = new_rows
    time.sleep(0.05)

progress_bar.empty()
# Os widgets do Streamlit executam automaticamente o script de cima para baixo. Desde
# este botão não está ligado a qualquer outra lógica, ele só causa uma planície
# rerun.

st.button("Re-run")