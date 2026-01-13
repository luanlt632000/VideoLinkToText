# VideoLinkToText

Dưới đây là **README.md** hoàn chỉnh cho file Python bạn gửi, có hướng dẫn cài môi trường cho **Windows** và **macOS**.

---

# 🎬 Facebook Video → Audio → Text Tool

Công cụ Python giúp bạn:

1. Tải video Facebook (Reels, Post, Video…)
2. Trích xuất âm thanh ra MP3
3. Chuyển giọng nói thành văn bản (speech-to-text) bằng **OpenAI Whisper**

---

## 📦 Tính năng

| Chức năng               | Mô tả                                          |
| ----------------------- | ---------------------------------------------- |
| Download Facebook video | Dùng `yt-dlp`                                  |
| Tách âm thanh           | Dùng `ffmpeg`                                  |
| Chuyển audio → text     | Dùng `openai-whisper` (offline, chạy trên máy) |

---

## 🧰 Yêu cầu hệ thống

| Thành phần | Phiên bản            |
| ---------- | -------------------- |
| Python     | 3.8+                 |
| FFmpeg     | Bắt buộc             |
| Internet   | Chỉ cần để tải video |

---

# 🖥 Cài đặt trên Windows

### 1. Cài Python

Tải tại:
[https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/)

⚠ Khi cài nhớ tick **"Add Python to PATH"**

Kiểm tra:

```bash
python --version
pip --version
```

---

### 2. Cài FFmpeg

Tải FFmpeg:
[https://www.gyan.dev/ffmpeg/builds/](https://www.gyan.dev/ffmpeg/builds/)

→ Tải bản **release-full.zip**
→ Giải nén → Copy thư mục `ffmpeg` vào `C:\ffmpeg`

Thêm vào PATH:

1. Mở **Environment Variables**
2. Edit `Path`
3. Add:

```
C:\ffmpeg\bin
```

Kiểm tra:

```bash
ffmpeg -version
```

---

### 3. Cài thư viện Python

```bash
pip install yt-dlp openai-whisper
```

---

# 🍎 Cài đặt trên macOS

### 1. Cài Homebrew (nếu chưa có)

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

---

### 2. Cài Python & FFmpeg

```bash
brew install python ffmpeg
```

---

### 3. Cài thư viện Python

```bash
pip3 install yt-dlp openai-whisper
```

---

# ▶️ Cách sử dụng

Lưu file Python thành:

```
fb_to_text.py
```

Chạy:

```bash
python fb_to_text.py
```

Hoặc trên macOS:

```bash
python3 fb_to_text.py
```

---

## 📌 Quy trình chạy

1. Nhập link Facebook:

```
https://www.facebook.com/reel/xxxxxxx
```

2. Script sẽ:

   * Tải video → `video.mp4`
   * Trích audio → `audio.mp3`
   * Hỏi có chạy speech-to-text không

3. Nếu chọn **y**
   → Xuất file:

```
transcription.txt
```

---

# 🧠 Ghi chú Whisper

Whisper chạy **offline**, không cần OpenAI API.
Model mặc định: `base`

Nếu máy mạnh có thể chỉnh:

```python
model = whisper.load_model("medium")
```

Hoặc:

```
tiny, base, small, medium, large
```

---

# ⚠️ Lỗi thường gặp

| Lỗi                | Cách sửa                                  |
| ------------------ | ----------------------------------------- |
| `ffmpeg not found` | Chưa cài hoặc chưa add PATH               |
| `pip not found`    | Python chưa add PATH                      |
| Video không tải    | Facebook link private hoặc login required |
| Whisper chậm       | Dùng model nhỏ hơn (`base`, `small`)      |

---

# 📁 File sinh ra

| File                | Nội dung       |
| ------------------- | -------------- |
| `video.mp4`         | Video Facebook |
| `audio.mp3`         | Audio          |
| `transcription.txt` | Văn bản        |

---

Nếu bạn muốn:

* Xuất **SRT subtitle**
* Chạy **batch nhiều link**
* Làm **UI web**

cứ nói, tôi setup cho bạn.
