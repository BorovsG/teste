import streamlit as st

# Tabela de preços (dicionários para melhor organização)
precos_hotel1 = {1: 20, 2: 28, 3: 35, 4: 42, 5: 48, 6: 53}
precos_hotel2 = {1: 25, 2: 34, 3: 42, 4: 50, 5: 57, 6: 63}

def calcular_orcamento(hotel, qpessoas, dias):
    if hotel == 1:
        diaria = precos_hotel1[qpessoas]
    else:
        diaria = precos_hotel2[qpessoas]
    return diaria * dias

def main():
    st.title("Sistema de Reservas ADSResorts")

    # Input dos dados do cliente
    nome = st.text_input("Digite seu nome completo:")
    cpf = st.text_input("Digite seu CPF:")
    hotel = st.selectbox("Escolha o hotel desejado:", options=["Hotel Executive", "Hotel Delux"])
    qpessoas = st.number_input("Digite a quantidade de hóspedes:", min_value=1, max_value=6)
    dias = st.number_input("Digite a quantidade de dias:")

    # Botão para calcular o orçamento e exibir os resultados
    if st.button("Calcular Orçamento"):
        orcamento = calcular_orcamento(hotel, qpessoas, dias)

        st.write("---")
        st.subheader("Resumo da Reserva")
        st.write(f"Nome: {nome}")
        st.write(f"CPF: {cpf}")
        st.write(f"Hotel escolhido: {hotel}")
        st.write(f"Quantidade de hóspedes: {qpessoas}")
        st.write(f"Quantidade de dias: {dias}")
        st.write(f"Orçamento total: R$ {orcamento:.2f}")

        # Confirmação da reserva
        confirmacao = st.radio("Deseja confirmar sua reserva?", ("Sim", "Não"))
        if confirmacao == "Sim":
            st.success("Sua reserva foi realizada com sucesso!")
        else:
            st.error("Sua reserva foi cancelada.")

if __name__ == "__main__":
    main()

