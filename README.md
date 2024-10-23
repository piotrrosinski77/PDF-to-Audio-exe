# PDF-to-Audio-exe

PDF-to-Audio-exe is a simple Python application that converts text from PDF files into audio files (MP3) using text-to-speech synthesis. This project leverages the `PyPDF2` library for PDF handling and `pyttsx3` for text-to-speech conversion, all packaged into a standalone executable using `PyInstaller`.

<div align="center">
    <img src="images/screenshot.png" alt="Application Screenshot 1" width="200" style="display: inline-block;"/>
    <img src="images/screenshot_2.png" alt="Application Screenshot 2" width="300" style="display: inline-block;"/>
</div>

## Features
- Convert any PDF file to audio in MP3 format.

## Requirements
- Python 3.x
- PyPDF2
- pyttsx3

## Installation
Clone this repository:

   ```bash
   git clone https://github.com/yourusername/PDF-to-Audio-exe.git
   cd PDF-to-Audio-exe
   ```

## Usage
Place the PDF file you want to convert in the same directory as the executable.

Run the executable:

```bash
./PDF-to-Audio.exe
```

When prompted, enter the name of the PDF file (without the extension).

The audio will be saved as an MP3 file in the same directory.
