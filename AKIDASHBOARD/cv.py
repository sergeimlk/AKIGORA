import streamlit as st

# Set the page configuration to have a wide layout
st.set_page_config(layout="wide")

# Use a with statement to specify the sidebar or main page
with st.sidebar:
    # You can add a selectbox or other elements here if needed

# Use a with statement to specify the 👨‍💻CV & CANDIDATURE page
with st.container():
    st.header("👨‍💻CV & CANDIDATURE")
    st.image("CV.png", caption='CV de Sergei Milyukov', use_column_width=True)
