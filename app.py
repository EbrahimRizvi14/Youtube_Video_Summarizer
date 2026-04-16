from dotenv import load_dotenv
import streamlit as st
from ai.pipeline import run_pipeline
from data_extractor.transcript_extractor import get_transcript

st.set_page_config(page_title="YouTube Video Summarizer", page_icon="📺", layout="wide")

load_dotenv()

st.sidebar.title("Settings ⚙️")
video_url = st.sidebar.text_input("Enter YouTube Video URL: ")
model = st.sidebar.selectbox("Select Language Model", ["llama-3.3-70b-versatile", "meta-llama/llama-4-scout-17b-16e-instruct", "groq/compound", ])


if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello, how can I help you with this video?"}
    ]

if video_url:
    video_id = video_url.split("v=")[-1]
    transcript = get_transcript(video_id)
    fake_transcript = [
    "So in this video we're basically talking about how you can use AI to summarize YouTube videos.",
    "First, you get the transcript and then you clean it up because there's a lot of filler words.",
    "Stuff like 'uh' and unnecessary pauses are removed to make the text clearer.",
    "Then we send it into a language model which understands the main points and gives a summary.",
    "You can also ask questions about the video, which is actually really useful.",
    "We built a small app using Streamlit where you just paste a YouTube link.",
    "The app processes everything and gives you summaries and answers in real time.",
    "Overall, it's a simple but powerful way to understand long videos quickly."
]
    if transcript:

        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        question = st.chat_input("Ask a question about the video content:")

        if question:
            st.session_state.messages.append({"role": "user", "content": question})

            result = run_pipeline(question, transcript, model)

            st.session_state.messages.append({"role": "assistant", "content": result})

            st.rerun()

    else:
        st.error("Could not fetch transcript for the provided video URL.")
else:
    st.info("Please enter a YouTube video URL in the sidebar to get started.")