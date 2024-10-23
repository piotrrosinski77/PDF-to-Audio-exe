import os
from PyPDF2 import PdfReader
import pyttsx3
import tkinter as tk
from tkinter import filedialog, messagebox

def convert_pdf_to_audio():
    # Open file dialog to select a PDF file
    pdf_path = filedialog.askopenfilename(title="Select a PDF file", filetypes=[("PDF files", "*.pdf")])
    
    if not pdf_path:  # If no file is selected, return
        return

    # Check if the selected file is a PDF
    if not pdf_path.endswith('.pdf'):
        messagebox.showerror("Invalid File", "Please select a valid PDF file.")
        return

    # Read text from the PDF file
    try:
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""

        if text.strip():
            # Initialize pyttsx3
            engine = pyttsx3.init()

            # Save the speech to an mp3 file
            mp3_output = os.path.splitext(os.path.basename(pdf_path))[0] + ".mp3"
            mp3_path = os.path.join(os.path.dirname(pdf_path), mp3_output)

            # Set voice and speed settings
            engine.setProperty('rate', 200)  # Set speed (default is 200)

            # Convert text to speech
            engine.save_to_file(text, mp3_path)
            engine.runAndWait()

            messagebox.showinfo("Success", f"The text has been saved as {mp3_output} in the same directory as the PDF file.")
        else:
            messagebox.showwarning("No Text", "The PDF file does not contain any text to read.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create the main window
root = tk.Tk()
root.title("PDF to Audio Converter")
root.geometry("300x150")

# Create a button to start the conversion
convert_button = tk.Button(root, text="Select PDF and Convert to Audio", command=convert_pdf_to_audio)
convert_button.pack(pady=30)

# Start the GUI event loop
root.mainloop()
