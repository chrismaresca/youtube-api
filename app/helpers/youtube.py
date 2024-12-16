from youtube_transcript_api import YouTubeTranscriptApi
import re

def get_video_id(youtube_url):
    """
    Extract video ID from a YouTube URL.
    
    Args:
        youtube_url (str): URL of the YouTube video
        
    Returns:
        str: The video ID extracted from the URL
        
    Raises:
        ValueError: If the URL is invalid or video ID cannot be extracted
    """
    # Extract the video ID from the YouTube URL
    video_id_match = re.search(r'(?<=v=)[^&#]+|(?<=be/)[^&#]+', youtube_url)
    if video_id_match:
        return video_id_match.group(0)
    else:
        raise ValueError("Invalid YouTube URL. Please provide a valid link.")

def get_youtube_transcript(video_url):
    """
    Fetch and return the transcript of a YouTube video.
    
    Args:
        video_url (str): URL of the YouTube video
        
    Returns:
        str: Full transcript text of the video, or error message if failed
    """
    try:
        # Get video ID from the URL
        video_id = get_video_id(video_url)
        
        # Fetch the transcript using YouTubeTranscriptApi
        transcript = YouTubeTranscriptApi.get_transcript(video_id)

        # Concatenate all the text parts into a single string
        full_transcript = " ".join([entry['text'] for entry in transcript])
        return full_transcript

    except Exception as e:
        return f"An error occurred: {str(e)}"