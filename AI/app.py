import os
import streamlit as st
import google.generativeai as genai

from PIL import Image

# Local
from constants import *
from util import *


def __get_gemini_client__() -> genai.GenerativeModel:
    genai.configure(api_key=GEMINI_API_KEY)
    gemini_model = genai.GenerativeModel("gemini-1.5-flash")
    return gemini_model

def main():
    gemini_model = __get_gemini_client__()

    # Streamlit app interface customization
    st.markdown(
        STREAMLIT_HOMEPAGE_CONTENT,
        unsafe_allow_html=True
    )

    st.title('Image Describer')
    st.header('Describe your image like a poem!')
    st.write('Upload an image of the item you wish to write a poem on, and we\'ll tell you how!')

    uploaded_image = st.file_uploader(
        "",
        type=["png", "jpg", "jpeg"],
    )

    if uploaded_image is not None:
        # Display a progress bar
        image = Image.open(uploaded_image)
        user_uploaded_image = image.copy()
        file_ext = str(uploaded_image.name.split(".")[-1]).lower().strip()
        print(file_ext)

        # Get image size in MB using os.stat
        image = image.resize((image.width // 2, image.height // 2))
        # Redice image quality
        compressed_image_name = f"temp.{file_ext}"

        image.save(
            compressed_image_name,
            "JPEG" if file_ext == "jpg" else file_ext.upper(),
            quality=25,
            optimize=True,
            progressive=True
        )
        image = Image.open(compressed_image_name)
        
        # Print image size
        image_size = os.stat(compressed_image_name).st_size / (1024 * 1024)
        print(f"Compressed image size: {image_size} MB")

        if image_size > 3.9:
            st.error("Please upload an image less than 15MB.")
            return
        
        st.image(user_uploaded_image, caption='Your Uploaded Image', use_column_width=True)

        # Get poem instructions
        instructions = get_poem_from_image(image, gemini_model)
        if instructions:
            st.subheader("The poem:")
            st.markdown(instructions, unsafe_allow_html=True)
        else:
            st.error("Could not get instructions for generating the poem")

        # Delete compressed_image_name file
        os.remove(compressed_image_name)
    

if __name__ == "__main__":
    main()
    # Run the app with the command streamlit run app.py in the terminal