import yt_dlp

def youtube_downloader(url):
    # Configure options (downloads the best quality with audio)
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',  # Ensures MP4 output
        'merge_output_format': 'mp4',  # Merge audio/video if needed
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        print("Download complete!")

def instavid_downloader(url):
    ydl_opts = {
        'format': 'best',  # Best quality
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print("Done!")

def x_downloader(url):
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',  # Best quality
        'outtmpl': '%(title)s.%(ext)s',  # Filename
        # Twitter often blocks scrapers, so mimic a browser:
        'headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
        }
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print("Downloaded!")

def others(url):
    ydl_opts = {
    'format': 'bestvideo+bestaudio/best',  # Best quality
    'merge_output_format': 'mp4',          # Merge audio/video if needed
    'outtmpl': '%(title)s.%(ext)s',        # Output filename
    'noplaylist': True,                    # Download single video, not playlists
    'quiet': True,                         # Hide verbose logs
    # Mimic a browser to avoid blocking:
    'headers': {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
    }
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download complete!")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":

    print("From which platform you want to download.\nEnter your options number:")
    print("1. Youtube\n2. Instagram\n3. X\n4. Others")
    option = int(input("Option: "))
    
    if option == 1:
        url = input("Enter the url: ")
        youtube_downloader(url)

    elif option == 2:
        url = input("Enter the url: ")
        instavid_downloader(url)

    elif option == 3:
        url = input("Enter the url: ")
        x_downloader(url)
        
    elif option == 4:
        url = input("Enter the url: ")
        others(url)


    