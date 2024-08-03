import yt_dlp

# List audio and video formats before downloading
def list_formats(url):
    ydl_opts = {
        'quiet': True,
        'no_warnings': True
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        ydl.list_formats(info_dict)

# Downloads the audio file only
def download_audio(url, audio_id):
    ydl_opts = {
        'format': audio_id,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio'
        }],
        'outtmpl': f'/Users/armaanswan/Downloads/%(title)s.%(ext)s',
        'quiet': True,
        'no_warnings': True
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(url)

    print("\nAudio downloaded successfully!\n")

# Downloads the video file only
def download_video(url, video_id):
    ydl_opts = {
        'format': video_id,
        'outtmpl': f'/Users/armaanswan/Downloads/%(title)s.%(ext)s',
        'quiet': True,
        'no_warnings': True
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(url)

    print("\nVideo downloaded successfully!\n")

# Downlods both the audio and video file
def download_audio_video(url, audio_id, video_id):
    ydl_opts = {
        'format': f'{video_id}+{audio_id}',
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4' # Replace with desired format
        }],
        'outtmpl': f'/Users/armaanswan/Downloads/%(title)s.%(ext)s',
        'quiet': True,
        'no_warnings': True
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(url)

    print("\nDownload successful!\n")

if __name__ == "__main__":
    print("\nWelcome to the YouTube Downloader!\n")
    
    url = input("Enter YouTube URL: ")
    print("\n")
    list_formats(url)

    audio_id = input("\nEnter audio ID: ")
    video_id = input("\nEnter video ID: ")

    if (audio_id and video_id):
        print("\nDownloding...")
        download_audio_video(url, audio_id, video_id)
    elif (audio_id and not video_id):
        print("\nDownloading audio only...")
        download_audio(url, audio_id)
    else:
        print("\nDownloading video only...")
        download_video(url, video_id)
