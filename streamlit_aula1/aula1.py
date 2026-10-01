import streamlit as st
import pandas as pd

nome = "Lucas Caldas Lima"
idade = 17

st.title("Meu primeiro dash")
st.subheader(nome)

st.write("Olá, mundo")
st.write(f"Meu nome é {nome} e tenho {idade} anos")

df = pd.DataFrame({
    "first column": ["Português", "Matemática", "Python", "Frame"],
    "second column": [5, 9, 7, 10],
})

st.write(df)
