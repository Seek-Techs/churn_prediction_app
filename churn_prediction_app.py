import streamlit as st
import joblib

def main():
    # Load the model
    try:
        model = joblib.load('churn_predict_model')
    except FileNotFoundError:
        st.error("Model file not found. Please make sure the model file exists.")
        return
    except Exception as e:
        st.error(f"Error loading the model: {e}")
        return
    
    # Set up the UI
    st.title('Bank Customers Exit Prediction')
    st.sidebar.subheader('Enter Customer Details')
    
    # Input fields
    credit_score = st.sidebar.number_input("Credit Score", min_value=0)
    age = st.sidebar.number_input("Age", min_value=0)
    tenure = st.sidebar.number_input("Tenure (in years)", min_value=0)
    balance = st.sidebar.number_input("Account Balance", min_value=0.0)
    num_of_products = st.sidebar.number_input("Number of Products", min_value=0)
    has_credit_card = st.sidebar.selectbox("Has Credit Card", ["Yes", "No"])
    is_active_member = st.sidebar.selectbox("Is Active Member", ["Yes", "No"])
    estimated_salary = st.sidebar.number_input("Estimated Salary", min_value=0.0)
    geography = st.sidebar.selectbox("Geography", ["Germany", "Spain", "France"])
    gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
    
    # Map categorical variables
    if geography == "Germany":
        geography_germany, geography_spain, geography_france = 1, 0, 0
    elif geography == "Spain":
        geography_germany, geography_spain, geography_france = 0, 1, 0
    else:
        geography_germany, geography_spain, geography_france = 0, 0, 1
        
    gender = 1 if gender == "Male" else 0
    has_credit_card = 1 if has_credit_card == "Yes" else 0
    is_active_member = 1 if is_active_member == "Yes" else 0
    
    # Predict churn
    if st.sidebar.button('Predict'):
        try:
            prediction = model.predict([[credit_score, age, tenure, balance, 
                                         num_of_products, has_credit_card, is_active_member, 
                                         estimated_salary, geography_germany, 
                                         geography_spain, gender]])
            probability = model.predict_proba([[credit_score, age, tenure, balance, 
                                                num_of_products, has_credit_card, is_active_member, 
                                                estimated_salary, geography_germany, 
                                                geography_spain, gender]])[0][1]
            
            # Display prediction
            if prediction == 0:
                st.success(f'The customer is likely to stay. Exit probability: {probability:.2f}')
            else:
                st.warning(f'The customer is likely to exit. Exit probability: {probability:.2f}')
            
        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")

if __name__ == '__main__':
    main()
