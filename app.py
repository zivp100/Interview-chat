import streamlit as st
import streamlit.components.v1 as components

st.title("Virtual behavioural interview")

# Embed the iframe from Chatbase
components.html(
    """
    <iframe
        src="https://www.chatbase.co/chatbot-iframe/s5El4QGPJw3wVIx5RRF-5"
        width="100%"
        style="height: 100%; min-height: 700px"
        frameborder="0"
    ></iframe>
    """,
    height=700,     # adjust the height to your liking
    scrolling=True  # allows scrolling within the iframe
)
