import os
import subprocess
import sys

def install_dependencies():
    """Cài đặt các thư viện cần thiết."""
    print("Đang cài đặt thư viện yt-dlp...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "yt-dlp"])

def download_facebook_video(url, output_name="video.mp4"):
    """Tải video từ Facebook sử dụng yt-dlp."""
    print(f"Đang tải video từ: {url}")
    try:
        # Sử dụng yt-dlp để tải video
        command = [
            "yt-dlp",
            "-o", output_name,
            url
        ]
        subprocess.run(command, check=True)
        print(f"Tải video thành công: {output_name}")
        return output_name
    except Exception as e:
        print(f"Lỗi khi tải video: {e}")
        return None

def extract_audio(video_path, audio_path="audio.mp3"):
    """Trích xuất âm thanh từ video sử dụng ffmpeg."""
    print(f"Đang trích xuất âm thanh từ: {video_path}")
    try:
        command = [
            "ffmpeg",
            "-i", video_path,
            "-vn",
            "-acodec", "libmp3lame",
            "-q:a", "2",
            audio_path,
            "-y" # Ghi đè nếu file đã tồn tại
        ]
        subprocess.run(command, check=True)
        print(f"Trích xuất âm thanh thành công: {audio_path}")
        return audio_path
    except Exception as e:
        print(f"Lỗi khi trích xuất âm thanh: {e}")
        return None

def transcribe_audio(audio_path):
    """
    Chuyển đổi âm thanh thành văn bản.
    Lưu ý: Trong môi trường thực tế, bạn có thể sử dụng OpenAI Whisper hoặc các dịch vụ Cloud STT.
    Dưới đây là ví dụ sử dụng thư viện 'openai-whisper' (cần cài đặt: pip install openai-whisper).
    """
    print("Đang chuyển đổi âm thanh thành văn bản (sử dụng Whisper)...")
    try:
        import whisper
        model = whisper.load_model("base")
        result = model.transcribe(audio_path)
        
        output_file = "transcription.txt"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(result["text"])
        
        print(f"Chuyển đổi thành công! Kết quả lưu tại: {output_file}")
        return result["text"]
    except ImportError:
        print("Vui lòng cài đặt thư viện whisper: pip install openai-whisper")
    except Exception as e:
        print(f"Lỗi khi chuyển đổi: {e}")

if __name__ == "__main__":
    # URL video Facebook Reel
    video_url = input("Nhập URL video Facebook: ")
    
    # 1. Tải video
    video_file = download_facebook_video(video_url)
    
    if video_file:
        # 2. Trích xuất âm thanh
        audio_file = extract_audio(video_file)
        
        if audio_file:
            # 3. Chuyển đổi thành văn bản (Yêu cầu cài đặt whisper)
            print("\n--- Hướng dẫn tiếp theo ---")
            print("Để chuyển đổi âm thanh thành văn bản, bạn cần cài đặt thư viện Whisper của OpenAI:")
            print("1. pip install openai-whisper")
            print("2. Đảm bảo máy tính đã cài đặt ffmpeg.")
            print("\nBạn có muốn thử chạy transcription ngay không? (y/n)")
            choice = input().lower()
            if choice == 'y':
                transcribe_audio(audio_file)
