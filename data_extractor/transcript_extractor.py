from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(video_id):
    ytt_api = YouTubeTranscriptApi()
    fetched_transcript =ytt_api.fetch(video_id)
    
    snippets = []
    for snippet in fetched_transcript:
        snippets.append(snippet.text)
        
    return snippets

if __name__ == "__main__":
    video_id = "x7X9w_GIm1s"
    print(get_transcript(video_id))