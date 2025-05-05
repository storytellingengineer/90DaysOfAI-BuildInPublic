# 🎙️ Speech-to-Text Transcription App

A simple web app that transcribes speech from uploaded audio files using Python's `SpeechRecognition` library and Streamlit.

---

## 🚀 Features
- Upload `.wav` or `.mp3` files
- View and play the uploaded audio
- Transcribe using Google Web Speech API

---

## 📌 Why This Project?
Speech interfaces are transforming accessibility, virtual assistants, and real-time translation. This app is a first step toward building such voice-based systems.

---

## ⚙️ How to Run

1. Clone the repository
2. Install requirements:
    ```
    pip install -r requirements.txt
    ```
3. Run the app:
    ```
    streamlit run app.py
    ```

---

## 😓 Challenges Faced

| Issue                        | Resolution                                      |
|-----------------------------|--------------------------------------------------|
| Audio file conversion issues| Used `tempfile` for smooth handling in Streamlit |
| API errors or no response   | Added try/except with clear user messages        |
| Background noise interference | Recommended clearer audio inputs                |

---

## 📚 Learnings

- Real-time transcription requires clean audio and proper formats
- Google SpeechRecognition API works well but needs internet access
- Using `streamlit` makes prototyping fast and interactive

---

## 🛠️ Future Enhancements
- Add microphone recording support
- Support for longer audio with chunk processing
- Support for multi-language transcription

---

## 👀 Sample Output

> "Welcome to the world of voice-based AI applications."

---

