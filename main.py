import streamlit as st
import pickle
import pandas as pd

# Load similarity matrix
with open('product_recommendation.pkl', 'rb') as f:
    similarity = pickle.load(f)

# Load product data
data = pd.read_csv("Final_Data_Fashion.csv")  # Ensure this file has a "Product_Name" column

# Limit the default dropdown options
default_options = ["Dress", "Shoes", "T-shirt", "Jeans", "Sweater"]

# Function to get top 3 similar products
def simi(product):
    if product not in data["Product_Name"].values:
        return ["⚠️ Product not found!"]
    
    product_index = data[data["Product_Name"] == product].index[0]
    product_simi = similarity[product_index]
    final_product = sorted(list(enumerate(product_simi)), reverse=True, key=lambda x: x[1])[1:4]
    
    return [data.iloc[i[0]].Product_Name for i in final_product]

# Streamlit UI
st.set_page_config(page_title="Amazing Product Recommender", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
        .big-font { font-size:30px !important; font-weight: bold; text-align: center; }
        .recommend-btn { background-color: #FF5733; color: white; font-size: 18px; border-radius: 10px; padding: 10px; width: 100%; }
        .recommend-btn:hover { background-color: #FF4500; }
        .result-box { background-color: #f4f4f4; padding: 15px; border-radius: 10px; text-align: center; font-size: 20px; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<p class="big-font">🛍️ Amazing Product Recommendation System 🛍️</p>', unsafe_allow_html=True)
st.write("Enter a product and get the **top 3 most similar recommendations** instantly!")

# User input with dropdown (showing limited default options)
product_name = st.selectbox("🔍 Select a product:", default_options, index=0)

# Recommend button
if st.button("✨ Recommend ✨", key="recommend", help="Click to get similar products"):
    recommendations = simi(product_name)
    st.subheader("🛍️ Top 3 Recommended Products:")
    for rec in recommendations:
        st.markdown(f'<p class="result-box">{rec}</p>', unsafe_allow_html=True)