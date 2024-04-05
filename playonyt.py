# playonyt.py
import sys

import yt_dlp
import webbrowser




def play_youtube_song(query):
    # Prompt the user to enter the song they want to play on YouTube
    
    # Search for the song on YouTube using yt_dlp with the --quiet option
    ydl_opts = {'quiet': True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        search_results = ydl.extract_info(f"ytsearch:{query}", download=False)
    
    # Open the first video in the default web browser
    if 'entries' in search_results:
        first_video = search_results['entries'][0]
        video_url = first_video['webpage_url']
        webbrowser.open(video_url)
    else:
        print(f"No search results found for the song: {query}")

# Main function for executing the task directly
def main():
    play_youtube_song()

# If the module is run directly, execute the main function
if __name__ == "__main__":
    main()
