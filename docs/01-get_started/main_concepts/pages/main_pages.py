import streamlit as st 

st.title("Main Page 🎈")

st.markdown('''
À medida que os aplicativos crescem, torna-se útil organizá-los em várias páginas. Isto torna a aplicação mais fácil de gerir como programador e mais fácil de navegar como utilizador. O Streamlit fornece uma forma simples de criar aplicações de várias páginas.

 Concebemos esta funcionalidade para que a criação de uma aplicação de várias páginas seja tão fácil como criar uma aplicação de página única! Basta adicionar mais páginas a uma aplicação existente da seguinte forma:

1. Na pasta que contém o seu programa principal, crie uma nova pasta `pages` . Digamos que o seu programa principal se chama `main_page.py`.
2. Adicione novos arquivos `.py` na pasta `pages` para adicionar mais páginas ao seu aplicativo.
3. Execute streamlit run `main_page.py` como de costume.

É isso! O script main_page.py agora corresponderá à página principal do seu aplicativo. E irá ver os outros programas da pasta de páginas no selector de páginas da barra lateral. Por exemplo:
''')

st.sidebar.markdown("Main page 🎈")

