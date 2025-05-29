import streamlit as st
from transformers import pipeline

# Set Streamlit page configuration
st.set_page_config(page_title="Text Summarizer", layout="centered")

# Load the summarization pipeline
@st.cache_resource
def load_model():
    return pipeline("summarization", model="google-t5/t5-small")

summarizer = load_model()

# App Title
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>📝 Text Summarizer</h1>", unsafe_allow_html=True)
st.markdown("### Enter text below and get a summary instantly!")

# Text Input
input_text = st.text_area("Paste your text here:", height=250, placeholder="Type or paste any article, paragraph, or content...")

# Summarize Button
if st.button("Summarize"):
    if input_text.strip() == "":
        st.warning("Please enter some text to summarize.")
    else:
        with st.spinner("Generating summary..."):
            summary = summarizer(input_text, max_length=130, min_length=30, do_sample=False)[0]['summary_text']
        st.success("✅ Summary generated:")
        st.text_area("Summary", summary, height=200)

# Footer
st.markdown("<hr><p style='text-align: center;'>Built with 🤍 using Streamlit & Transformers</p>", unsafe_allow_html=True)
