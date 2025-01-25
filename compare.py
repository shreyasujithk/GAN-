import streamlit as st
from PIL import Image

# Title of the app
st.title("GAN Comparison: STACKGAN vs ATTNGAN (100 Epochs)")

# Load images
stagan_image = Image.open("C:/Users/shrey/Major Project/final/2.jpg")  # Replace with the actual path
attgan_image = Image.open("C:/Users/shrey/Major Project/final/1.jpg")  # Replace with the actual path

# Layout: Side-by-side image display
st.header("Comparison at 100 Epochs")
def compare():
    pass
col1, col2 = st.columns(2)

with col1:
    st.subheader("STACKGAN Result")
    st.image(stagan_image, caption="STACKGAN (100 Epochs)", use_column_width=True)

with col2:
    st.subheader("ATTNGAN Result")
    st.image(attgan_image, caption="ATTNGAN (100 Epochs)", use_column_width=True)


