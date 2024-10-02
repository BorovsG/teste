import streamlit as st

def calcular_orcamento(hotel, qpessoas):
  # Definimos as listas de preços dos hotéis aqui
  hotel1 = [0, 20, 28, 35, 42, 48, 53]
  hotel2 = [0, 25, 34, 42, 50, 57, 63]

  if hotel == 1:
    diaria = hotel1[qpessoas]
  else:
    diaria = hotel2[qpessoas]
  return diaria

def main():
  while True:
    st.title("Sistema de Reservas ADSResorts")
    name_key = f"name_{i}"  
    nome = st.text_input("Digite seu nome completo:", key=name_key)
    i += 1  
    cpf = st.text_input("Digite seu CPF:")
    hotel = st.selectbox("Escolha o hotel desejado:", options=["Hotel Executive", "Hotel Delux"])
    qpessoas = st.number_input("Digite a quantidade de hóspedes:", min_value=1, max_value=6)
    dias = st.number_input("Digite a quantidade de dias:", min_value=1, value=1)
 
    # Botão para calcular o orçamento
    if st.button("Calcular Orçamento"):
      diaria = calcular_orcamento(hotel, qpessoas)
      orcamento = diaria * dias

      # Exibe o resumo da reserva
      st.write(f"Nome: {nome}")
      st.write(f"CPF: {cpf}")
      st.write(f"Hotel escolhido: {hotel}")
      st.write(f"Quantidade de hóspedes: {qpessoas}")
      write(f"Quantidade de dias: {dias}")
      st.write(f"Valor da diária: R$ {diaria:.2f}")
      st.write(f"Orçamento total: R$ {orcamento:.2f}")

      # Confirmação da reserva
      confirmacao = st.radio("Deseja confirmar sua reserva?", ("Sim", "Não"))
      if confirmacao == "Sim":
        st.success("Sua reserva foi realizada com sucesso!")
      else:
        st.error("Sua reserva foi cancelada.")

    # Pergunta se deseja realizar outra reserva
    continuar = st.radio("Desejar realizar outra reserva?", ("Sim", "Não"))
    if continuar == "Não":
      break

if __name__ == "__main__":
  main()

