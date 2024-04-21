from pytube import YouTube
import datetime

def download_video(url, format='mp4'):
    yt = YouTube(url)
    if format == 'mp4':
        stream = yt.streams.get_highest_resolution()
    elif format == 'mp3':
        stream = yt.streams.filter(only_audio=True).first()
    else:
        print("Unsupported format")
        return

    # Saat ve tarih bilgisi ile dosya ismini oluştur.
    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{current_time}.{format}"

    print(f"Downloading {format} as {filename}...")
    stream.download(output_path='.', filename=filename)
    print("Download completed!")

def main():
    print("Welcome to YouTube Downloader!")
    print("How would you like to provide the YouTube video link?")
    print("1. Enter link directly")
    print("2. Read from a text file")
    choice = input("Enter your choice (1 or 2): ")

    urls = []
    if choice == '1':
        url = input("Enter the YouTube video URL: ")
        urls.append(url)
    elif choice == '2':
        file_path = input("Enter the path to the text file: ")
        with open(file_path, "r") as file:
            urls = file.read().splitlines()
    else:
        print("Invalid choice")
        return

    print("Choose the format you want to download:")
    print("1. MP4 (Video)")
    print("2. MP3 (Audio)")
    format_choice = input("Enter your choice (1 or 2): ")

    format = 'mp4'
    if format_choice == '2':
        format = 'mp3'

    for url in urls:
        download_video(url, format)

if __name__ == "__main__":
    main()
