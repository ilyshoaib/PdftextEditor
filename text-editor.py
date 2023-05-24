import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfFileReader, PdfFileWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from PIL import Image
import io
import os

# Global variables
pdf_writer = PdfFileWriter()
current_file = None

# Functions
def create_pdf():
    global pdf_writer, current_file
    pdf_writer = PdfFileWriter()
    current_file = None
    messagebox.showinfo("Create File", "New File created.")

def open_pdf():
    global pdf_writer, current_file
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        current_file = file_path
        pdf_writer = PdfFileWriter()
        pdf_reader = PdfFileReader(current_file)
        for page_num in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page_num))
        messagebox.showinfo("Open File", f"{current_file} opened.")

def save_pdf():
    global pdf_writer, current_file
    if current_file is None:
        current_file = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("Text or PDF files", "*.pdf")])
    if current_file:
        with open(current_file, "wb") as output_file:
            pdf_writer.write(output_file)
        messagebox.showinfo("Save", f"{current_file} saved.")

def add_text():
    global pdf_writer
    text = input("Enter the text to add: ")
    if text:
        packet = io.BytesIO()
        can = canvas.Canvas(packet, pagesize=letter)
        can.setFont("Helvetica", 12)
        can.drawString(72, 720, text)
        can.save()
        packet.seek(0)
        watermark = PdfFileReader(packet)
        watermark_page = watermark.getPage(0)
        
        if pdf_writer.getNumPages() > 0:
            page = pdf_writer.getPage(0)
            page.merge_page(watermark_page)
        else:
            pdf_writer.addPage(watermark_page)
            
        messagebox.showinfo("Add Text", "Text added successfully.")
    else:
        messagebox.showwarning("Add Text", "No text entered.")


def add_image():
    global pdf_writer
    image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png")])
    if image_path:
        img = Image.open(image_path)
        width, height = img.size
        if width > height:
            new_width = 792
            new_height = int((new_width / width) * height)
        else:
            new_height = 612
            new_width = int((new_height / height) * width)
        img = img.resize((new_width, new_height))
        img.save("temp_img.jpg", "JPEG")
        packet = io.BytesIO()
        can = canvas.Canvas(packet, pagesize=letter)
        can.drawImage("temp_img.jpg", 36, 36, width=new_width, height=new_height)
        can.save()
        packet.seek(0)
        watermark = PdfFileReader(packet)
        watermark_page = watermark.getPage(0)
        
        if pdf_writer.getNumPages() > 0:
            page = pdf_writer.getPage(0)
            page.mergePage(watermark_page)
        else:
            pdf_writer.addPage(watermark_page)
            
        os.remove("temp_img.jpg")

def crop_image():
    global pdf_writer
    image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png")])
    if image_path:
        img = Image.open(image_path)
        original_width, original_height = img.size

        aspect_ratio = input("Enter the desired aspect ratio (e.g., 1.1, 16:9): ")
        if ":" in aspect_ratio:
            w_ratio, h_ratio = map(int, aspect_ratio.split(":"))
        else:
            w_ratio = float(aspect_ratio)
            h_ratio = 1

        # Calculate the new dimensions
        new_width = original_width
        new_height = int(original_width * h_ratio / w_ratio)

        # If new height is greater than the original height, resize based on height
        if new_height > original_height:
            new_height = original_height
            new_width = int(original_height * w_ratio / h_ratio)

        # Calculate the position to crop
        left = (original_width - new_width) / 2
        top = (original_height - new_height) / 2
        right = (original_width + new_width) / 2
        bottom = (original_height + new_height) / 2

        cropped_img = img.crop((left, top, right, bottom))
        cropped_img.save("temp_cropped_img.jpg", "JPEG")

        packet = io.BytesIO()
        can = canvas.Canvas(packet, pagesize=letter)
        can.drawImage("temp_cropped_img.jpg", 36, 36, width=612, height=612)
        can.save()
        packet.seek(0)
        watermark = PdfFileReader(packet)
        watermark_page = watermark.getPage(0)
        
        if pdf_writer.getNumPages() > 0:
            page = pdf_writer.getPage(0)
            page.mergePage(watermark_page)
        else:
            pdf_writer.addPage(watermark_page)
            
        os.remove("temp_cropped_img.jpg")

def merge_pdf():
    global pdf_writer
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        pdf_reader = PdfFileReader(file_path)
        for page_num in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page_num))

def split_pdf():
    global pdf_writer
    if current_file is None:
        current_file = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if current_file:
        pdf_reader = PdfFileReader(current_file)
        for page_num in range(pdf_reader.getNumPages()):
            output = PdfFileWriter()
            output.addPage(pdf_reader.getPage(page_num))
            split_file_name = os.path.splitext(current_file)[0] + "_page" + str(page_num + 1) + ".pdf"
            with open(split_file_name, "wb") as output_file:
                output.write(output_file)
   
def rotate_pdf():
    global pdf_writer
    degrees = input("Enter the number of degrees to rotate (clockwise): ")
    try:
        degrees = int(degrees)
        if degrees % 90 != 0:
            print("Error: Please enter a multiple of 90 degrees.")
            return
        for page_num in range(pdf_writer.getNumPages()):
            page = pdf_writer.getPage(page_num)
            page.rotateClockwise(degrees)
    except ValueError:
        print("Error: Please enter a valid integer value.")

def delete_page():
    global pdf_writer
    page_num = input("Enter the page number to delete (starting from 1): ")
    try:
        page_num = int(page_num) - 1
        if page_num < 0 or page_num >= pdf_writer.getNumPages():
            print(f"Error: Please enter a page number between 1 and {pdf_writer.getNumPages()}.")
            return
        new_pdf_writer = PdfFileWriter()
        for i in range(pdf_writer.getNumPages()):
            if i != page_num:
                new_pdf_writer.addPage(pdf_writer.getPage(i))
        pdf_writer = new_pdf_writer
    except ValueError:
        print("Error: Please enter a valid integer value.")

# Create the tkinter GUI
root = tk.Tk()
root.title("Text Editor")

# Create buttons and menus
create_button = tk.Button(root, text="Create a file", command=create_pdf)
create_button.pack()

open_button = tk.Button(root, text="Open ", command=open_pdf)
open_button.pack()

save_button = tk.Button(root, text="Save ", command=save_pdf)
save_button.pack()

add_text_button = tk.Button(root, text="Add Text", command=add_text)
add_text_button.pack()

add_image_button = tk.Button(root, text="Add Image", command=add_image)
add_image_button.pack()

crop_image_button = tk.Button(root, text="Crop Image", command=crop_image)
crop_image_button.pack()

rotate_pdf_button = tk.Button(root, text="Rotate", command=rotate_pdf)
rotate_pdf_button.pack()

delete_page_button = tk.Button(root, text="Delete Page", command=delete_page)
delete_page_button.pack()

# Run the tkinter main loop
root.mainloop()
