import os 
from PyPDF2 import PdfReader
import pyttsx3

# Get the PDF file name from the user
file_name = input("Enter the name of the PDF file (without extension) in the current directory: ") + ".pdf"

# Path to the current directory
current_directory = os.getcwd()

# Path to the PDF file
pdf_path = os.path.join(current_directory, file_name)

# Check if the file exists
if os.path.exists(pdf_path):
    print(f"The file '{file_name}' is located in the current directory.")
    
    # Read text from the PDF file
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()

    if text.strip():
        # Initialize pyttsx3
        engine = pyttsx3.init()

        # Save the speech to an mp3 file
        mp3_output = file_name.replace(".pdf", ".mp3")
        mp3_path = os.path.join(current_directory, mp3_output)

        # Set voice and speed settings
        engine.setProperty('rate', 200)  # Set speed (default is 200)

        # Convert text to speech
        engine.save_to_file(text, mp3_path)
        engine.runAndWait()
        
        print(f"The text has been saved as {mp3_output} in the current directory.")
    else:
        print("The PDF file does not contain any text to read.")
else:
    print(f"The file '{file_name}' was not found in the current directory.")
