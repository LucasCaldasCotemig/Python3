import streamlit as st
import pandas as pd

horarios = {
    "510": ["05:30", "06:15", "07:00", "07:45", "08:30"],
    "520": ["05:50", "06:40", "07:30", "08:20", "09:10"],
    "550": ["06:00", "06:50", "07:40", "08:30", "09:20"],
    "620": ["05:40", "06:30", "07:20", "08:10", "09:00"],
}

passageiros = {
    "510": 1250,
    "520": 980,
    "550": 1530,
    "620": 740,
}

st.title("Expresso Mobilidade")
st.subheader("Painel do Operador")

nome = st.text_input("Digite seu nome:")
st.write("Olá,", nome)

linha = st.selectbox(
    "Escolha uma linha:",
    ["510", "520", "550"]
)
st.write("Linha selecionada:", linha)

tabela_horarios = pd.DataFrame({
    "Horários da linha " + linha: horarios[linha],
})
st.write(tabela_horarios)

linhas = st.multiselect(
    "Escolha as linhas:",
    ["510", "520", "550", "620"]
)
st.write(linhas)

if st.button("Calcular"):
    st.write("Calculando...")

    if len(linhas) == 0:
        st.write("Selecione pelo menos uma linha para calcular.")
    else:
        resultado = {
            "Linha": [],
            "Passageiros por dia": [],
            "Ônibus necessários": [],
        }

        for item in linhas:
            resultado["Linha"].append(item)
            resultado["Passageiros por dia"].append(passageiros[item])
            resultado["Ônibus necessários"].append(int(passageiros[item] / 80) + 1)

        df = pd.DataFrame(resultado)
        st.write(df)
        st.write(f"Total de ônibus na operação: {df['Ônibus necessários'].sum()}")
