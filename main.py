import streamlit as st
from PyPDF2 import PdfReader
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
import pandas as pd
import io

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_file):
    text = ""
    pdf_reader = PdfReader(pdf_file)
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

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

# Function to generate and display a word cloud with color theme options
def generate_word_cloud(text, num_words=200, color_theme="Color", most_used=True, custom_font=None, width=800, height=400):
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

    # Create a WordCloud instance with the specified settings, including width and height
    wordcloud = WordCloud(width=width, height=height, background_color='white',
                          colormap=colormap,
                          collocations=False,  # Disable collocations to emphasize word frequency
                          max_words=num_words,
                          font_path=custom_font).generate_from_frequencies(wordcloud_data)

    return wordcloud  # Return the WordCloud object


import streamlit as st
from PyPDF2 import PdfReader
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
import pandas as pd
import io

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_file):
    text = ""
    pdf_reader = PdfReader(pdf_file)
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

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

# Function to generate and display a word cloud with color theme options
def generate_word_cloud(text, num_words=200, color_theme="Color", most_used=True, custom_font=None, width=800, height=400):
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

    # Create a WordCloud instance with the specified settings, including width and height
    wordcloud = WordCloud(width=width, height=height, background_color='white',
                          colormap=colormap,
                          collocations=False,  # Disable collocations to emphasize word frequency
                          max_words=num_words,
                          font_path=custom_font).generate_from_frequencies(wordcloud_data)

    return wordcloud  # Return the WordCloud object

def main():
    st.title("PDF to Word-Cloud Generator")
    st.write("Upload a PDF file, and I'll generate a word-cloud and display word details from its content.")

    # Upload PDF file
    uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])

    st.sidebar.subheader(" PDF to Word-Cloud Generator (V 1.5) ")
    
    # Sidebar options
    st.sidebar.subheader("Options")
    
    # Dropdown select box for color theme
    color_theme = st.sidebar.selectbox("Select Color Theme:", ("Color", "Mono-Chrome", "Pastel", "Cool", "Warm"))

    # Radio button to select most used or least used words
    display_most_used = st.sidebar.radio("Select Words to Display:", ("Most Used Words", "Least Used Words"), index=0)

    # File uploader for custom font
    custom_font = st.sidebar.file_uploader("Upload Custom Font (TTF file)", type=["ttf"])

    # Select box for image size
    image_size = st.sidebar.selectbox("Select Image Size:", ("Small", "Medium", "Large"))

    # Select box for image format
    image_format = st.sidebar.selectbox("Select Image Format:", ("JPEG", "PNG", "SVG"))


    # Define image width and height based on user selection
    if image_size == "Small":
        width, height = 400, 200
    elif image_size == "Medium":
        width, height = 600, 300
    else:
        width, height = 800, 400

    if uploaded_file is not None:
        # Read and extract text from the PDF
        pdf_text = extract_text_from_pdf(uploaded_file)

        # Determine whether to display most used or least used words
        most_used = display_most_used == "Most Used Words"

        # Display word cloud with color theme option and custom font
        st.write(f"Word-Cloud of the {display_most_used} from the PDF:")

        if custom_font:
            custom_font_name = custom_font.name  # Get the uploaded font file name
            custom_font_path = f"./{custom_font_name}"  # Create a temporary path using the file name

            # Save the uploaded font file with its original name
            with open(custom_font_path, "wb") as f:
                f.write(custom_font.read())

            try:
                wordcloud = generate_word_cloud(pdf_text, color_theme=color_theme, most_used=most_used,
                                                custom_font=custom_font_path, width=width, height=height)

                # Display the Word-Cloud image
                st.image(wordcloud.to_array(), use_column_width=False, width=width, caption="Word-Cloud")
            except Exception as e:
                st.error(f"An error occurred while generating the Word-Cloud: {str(e)}")
        else:
            # st.error("Please upload a custom font to proceed.")
            
            wordcloud = generate_word_cloud(pdf_text, num_words=200, color_theme=color_theme, most_used=most_used)
            # Display the Word-Cloud image
            st.image(wordcloud.to_array(), use_column_width=False, width=width, caption="Word-Cloud")

        # Allow user to download the Word-Cloud image
        if st.button("Download Word-Cloud"):
            if image_format == "JPEG":
                image_data = wordcloud.to_array()
                image = Image.fromarray(image_data)
                img_buffer = io.BytesIO()
                image.save(img_buffer, format="JPEG")
                st.download_button("Download JPEG", img_buffer, key="wordcloud.jpg", mime="image/jpeg")
            elif image_format == "PNG":
                image_data = wordcloud.to_image()
                img_buffer = io.BytesIO()
                image_data.save(img_buffer, format="PNG")
                st.download_button("Download PNG", img_buffer, key="wordcloud.png", mime="image/png")
            elif image_format == "SVG":
                svg_data = wordcloud.to_svg()
                st.download_button("Download SVG", svg_data, key="wordcloud.svg", mime="image/svg+xml")

        # Display word details in a table
        display_word_details(pdf_text, most_used=most_used)

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
