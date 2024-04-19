from pytube import YouTube

def download_video(url, format='mp4'):
    yt = YouTube(url)
    if format == 'mp4':
        stream = yt.streams.get_highest_resolution()
    elif format == 'mp3' or format == 'aac':
        stream = yt.streams.filter(only_audio=True).first()
    else:
        print("Unsupported format")
        return

    print(f"Downloading {format}...")
    stream.download(output_path='.', filename=f"video.{format}")
    print("Download completed!")

def main():
    print("Welcome to YouTube Downloader!")
    url = input("Enter the YouTube video URL: ")
    print("Choose the format you want to download:")
    print("1. MP4 (Video)")
    print("2. MP3 (Audio)")
    print("3. AAC (Audio)")
    choice = input("Enter your choice (1, 2, or 3): ")

    format = 'mp4'
    if choice == '2':
        format = 'mp3'
    elif choice == '3':
        format = 'aac'

    download_video(url, format)

if __name__ == "__main__":
    main()
