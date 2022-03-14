# https://es.acervolima.com/2021/02/09/una-guia-para-principiantes-de-streamlit/
import streamlit as st 

st.markdown( """ <style> .reportview-container { background: 
    }
   .sidebar .sidebar-content { background: url("https://images.app.goo.gl/LFCobouKtT7oZ7Qv7")
    }
    </style> """, unsafe_allow_html=True )
  
st.title("Hello GeeksForGeeks !!!") 
st.header("This is a header")
  
st.subheader("This is a subheader") 
st.text("Hello GeeksForGeeks!!!") 
st.markdown("### This is a markdown") 
  
st.info("Information")
  
st.warning("Warning")
  
st.error("Error") 
st.write("Text with write")
  
st.write(range(10)) 

