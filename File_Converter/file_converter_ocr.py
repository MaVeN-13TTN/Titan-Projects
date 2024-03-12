import os
import tkinter as tk
from tkinter import filedialog
from customtkinter import CTk, CTkButton, CTkLabel, CTkEntry, CTkToplevel, CTkFrame
import textract
import comtypes.client
from PIL import Image
from pytesseract import pytesseract

pytesseract.pytesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def convert_pdf_to_word(input_file, output_file):
    textract.process(input_file, output_file, extensions=['.docx'])

def convert_word_to_pdf(input_file, output_file):
    word = comtypes.client.CreateObject('Word.Application')
    doc = word.Documents.Open(input_file)
    doc.SaveAs(output_file, FileFormat=17)
    doc.Close()
    word.Quit()

def convert_pdf_to_ppt(input_file, output_file):
    prs = comtypes.client.CreateObject('PowerPoint.Application')
    pres = prs.Presentations.Open(input_file)
    slide = pres.Slides.Add(1, 12)  # 12 = ppLayoutText
    slide.Shapes.Title.TextFrame.TextRange.Text = os.path.basename(input_file)
    left = top = inch = 1
    slide.Shapes.Title.Left = inch * left
    slide.Shapes.Title.Top = inch * top
    slide.Shapes.AddTextbox(1, 0, 0, 5, 3).TextFrame.TextRange.Text = textract.process(input_file).decode('utf-8')
    pres.SaveAs(output_file, 32)  # 32 = ppSaveAsDefault
    pres.Close()
    prs.Quit()

def ocr_text_from_image(image_file):
    image = Image.open(image_file)
    text = pytesseract.image_to_string(image)
    return text

def ocr_text_from_pdf(pdf_file):
    text = textract.process(pdf_file).decode('utf-8')
    return text

def ocr_text_from_word(word_file):
    text = textract.process(word_file, method='docx').decode('utf-8')
    return text

def browse_file(filetype, entry):
    file_path = filedialog.askopenfilename(filetypes=[(filetype, '*.' + filetype)])
    entry.insert(0, file_path)

def convert_and_ocr():
    input_file = convert_entry.get()
    output_file = output_entry.get()
    filetype = input_file.split('.')[-1]

    if filetype == 'pdf':
        if output_file.endswith('.docx'):
            convert_pdf_to_word(input_file, output_file)
        elif output_file.endswith('.pptx'):
            convert_pdf_to_ppt(input_file, output_file)
    elif filetype == 'docx':
        if output_file.endswith('.pdf'):
            convert_word_to_pdf(input_file, output_file)
    elif filetype in ['jpg', 'jpeg', 'png']:
        text = ocr_text_from_image(input_file)
        with open(output_file, 'w') as f:
            f.write(text)
    else:
        print("Unsupported file format")

root = CTk()
root.title("File Converter and OCR")

convert_frame = CTkFrame(root)
convert_frame.pack(pady=20)

convert_label = CTkLabel(convert_frame, text="Convert and OCR:")
convert_label.grid(row=0, column=0, padx=(0, 10))

convert_entry = CTkEntry(convert_frame, width=300)
convert_entry.grid(row=0, column=1, padx=(0, 10))

browse_button = CTkButton(convert_frame, text="Browse", command=lambda: browse_file('pdf', convert_entry))
browse_button.grid(row=0, column=2)

output_frame = CTkFrame(root)
output_frame.pack(pady=20)

output_label = CTkLabel(output_frame, text="Output file:")
output_label.grid(row=0, column=0, padx=(0, 10))

output_entry = CTkEntry(output_frame, width=300)
output_entry.grid(row=0, column=1, padx=(0, 10))

ocr_button = CTkButton(output_frame, text="Convert and OCR", command=convert_and_ocr)
ocr_button.grid(row=0, column=2)

root.mainloop()