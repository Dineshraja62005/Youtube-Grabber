from pytube import YouTube

# Function to download a video
def download_video(url, output_path):
    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()
    stream.download(output_path)
    print("Video downloaded successfully!")

# Function to download audio
def download_audio(url, output_path):
    yt = YouTube(url)
    stream = yt.streams.filter(only_audio=True).first()
    stream.download(output_path)
    print("Audio downloaded successfully!")

# User choice menu
def user_choice():
    print("Choose an option:")
    print("1. Download Video")
    print("2. Download Audio")
    choice = input("Enter your choice (1/2): ")
    return choice

# Main function
if __name__ == "__main":
    url = input("Enter the YouTube video URL: ")
    output_directory = "path/to/save/downloads/"
    
    choice = user_choice()

    if choice == "1":
        download_video(url, output_directory)
    elif choice == "2":
        download_audio(url, output_directory)
    else:
        print("Invalid choice. Please enter 1 or 2.")
