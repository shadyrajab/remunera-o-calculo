import streamlit as st


def values():
    if "dataframe" in st.session_state:
        c1, c2, c3, c4 = st.columns(4)
        st.session_state.salario = c1.number_input("Salário do Consultor")
        st.session_state.ajuda = c2.number_input("Ajuda de Custo")
        st.session_state.estorno = c3.number_input("Valor à ser Estornado")
        st.session_state.adiantamento = c4.number_input("Valor do adiantamento")