from groq import Groq
import os
from dotenv import load_dotenv
from ai import config


load_dotenv()

def run_pipeline(message, transcript, model):
    client = Groq(
    api_key=os.getenv("GROQ_API_KEY"),
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f'Question: {message}\n\nSystem Prompt: {config.prompt}\n\n{" ".join(transcript)}',
            }
        ],
        model=model,
    )

    return chat_completion.choices[0].message.content

if __name__ == "__main__":
    result = run_pipeline('''What is the topic of this video?''', '''This is a sample transcript of a YouTube video. It contains various sentences that may be relevant to the video's content. The transcript may also include timestamps and other metadata that can be noisy or incomplete. The AI assistant will use this transcript to summarize the video and answer questions based on the provided context.''', "llama-3.3-70b-versatile")
    print(result)