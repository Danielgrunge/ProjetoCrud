import streamlit as st

st.title("Cadastro Crud")

with st.form(key="include_cliente"):
    input_name = st.text_input(label='Insira seu Nome')
    input_age = st.number_input(label='Insira sua Idade', format='%d', step=1, min_value=0)
    input_occupation = st.selectbox("Selecione sua profissão", ['Desenvolvedor', 'Musico', 'Design','Professor' ])
    input_button_submit = st.form_submit_button(label='Enviar')


if input_button_submit:
    st.write(f'Nome: {input_name}')
    st.write(f'Idade:  {input_age}')
    st.write(f'Profissão:  {input_occupation}')

    