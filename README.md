# PDF/Text to Audio Converter

A simple Python application with a graphical user interface (GUI) using Tkinter that converts PDF or TXT files into speech (MP3 audio) using offline or online text-to-speech engines.

---

## Features

- Supports `.pdf` and `.txt` input files
- Extracts text from PDFs using `PyPDF2`
- Two text-to-speech engine options:
  - **Offline:** `pyttsx3` (no internet required)
  - **Online:** `gTTS` (Google Text-to-Speech, requires internet)
- Save audio output as `.mp3`
- Easy-to-use GUI built with Tkinter
- Cross-platform support (Windows, macOS, Linux)

---

## How to Run

1. **Clone the repository:**

   ```bash
   git clone https://github.com/AdarshZolekar/PDF-to-Audio-Converter.git
   ```

2. **Run the script:**

   - Open a terminal or command prompt. 
   - Navigate to the project directory:

     ```bash
     cd PDF-to-Audio-Converter
     ```

   - Run the main script:

     ```bash
     python PDF-to-Audio-Converter.py
     ```

   - Follow the on-screen instructions and start listening!

---

## How to use

- Click Browse to select a PDF or TXT file.

- Choose the TTS engine (Offline or Online).

- Click Convert to Audio.

- Choose the location and filename to save the MP3 audio.

- Wait for conversion success message.

---

## Dependencies

1. **pyttsx3** *(Offline TTS engine)*

2. **gTTS** *(Google Text-to-Speech)*

3. **PyPDF2** *(PDF text extraction)*

4. **Tkinter** *(built-in Python GUI library)*

---

## Notes

- Offline TTS (pyttsx3) does not require an internet connection.

- Online TTS (gTTS) requires an internet connection to work.

- PDF files must contain selectable text (not scanned images).

- Tested on Python 3.7+.

---

## Future Improvements 

- Support for more file formats like .docx and scanned PDFs (with OCR)

- Adjustable speech rate and voice selection for offline TTS (pyttsx3)

- Audio playback within the app right after conversion

---

## License

This project is open-source under the MIT License.

---

## Contributions

Feel free to open issues or submit pull requests for improvements or bug fixes!

