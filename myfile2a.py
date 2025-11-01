import pickle
import streamlit as st

# Load the trained model
model1 = pickle.load(open("areapricebedage.pkl", "rb"))

# Page configuration
st.set_page_config(page_title="🏡 House Price Predictor", page_icon="💰", layout="centered")

# Custom CSS for better visuals
st.markdown("""
    <style>
        .main {
            background-color: #f0f6ff;
            padding: 2rem;
            border-radius: 10px;
        }
        h1 {
            color: #004aad;
            text-align: center;
            font-family: 'Arial Black', sans-serif;
        }
        .stButton>button {
            background-color: #004aad;
            color: white;
            font-size: 18px;
            border-radius: 8px;
            padding: 10px 24px;
        }
        .stButton>button:hover {
            background-color: #0077ff;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# App function
def mydeploy():
    st.markdown("<div class='main'>", unsafe_allow_html=True)
    st.title("🏠 House Price Prediction App")

    st.write("### Enter the property details below to estimate the price:")

    # Inputs in columns for better layout
    col1, col2, col3 = st.columns(3)
    with col1:
        a = st.number_input("📐 Area (in sq. ft.)", min_value=100.0, step=50.0)
    with col2:
        b = st.number_input("🛏️ Number of Bedrooms", min_value=1, step=1)
    with col3:
        age = st.number_input("🏗️ Age of Property (years)", min_value=0, step=1)

    # Predict button
    pred = st.button("🔍 Predict Price")

    if pred:
        x = model1.predict([[a, b, age]])
        st.success(f"💰 **Estimated Price:** ₹ {x[0]:,.2f}")
        st.balloons()

    st.markdown("</div>", unsafe_allow_html=True)

# Run app
mydeploy()
