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


# Function to generate and display a word cloud with color theme options
def generate_word_cloud(text, num_words=200, color_theme="Color", most_used=True, custom_font=None):
    # Tokenize the text into words
    words = text.split()

    # Calculate word frequencies
    word_counter = Counter(words)

    # Get the most common or least common words and their frequencies
    if most_used:
        word_data = word_counter.most_common(num_words)
    else:
        word_data = word_counter.most_common()[-num_words:]

    # Create a dictionary of the selected words
    wordcloud_data = dict(word_data)

    # Define the colormap based on the selected color theme
    colormap = 'viridis'  # Default to a color theme

    if color_theme == "Mono-Chrome":
        colormap = 'gray'  # Monochrome theme
    elif color_theme == "Pastel":
        colormap = 'Pastel1'  # Pastel theme
    elif color_theme == "Cool":
        colormap = 'cool'  # Cool theme
    elif color_theme == "Warm":
        colormap = 'autumn'  # Warm theme

    # Create a WordCloud instance with the specified settings
    wordcloud = WordCloud(width=800, height=400, background_color='white',
                          colormap=colormap,
                          collocations=False,  # Disable collocations to emphasize word frequency
                          max_words=num_words,
                          font_path=custom_font).generate_from_frequencies(wordcloud_data)
    
    st.image(wordcloud.to_array(), use_column_width=True)

# Function to display word details in a table with most frequent or least frequent words at the top
def display_word_details(text, most_used=True, num_words=200):
    word_list = text.split()
    word_counter = Counter(word_list)
    
    # Sort the word frequency dictionary by frequency in ascending or descending order
    if most_used:
        sorted_word_counter = dict(sorted(word_counter.items(), key=lambda item: item[1], reverse=True))
    else:
        sorted_word_counter = dict(sorted(word_counter.items(), key=lambda item: item[1]))
    
    data = {'S.No': [], 'Word': [], 'Frequency': []}
    
    # Initialize a counter for the serial number
    serial_number = 1
    
    # Get the most common or least common words and their frequencies
    if most_used:
        word_data = list(sorted_word_counter.items())[:num_words]
    else:
        word_data = list(sorted_word_counter.items())[-num_words:]
    
    for word, freq in word_data:
        data['Word'].append(word)
        data['Frequency'].append(freq)
        
        # Add the serial number to the DataFrame
        data['S.No'].append(serial_number)
        
        # Increment the serial number
        serial_number += 1

    df = pd.DataFrame(data)
    
    st.subheader(f"Details of Words ({'Most Used' if most_used else 'Least Used'})")
    st.write(df.set_index('S.No'))  # Set 'S.No' as the index


def main():
    st.title("PDF to Word Cloud Generator")
    st.write("Upload a PDF file, and I'll generate a word cloud and display word details from its content.")

    # Upload PDF file
    uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])

    # Dropdown select box for color theme
    color_theme = st.selectbox("Select Color Theme:", ("Color", "Mono-Chrome", "Pastel", "Cool", "Warm"))

    # # Radio button to select most used or least used words
    display_most_used = st.radio("Select Words to Display:", ("Most Used Words", "Least Used Words"), index=0)

    # File uploader for custom font
    custom_font = st.file_uploader("Upload Custom Font (TTF file)", type=["ttf"])

    if uploaded_file is not None:
        # Read and extract text from the PDF
        pdf_text = extract_text_from_pdf(uploaded_file)

        # Determine whether to display most used or least used words
        most_used = display_most_used == "Most Used Words"

        # Display word cloud with color theme option and custom font
        st.write(f"Word Cloud of the {display_most_used} from the PDF:")
        
        if custom_font:
            custom_font_name = custom_font.name  # Get the uploaded font file name
            custom_font_path = f"./{custom_font_name}"  # Create a temporary path using the file name
            
            # Save the uploaded font file with its original name
            with open(custom_font_path, "wb") as f:
                f.write(custom_font.read())
            
            try:
                generate_word_cloud(pdf_text, num_words=200, color_theme=color_theme, most_used=most_used, custom_font=custom_font_path)
            except Exception as e:
                st.error(f"An error occurred while generating the Word Cloud: {str(e)}")
        else:
            generate_word_cloud(pdf_text, num_words=200, color_theme=color_theme, most_used=most_used)

        # Display word details in a table
        display_word_details(pdf_text, most_used=most_used, num_words=200)
        
    # Write linkedin and other credentials on the sidebar footer
    # Include sidebar with credentials
    with st.sidebar:
        # st.markdown('Chat With DIDX.net (V 0.1)')
        st.markdown("""
                    #### PDF to Word Cloud Generator (V 1.5) 
                    #### Let's connect: [Kamran Feroz](https://www.linkedin.com/in/kamranferoz/)
                    """)
    st.markdown(
        "<style>#MainMenu{visibility:hidden;}</style>",
        unsafe_allow_html=True)        
        
if __name__ == "__main__":
    main()
