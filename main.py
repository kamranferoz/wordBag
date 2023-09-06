import streamlit as st
from PyPDF2 import PdfReader
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_file):
    text = ""
    pdf_reader = PdfReader(pdf_file)
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

# Function to generate and display the word cloud
def generate_word_cloud(text):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    st.image(wordcloud.to_image(), use_column_width=True)
    plt.close()  # Close the Matplotlib figure

def main():
    st.title("PDF to Word Cloud Generator")
    st.write("Upload a PDF file, and I'll generate a word cloud from its content.")

    # Upload PDF file
    uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])

    if uploaded_file is not None:
        # Read and extract text from the PDF
        pdf_text = extract_text_from_pdf(uploaded_file)

        # Display word cloud
        st.write("Word Cloud generated from the PDF:")
        generate_word_cloud(pdf_text)

if __name__ == "__main__":
    main()
