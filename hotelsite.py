import streamlit as st

# Tabela de preços (mesma que no código original)
hotel1 = [0, 20, 28, 35, 42, 48, 53]
hotel2 = [0, 25, 34, 42, 50, 57, 63]

def calcular_orcamento(hotel, qpessoas, dias):
    if hotel == 1:
        diaria = hotel1[qpessoas]
    else:
        diaria = hotel2[qpessoas]
    return diaria * dias

def main():
    st.title("Sistema de Reservas ADSResorts")

    # Coleta de dados
    nome = st.text_input("Digite seu nome completo")
    cpf = st.text_input("Digite seu CPF")
    hotel = st.selectbox("Escolha o hotel desejado:", options=["Hotel Executive", "Hotel Delux"])
    qpessoas = st.number_input("Digite a quantidade de hóspedes (1 a 6):", min_value=1, max_value=6, value=1)
    dias = st.number_input("Digite a quantidade de dias:", min_value=1, value=1)

    # Botão para calcular o orçamento
    if st.button("Calcular Orçamento"):
        orcamento = calcular_orcamento(hotel, qpessoas, dias)

        # Apresentação dos resultados
        st.write(f"**Resumo da Reserva**")
        st.write(f"Nome: {nome}")
        st.write(f"CPF: {cpf}")
        st.write(f"Hotel: {hotel}")
        st.write(f"Hóspedes: {qpessoas}")
        st.write(f"Dias: {dias}")
        st.write(f"Orçamento: R${orcamento:.2f}")

        # Confirmação da reserva
        
def limpar_estado():
    global nome, cpf, hotel, qpessoas, dias, orcamento
    nome = ""
    cpf = ""
    hotel = None
    qpessoas = None
    dias = None
    orcamento = None

if __name__ == "__main__":
    continuar = True
    while continuar:
        main()

        # Opção de continuar ou não
        continuar = st.radio("Deseja realizar outra reserva?", ("Sim", "Não"))
        continuar = continuar == "Sim"

        if continuar:
            limpar_estado()
            st.success("Preparando para uma nova reserva!")

