from ai import pipeline
from data_extractor import extract_transcript

video = "https://www.youtube.com/watch?v=x7X9w_GIm1s"
video_id = video.split("v=")[-1]

transcript = extract_transcript.get_transcript(video_id)
result = pipeline.run_pipeline(transcript, '''What is the topic of this video?''')
print(result)