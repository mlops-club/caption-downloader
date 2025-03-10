import yt_dlp
import json
import os

def download_captions(video_url, output_dir='captions'):
    """
    Download English captions from a YouTube video
    
    Args:
        video_url: URL of the YouTube video
        output_dir: Directory to save the captions
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Configure yt-dlp options
    ydl_opts = {
        'skip_download': True,  # Skip downloading the video
        'writesubtitles': True,  # Enable subtitle downloading
        'writeautomaticsub': True,  # Enable automatic subtitle downloading
        'subtitleslangs': ['en'],  # Download only English subtitles
        'subtitlesformat': 'vtt',  # VTT format for subtitles
        'outtmpl': os.path.join(output_dir, '%(id)s.%(ext)s'),  # Output template
        'quiet': False,  # Show progress
    }
    
    # Download the captions
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(video_url, download=True)
        print(f"Downloaded captions for: {info.get('title', 'Unknown title')}")
        
        # Return the path to the downloaded caption file
        video_id = info.get('id', 'unknown')
        caption_path = os.path.join(output_dir, f"{video_id}.en.vtt")
        
        if os.path.exists(caption_path):
            print(f"Caption file saved to: {caption_path}")
            return caption_path
        else:
            print("No English captions were found or downloaded.")
            return None

if __name__ == "__main__":
    video_url = "https://www.youtube.com/watch?v=UIVADiGfwWc"
    download_captions(video_url)

