import streamlit as st
import pandas as pd
import joblib

model = joblib.load("House_Rent_Prediction.pkl")

st.title( "House Rent Prediction")

bhk = st.selectbox("BHK", [1, 2, 3, 4, 5, 6])

size = st.number_input(
    "Size (sq ft)",
    min_value=100,
    max_value=10000,
    value=1000
)

bathroom = st.selectbox("Bathroom", [1, 2, 3, 4, 5, 6])

area_type = st.selectbox(
    "Area Type",
    ["Carpet Area", "Super Area"]
)

city = st.selectbox(
    "City",
    ["Chennai", "Delhi", "Hyderabad", "Kolkata", "Mumbai"]
)

furnishing = st.selectbox(
    "Furnishing Status",
    ["Furnished", "Semi-Furnished", "Unfurnished"]
)

tenant = st.selectbox(
    "Tenant Preferred",
    ["Bachelors", "Bachelors/Family", "Family"]
)

contact = st.selectbox(
    "Point of Contact",
    ["Contact Agent", "Contact Builder", "Contact Owner"]
)

if st.button("Predict Rent"):

    data = {
        'BHK': [bhk],
        'Size': [size],
        'Bathroom': [bathroom],

        'Area Type_Carpet Area': [1 if area_type == "Carpet Area" else 0],
        'Area Type_Super Area': [1 if area_type == "Super Area" else 0],

        'City_Chennai': [1 if city == "Chennai" else 0],
        'City_Delhi': [1 if city == "Delhi" else 0],
        'City_Hyderabad': [1 if city == "Hyderabad" else 0],
        'City_Kolkata': [1 if city == "Kolkata" else 0],
        'City_Mumbai': [1 if city == "Mumbai" else 0],

        'Furnishing Status_Semi-Furnished': [1 if furnishing == "Semi-Furnished" else 0],
        'Furnishing Status_Unfurnished': [1 if furnishing == "Unfurnished" else 0],

        'Tenant Preferred_Bachelors/Family': [1 if tenant == "Bachelors/Family" else 0],
        'Tenant Preferred_Family': [1 if tenant == "Family" else 0],

        'Point of Contact_Contact Builder': [1 if contact == "Contact Builder" else 0],
        'Point of Contact_Contact Owner': [1 if contact == "Contact Owner" else 0]
    }

    input_df = pd.DataFrame(data)

    prediction = model.predict(input_df)

    st.success(f"🏠 Predicted Rent: ₹{prediction[0]:,.0f} per month")

    st.info("⚠️ This prediction is based on historical rental data and may vary from actual market prices.")