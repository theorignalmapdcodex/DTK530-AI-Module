import os
import streamlit as st

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

LLM_OUTPUT_LENGTH_SIZE = 1024

STREAMLIT_HOMEPAGE_CONTENT = """
<style>
.stApp {
    background-color: #dec3e6;
}
.reportview-container .markdown-text-container {
    color: #ffffff;
}
.reportview-container .css-1d391kg {
    color: #ffffff;
}
h1, h2, h3, h4, h5, h6 {
    color: #ffffff;
    font-weight: bold;
}
.stButton>button {
    color: #ffffff;
    background-color: #4caf50;
}
.stFileUploader .css-1m6mopr {
    color: #ffffff;
    background-color: #4caf50;
}
</style>
"""

POEM_INSTRUCTIONS_PROMPT = """
Based on the image of an item provided by the user, which represents a product they wish to write a poem on, 
please analyze the item and generate four lines of poem that describes the item in a creative and engaging way.
The poem should be written in a way that is suitable for a greeting card or a social media post.
"""