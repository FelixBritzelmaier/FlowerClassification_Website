import streamlit as st
from labels import labels

st.title("📗 Flower Classes")
st.markdown("<h2 style=\"color:green;\">How many flowers can I search for ?</h2>", unsafe_allow_html=True)
st.markdown("Our model can classify **102** different classes of flowers. Including :")
colones = st.columns(3)
for i,label in enumerate(labels):
    col = colones[i % 3]
    col.markdown(f"<p><b style=\"color:green;\">•   </b>{labels[label]}</p>", unsafe_allow_html=True)