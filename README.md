Documentation for Bank Customer Churn Prediction App:

---

## Overview:
This Streamlit web application predicts the likelihood of bank customers churning based on various input features such as credit score, age, tenure, account balance, and more. The prediction is made using a pre-trained machine learning model loaded into the application.

## Usage:
1. **Model Loading:**
   - Upon initialization, the application attempts to load the pre-trained machine learning model (`churn_predict_model`) using the `joblib` library. If the model file is not found or if there is an error loading the model, appropriate error messages are displayed.

2. **User Interface:**
   - The application provides a user-friendly interface for entering customer details via a sidebar.
   - The user inputs various attributes of the bank customer, including credit score, age, tenure, account balance, number of products, credit card status, active membership, estimated salary, geography, and gender.

3. **Prediction:**
   - After entering the customer details, the user can click the "Predict" button to generate the churn prediction.
   - The application handles the prediction process and displays the prediction outcome along with the churn probability.
   - If the prediction is successful, the application displays whether the customer is likely to stay or churn, along with the churn probability.

4. **Categorical Variable Mapping:**
   - The application maps categorical variables such as geography and gender to binary variables for model input. 
   - Geography is mapped to three binary variables (`geography_germany`, `geography_spain`, `geography_france`) based on the selected country.
   - Gender is mapped to a binary variable (`gender`) where 1 represents "Male" and 0 represents "Female".
   - Credit card status and active membership are also mapped to binary variables.

5. **Error Handling:**
   - The application includes error handling mechanisms to catch and display any exceptions that occur during the prediction process.
   - Error messages are displayed to the user in case of invalid inputs or errors encountered during prediction.

## Requirements:
- Python 3.x
- Streamlit
- joblib
- scikit-learn

## Installation:
1. Install Streamlit using pip:
   ```
   pip install streamlit
   ```
2. Install joblib using pip:
   ```
   pip install joblib
   ```

## Running the Application:
1. Save the provided code in a Python file (e.g., `churn_prediction_app.py`).
2. Place the pre-trained model file (`churn_predict_model`) in the same directory as the Python file.
3. Open a terminal or command prompt and navigate to the directory containing the Python file.
4. Run the Streamlit application using the following command:
   ```
   streamlit run churn_prediction_app.py
   ```

---

This documentation provides an overview of the Bank Customer Churn Prediction application, its usage, requirements, installation instructions, and running instructions. It serves as a guide for users and developers interested in utilizing or contributing to the application.