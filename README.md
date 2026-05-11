# YouTube Video Summarizer

A Streamlit app that lets you paste a YouTube video URL, fetches the video's transcript, and uses a Groq-hosted language model to answer questions or summarize the video content.

## Features

- Paste a YouTube video URL in the sidebar
- Fetch transcript text with `youtube-transcript-api`
- Ask questions about the video through a chat interface
- Choose between supported Groq language models
- Keep answers grounded in the transcript context

## Project Structure

```text
.
├── app.py
├── main.py
├── ai
│   ├── config.py
│   └── pipeline.py
└── data_extractor
    └── transcript_extractor.py
```

- `app.py` - Streamlit web app entry point.
- `main.py` - Simple command-line test script.
- `ai/config.py` - Prompt instructions for the assistant.
- `ai/pipeline.py` - Groq API call logic.
- `data_extractor/transcript_extractor.py` - YouTube transcript extraction.

## Requirements

- Python 3.10 or newer recommended
- A Groq API key
- A YouTube video with an available transcript

Install the required Python packages:

```bash
pip install streamlit python-dotenv groq youtube-transcript-api
```

## Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

The `.env` file is ignored by git, so your API key should not be committed.

## Run the App

Start the Streamlit app:

```bash
streamlit run app.py
```

Then open the local URL shown in your terminal, usually:

```text
http://localhost:8501
```

## Usage

1. Paste a YouTube video URL in the sidebar.
2. Select a language model.
3. Wait for the transcript to load.
4. Ask a question such as:
   - `Summarize this video.`
   - `What are the main points?`
   - `What does the speaker say about AI?`

## Notes

- The app currently extracts the video ID using `video_url.split("v=")[-1]`, so standard YouTube watch URLs work best.
- Videos without transcripts, private videos, or region-restricted videos may fail to load.
- The assistant is instructed to answer only from transcript context and avoid using outside knowledge.

## Optional Improvements

- Support more YouTube URL formats, such as `youtu.be/...` links.
- Add transcript caching to avoid repeated API calls.
- Add clearer error handling for unavailable transcripts.
