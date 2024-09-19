import streamlit as st

# Dados dos hotéis
hotel1 = [0, 20, 28, 35, 42, 48, 53]
hotel2 = [0, 25, 34, 42, 50, 57, 63]

# Título da aplicação
st.title("Sistema de Reservas da ADSResorts")
st.write("Seja muito bem-vindo ao sistema de reservas!")

# Escolha do hotel
hotel = st.selectbox("Escolha o hotel desejado:", options=["Hotel 1", "Hotel 2"])

# Quantidade de pessoas
qpessoas = st.number_input("Digite a quantidade de hóspedes (1 a 6):", min_value=1, max_value=6, value=1)

# Quantidade de dias
dias = st.number_input("Digite a quantidade de dias:", min_value=1, value=1)

# Exibir resumo das informações
if st.button("Calcular"):
    if hotel == "Hotel 1":
        preço = hotel1[qpessoas]
    else:
        preço = hotel2[qpessoas]
    
    st.write(f"**Hotel selecionado:** {hotel}")
    st.write(f"**Quantidade de hóspedes:** {qpessoas}")
    st.write(f"**Quantidade de dias:** {dias}")
    st.write(f"**Preço total:** R$ {preço * dias:.2f}")