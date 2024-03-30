import streamlit as st
import pandas as pd
import joblib

# Carregar o modelo treinado
model = joblib.load('random_forest_model.pkl')

# Definindo o layout do app
st.title('Previsão de Empréstimo')

# Coletando os dados de entrada do usuário
Age = st.number_input('Idade', min_value=18, max_value=100, step=1)
Current_Loan_Expenses = st.number_input('Despesas Atuais de Empréstimo (USD)', format="%.2f")
Dependents = st.number_input('Dependentes', min_value=0, max_value=10, step=1)
No_of_Defaults = st.number_input('Número de Inadimplências', min_value=0, max_value=10, step=1)
Property_Age = st.number_input('Idade da Propriedade', format="%.2f")
Property_Type = st.selectbox('Tipo de Propriedade', [1, 2, 3, 4])
Co_Applicant = st.selectbox('Co-requerente', [0, 1])

# Previsão
if st.button('Prever'):
    features = pd.DataFrame({
        'Age': [Age],
        'Current Loan Expenses (USD)': [Current_Loan_Expenses],
        'Dependents': [Dependents],
        'No. of Defaults': [No_of_Defaults],
        'Property Age': [Property_Age],
        'Property Type': [Property_Type],
        'Co-Applicant': [Co_Applicant]
    })

    prediction = model.predict(features)

    st.write(f'Previsão de Quantia de Empréstimo Sancionada: R${prediction[0]:,.2f}')
