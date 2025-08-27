import tkinter as tk
from tkinter import filedialog, messagebox
import pyttsx3
from gtts import gTTS
import PyPDF2
import os

def extract_text_from_file(file_path):
    if file_path.endswith(".txt"):
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    elif file_path.endswith(".pdf"):
        text = ""
        with open(file_path, "rb") as file:
            pdf = PyPDF2.PdfReader(file)
            for page in pdf.pages:
                text += page.extract_text()
        return text
    else:
        return None

def convert_to_audio(text, output_path, use_offline=True):
    try:
        if use_offline:
            engine = pyttsx3.init()
            engine.save_to_file(text, output_path)
            engine.runAndWait()
        else:
            tts = gTTS(text)
            tts.save(output_path)
        messagebox.showinfo("Success", f"Audio saved as {output_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to convert text to audio:\n{str(e)}")

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text or PDF files", "*.txt *.pdf")])
    if file_path:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, file_path)

def generate_audio():
    file_path = file_entry.get()
    if not file_path or not os.path.exists(file_path):
        messagebox.showerror("Error", "Please select a valid file.")
        return

    text = extract_text_from_file(file_path)
    if not text:
        messagebox.showerror("Error", "Could not extract text from the file.")
        return

    output_file = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")])
    if not output_file:
        return

    use_offline = engine_var.get() == "offline"
    convert_to_audio(text, output_file, use_offline)

root = tk.Tk()
root.title("PDF/Text to Audio Converter")
root.geometry("500x250")
root.resizable(False, False)

tk.Label(root, text="Select PDF or TXT file:").pack(pady=5)
file_frame = tk.Frame(root)
file_frame.pack(pady=5)

file_entry = tk.Entry(file_frame, width=50)
file_entry.pack(side=tk.LEFT, padx=5)

browse_btn = tk.Button(file_frame, text="Browse", command=browse_file)
browse_btn.pack(side=tk.LEFT)

tk.Label(root, text="Select TTS Engine:").pack(pady=10)

engine_var = tk.StringVar(value="offline")
tk.Radiobutton(root, text="Offline (pyttsx3)", variable=engine_var, value="offline").pack()
tk.Radiobutton(root, text="Online (gTTS - needs internet)", variable=engine_var, value="online").pack()

generate_btn = tk.Button(root, text="Convert to Audio", command=generate_audio, bg="#4CAF50", fg="white", padx=10, pady=5)
generate_btn.pack(pady=20)

root.mainloop()
