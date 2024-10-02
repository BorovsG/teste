import streamlit as st

# Tabela de preços
precos_executivo = [0, 20, 28, 35, 42, 48, 53]
precos_delux = [0, 25, 34, 42, 50, 57, 63]

def calcular_preco(hotel, pessoas, dias):
    if hotel == 1:
        diaria = precos_executivo[pessoas - 1]
    else:
        diaria = precos_delux[pessoas - 1]
    return diaria * dias

def reservar():
    st.title("Sistema de Reservas ADSResorts")

    nome = st.text_input("Digite seu nome completo:")
    cpf = st.text_input("Digite seu CPF:")
    hotel = st.selectbox("Escolha o hotel desejado:", options=["Hotel Executive", "Hotel Delux"])
    pessoas = st.slider("Quantidade de pessoas", 1, 6)
    dias = st.number_input("Digite a quantidade de dias:", min_value=1, value=1)

    if st.button("Calcular"):
        preco = calcular_preco(hotel, pessoas, dias)
        st.write(f"**Resumo da Reserva:**")
        st.write(f"Nome: {nome}")
        st.write(f"CPF: {cpf}")
        st.write(f"Hotel: {hotel}")
        st.write(f"Pessoas: {pessoas}")
        st.write(f"Dias: {dias}")
        st.write(f"Preço total: R${preco:.2f}")

        if st.button("Confirmar Reserva"):
            st.success("Sua reserva foi realizada com sucesso!")
        else:
            st.error("Reserva cancelada.")

if __name__ == "__main__":
    reservar()
