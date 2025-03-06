import streamlit as st
from query_data import query_rag

st.title("📄 PDF Chatbot")
st.write("Ask any question from your uploaded documents!")

query = st.text_input("Ask a question:")

if st.button("Ask"):
    if query:
        with st.spinner("Thinking...🤔"):
            response = query_rag(query)
            st.success("✅ Done!")
            st.write("💡 Answer:", response)
    else:
        st.warning("Please enter a question!")
