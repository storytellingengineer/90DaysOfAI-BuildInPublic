# 🗣️ Day 11 - Speech-to-Text with Google Speech API vs OpenAI Whisper

This project demonstrates two powerful methods for converting audio to text:

1. **Google Web Speech API**
2. **OpenAI Whisper**

---

## 🚀 Project Overview

I explored both **online (Google API)** and **offline (Whisper)** transcription methods to understand their strengths, limitations, and real-world applications.

---

## 🧠 Why This Project?

Speech-to-text is being used in:
- Meeting transcription apps (Otter.ai, Fireflies)
- Subtitling and content generation
- Accessibility for the hearing impaired
- Real-time customer service

I wanted to explore both a **quick-to-use API-based approach** and a **deep learning model** for handling longer and noisier audio.

---

## 🔧 Setup Instructions

### ✅ Whisper (Offline)

```bash
pip install -U openai-whisper
sudo apt update && sudo apt install ffmpeg

```

### ✅ Google Speech API (Online)

```bash
pip install SpeechRecognition
pip install PyAudio  # Might need special setup in Colab or Windows
```

## 💡 What Each Approach Offers

| Feature              | Google Speech API | OpenAI Whisper |
|----------------------|-------------------|----------------|
| Requires Internet    | ✅ Yes            | ❌ No          |
| Handles Noise        | ⚠️ Moderate       | ✅ Yes         |
| Long Audio Support   | ❌ No             | ✅ Yes         |
| Multilingual         | ⚠️ Limited        | ✅ Yes         |
| Open Source          | ❌ No             | ✅ Yes         |
| Speed                | ✅ Fast (live)    | ⚠️ Slower      |

---

## ❗ Challenges Faced

| Issue                     | Solution                                         |
|---------------------------|--------------------------------------------------|
| `PyAudio` install errors  | Used Google Colab or pip wheels manually         |
| Whisper model loading slow| Used `small` model to reduce memory usage        |
| Whisper needs `ffmpeg`    | Installed manually on Colab                      |
| Accuracy tradeoffs        | Tested with different samples to compare outputs |

---

## 📚 Reflections & Learnings

- Google API is great for fast, browser-based use cases, especially for real-time transcription.
- OpenAI Whisper is a powerful open-source tool, better suited for offline or longer audio analysis.
- Combining both gives a practical understanding of cloud-based vs edge-based AI systems.
- Whisper's multilingual support opens doors to global accessibility tools.

---

## 🔮 Future Additions

- Streamlit UI for both Whisper and Google API  
- Real-time transcription with microphone input  
- Timestamped transcripts for subtitle generation
