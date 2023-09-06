import streamlit as st
from PyPDF2 import PdfReader
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
import pandas as pd

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_file):
    text = ""
    pdf_reader = PdfReader(pdf_file)
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

# Function to generate and display the word cloud
def generate_word_cloud(text):
    # Specify a path to a system font (change this path to a font file on your system)
    custom_font_path = "font.ttf"  # Replace with the path to your font file
    
    wordcloud = WordCloud(width=800, height=400, background_color='white', font_path=custom_font_path).generate(text)
    st.image(wordcloud.to_image(), use_column_width=True)
    plt.close()  # Close the Matplotlib figure

# Function to display word details in a table
def display_word_details(text):
    word_list = text.split()
    word_counter = Counter(word_list)
    
    data = {'Word': [], 'Frequency': []}
    for word, freq in word_counter.items():
        data['Word'].append(word)
        data['Frequency'].append(freq)

    df = pd.DataFrame(data)
    
    st.subheader("Details of Words")
    st.write(df)
        
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
        
        # Display word details
        display_word_details(pdf_text)

    # Write linkedin and other credentials on the sidebar footer
    # Include sidebar with credentials
    with st.sidebar:
        # st.markdown('Chat With DIDX.net (V 0.1)')
        st.markdown(""" 
                    #### Let's connect: [Kamran Feroz](https://www.linkedin.com/in/kamranferoz/)
                    """)
    st.markdown(
        "<style>#MainMenu{visibility:hidden;}</style>",
        unsafe_allow_html=True)
    
if __name__ == "__main__":
    main()
