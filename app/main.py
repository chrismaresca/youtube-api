from fastapi import FastAPI, HTTPException
import logging
from datetime import datetime
from app.helpers import get_youtube_transcript

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="YouTube Transcript API",
    description="A simple API to fetch transcripts from YouTube videos"
)

@app.get("/")
async def root():
    """
    Root endpoint that provides basic API information
    
    Returns:
        dict: Basic information about the API
    """
    logger.info("Root endpoint accessed")
    return {
        "name": "YouTube Transcript API",
        "description": "Service for fetching transcripts from YouTube videos",
        "version": "0.1.0"
    }

@app.get("/health")
async def health_check():
    """
    Simple health check endpoint
    
    Returns:
        dict: Status message indicating the service is running
    """
    logger.info("Health check endpoint accessed")
    return {"status": "healthy"}

@app.get("/transcript")
async def get_transcript(url: str):
    """
    Get the transcript of a YouTube video
    
    Args:
        url (str): The YouTube video URL
        
    Returns:
        dict: Contains the transcript text
    """
    logger.info(f"Transcript requested for URL: {url}")
    try:
        transcript = get_youtube_transcript(url)
        logger.info("Transcript successfully retrieved")
        return {"transcript": transcript}
    except Exception as e:
        logger.error(f"Error retrieving transcript: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    logger.info("Starting application")
    uvicorn.run(app, host="0.0.0.0", port=8000) 