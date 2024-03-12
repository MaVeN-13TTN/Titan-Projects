import os
import tkinter as tk
from tkinter import filedialog, ttk
from customtkinter import CTk, CTkButton, CTkLabel, CTkEntry, CTkToplevel, CTkFrame
import textract
import comtypes.client
from PIL import Image
from pytesseract import pytesseract
import PyPDF2

poppler_path = r'C:\Program Files\poppler-24.03.0\bin\pdftotext.exe'
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
    slide.Shapes.AddTextbox(1, 0, 0, 5, 3).TextFrame.TextRange.Text = extract_pdf_text(input_file)
    pres.SaveAs(output_file, 32)  # 32 = ppSaveAsDefault
    pres.Close()
    prs.Quit()

def extract_pdf_text(pdf_file):
    with open(pdf_file, 'rb') as f:
        pdf_reader = PyPDF2.PdfFileReader(f)
        text = ''
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            text += page.extractText()
    return text

def ocr_text_from_image(image_file):
    image = Image.open(image_file)
    text = pytesseract.image_to_string(image)
    return text

def ocr_text_from_pdf(pdf_file):
    text = pytesseract.pdf_to_text(pdf_file)
    return text

def ocr_text_from_word(word_file):
    text = textract.process(word_file, method='docx').decode('utf-8')
    return text

def browse_file(filetype, entry):
    file_path = filedialog.askopenfilename(filetypes=[(filetype, '*.' + filetype)])
    entry.insert(0, file_path)

def save_file(content, output_file):
    downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
    output_file = os.path.join(downloads_folder, output_file)
    with open(output_file, 'w') as f:
        f.write(content)

def convert_and_download():
    input_file = input_entry.get()
    conversion_type = conversion_type_var.get()
    input_file_name, input_file_ext = os.path.splitext(os.path.basename(input_file))

    if conversion_type == 'PDF to Word':
        if input_file_ext.lower() == '.pdf':
            output_file = os.path.join(os.path.expanduser("~"), "Downloads", f"{input_file_name}.docx")
            convert_pdf_to_word(input_file, output_file)
            save_file('', output_file)
        else:
            print("Input file shouldbe a PDF")
    elif conversion_type == 'PDF to PowerPoint':
        if input_file_ext.lower() == '.pdf':
            output_file = os.path.join(os.path.expanduser("~"), "Downloads", f"{input_file_name}.pptx")
            convert_pdf_to_ppt(input_file, output_file)
            save_file('', output_file)
        else:
            print("Input file should be a PDF")
    elif conversion_type == 'Word to PDF':
        if input_file_ext.lower() == '.docx':
            output_file = os.path.join(os.path.expanduser("~"), "Downloads", f"{input_file_name}.pdf")
            convert_word_to_pdf(input_file, output_file)
            save_file('', output_file)
        else:
            print("Input file should be a Word file (.docx)")
    elif conversion_type == 'Image to Text':
        if input_file_ext.lower() in ['.jpg', '.jpeg', '.png']:
            output_file = os.path.join(os.path.expanduser("~"), "Downloads", f"{input_file_name}.txt")
            text = ocr_text_from_image(input_file)
            save_file(text, output_file)
        else:
            print("Input file should be an image file (jpg, jpeg, png)")
    elif conversion_type == 'PDF to Text':
        if input_file_ext.lower() == '.pdf':
            output_file = os.path.join(os.path.expanduser("~"), "Downloads", f"{input_file_name}.txt")
            text = extract_pdf_text(input_file)
            save_file(text, output_file)
        else:
            print("Input file should be a PDF file")
    elif conversion_type == 'Word to Text':
        if input_file_ext.lower() == '.docx':
            output_file = os.path.join(os.path.expanduser("~"), "Downloads", f"{input_file_name}.txt")
            text = ocr_text_from_word(input_file)
            save_file(text, output_file)
        else:
            print("Input file should be a Word file (.docx)")
    else:
        print("Unsupported conversion type")

root = CTk()
root.title("File Converter and OCR")

input_frame = CTkFrame(root)
input_frame.pack(pady=20)

input_label = CTkLabel(input_frame, text="Input file:")
input_label.grid(row=0, column=0, padx=(0, 10))

input_entry = CTkEntry(input_frame, width=300)
input_entry.grid(row=0, column=1, padx=(0, 10))

browse_input_button = CTkButton(input_frame, text="Browse", command=lambda: browse_file('pdf', input_entry))
browse_input_button.grid(row=0, column=2)

output_frame = CTkFrame(root)
output_frame.pack(pady=20)

conversion_type_var = tk.StringVar()
conversion_types = ['PDF to Word', 'PDF to PowerPoint', 'Word to PDF', 'Image to Text', 'PDF to Text', 'Word to Text']
conversion_type_dropdown = ttk.Combobox(output_frame, textvariable=conversion_type_var, values=conversion_types)
conversion_type_dropdown.grid(row=0, column=0, padx=(0, 10))
conversion_type_var.set(conversion_types[0])

download_button = CTkButton(output_frame, text="Download", command=convert_and_download)
download_button.grid(row=0, column=1, padx=(0, 10))

root.mainloop()