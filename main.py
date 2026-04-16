from ai.pipeline import run_pipeline
from data_extractor.transcript_extractor import get_transcript

video = "https://www.youtube.com/watch?v=x7X9w_GIm1s"
video_id = video.split("v=")[-1]

transcript = get_transcript(video_id)
result = run_pipeline("What is the topic of this video?", transcript, "llama-3.3-70b-versatile")
print(result)