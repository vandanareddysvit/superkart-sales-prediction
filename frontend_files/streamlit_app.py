import streamlit as st
import pandas as pd
import requests
import json

# --- Configuration ---
# The URL for your Flask API endpoint for single predictions
# You will need to update this with your actual Codespace forwarded URL + /v1/predict
# Example: 'https://organic-space-abcd1234-7860.app.github.dev/v1/predict'
FLASK_API_URL = "http://superkart_backend:5000/v1/predict" # This URL is for Docker network communication

st.set_page_config(page_title="SuperKart Sales Predictor", layout="centered")
st.title("SuperKart Sales Prediction")
st.markdown("Enter the product and store details to predict total sales.")

# --- Input Form ---
st.header("Product and Store Details")

with st.form("prediction_form"):
    product_weight = st.number_input("Product Weight (kg)", min_value=0.1, max_value=25.0, value=12.66, step=0.01)
    product_sugar_content = st.selectbox("Product Sugar Content", ['Low Sugar', 'Regular', 'No Sugar'], index=0)
    product_allocated_area = st.number_input("Product Allocated Area Ratio", min_value=0.0, max_value=1.0, value=0.027, step=0.001)
    product_mrp = st.number_input("Product MRP (INR)", min_value=10.0, max_value=300.0, value=117.08, step=0.01)
    store_size = st.selectbox("Store Size", ['Small', 'Medium', 'High'], index=1)
    store_location_city_type = st.selectbox("Store Location City Type", ['Tier 1', 'Tier 2', 'Tier 3'], index=1)
    store_type = st.selectbox("Store Type", ['Supermarket Type1', 'Supermarket Type2', 'Departmental Store', 'Food Mart'], index=1)
    product_id_char = st.selectbox("Product ID Character (First two letters)", ['FD', 'NC', 'DR', 'HC', 'FR', 'SN', 'DI', 'CR', 'SE'], index=0)
    store_age_years = st.number_input("Store Age (Years)", min_value=0, max_value=30, value=16, step=1)
    product_type_category = st.selectbox("Product Type Category", ['Perishables', 'Drinks', 'Non Perishables'], index=2)

    submitted = st.form_submit_button("Predict Sales")

    if submitted:
        # Prepare the payload for the Flask API
        payload = {
            "Product_Weight": product_weight,
            "Product_Sugar_Content": product_sugar_content,
            "Product_Allocated_Area": product_allocated_area,
            "Product_MRP": product_mrp,
            "Store_Size": store_size,
            "Store_Location_City_Type": store_location_city_type,
            "Store_Type": store_type,
            "Product_Id_char": product_id_char,
            "Store_Age_Years": store_age_years,
            "Product_Type_Category": product_type_category
        }

        st.write("Sending request to backend...")
        try:
            response = requests.post(FLASK_API_URL, json=payload)

            if response.status_code == 200:
                prediction = response.json().get("prediction")
                st.success(f"Predicted Product Store Sales Total: **₹{prediction:,.2f}**")
            else:
                error_message = response.json().get("error", "Unknown error")
                st.error(f"Error from API: {error_message} (Status Code: {response.status_code})")
                st.write(response.text)
        except requests.exceptions.ConnectionError as e:
            st.error(f"Could not connect to the backend API. Please ensure the Flask app is running. Error: {e}")
        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")


st.markdown("--- Request Payload ---")
st.json(payload if 'payload' in locals() else {})

