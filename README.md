# PDF Text Editor

**Note: The following introduction assumes that the PDF Text Editor project was presented as an Operating System project in the 4th semester.**

## Introduction

Welcome to the PDF Text Editor project! This project was developed as part of our Operating System course in the 4th semester. The aim of this project was to create a simple text editor application that allows users to perform various operations on PDF files. 

The PDF Text Editor provides a user-friendly graphical interface for performing tasks such as creating new PDF files, opening existing ones, editing text, adding images, cropping images, rotating pages, deleting pages, merging PDF files, and splitting PDF files. The application leverages the power of Python and several libraries, such as `PyPDF2`, `Pillow`, and `reportlab`, to achieve these functionalities.

By working on this project, we gained valuable insights into file handling, GUI development, PDF manipulation, and the overall implementation of an application in Python. We also improved our understanding of various operating system concepts, including file systems, process management, and user interfaces.



## Technologies Used

The following technologies were used to develop the PDF Text Editor:

- Programming Language: Python
- GUI Framework: Tkinter
- PDF Manipulation: PyPDF2, reportlab
- Image Processing: Pillow

## Features

- **Create a File**: Users can create a new PDF file.
- **Open File**: Users can open an existing PDF file.
- **Save File**: Users can save the current PDF file.
- **Add Text**: Users can add text to the PDF file.
- **Add Image**: Users can add an image to the PDF file.
- **Crop Image**: Users can crop an image and add it to the PDF file.
- **Rotate Pages**: Users can rotate the pages of the PDF file.
- **Delete Page**: Users can delete a specific page from the PDF file.
- **Keyboard Shortcuts**: Users can use keyboard shortcuts for copy, paste, and cut operations.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/ilyshoaib/PdftextEditor.git
   ```

2. Change to the project directory:

   ```bash
   cd PdftextEditor
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the application using the following command:

```bash
python3 text-editor.py
```

Once the application is launched, you can use the graphical user interface (GUI) to perform various operations. Here's a brief overview of the available options:

- Click on the "Create a File" button to create a new PDF file.
- Click on the "Open" button to open an existing PDF file.
- Click on the "Save" button to save the current PDF file.
- Click on the "Add Text" button to add text to the PDF file.
- Click on the "Add Image" button to add an image to the PDF file.
- Click on the "Crop Image" button to crop an image and add it to the PDF file.
- Click on the "Rotate" button to rotate the pages of the PDF file.
- Click on the "Delete Page" button to delete a specific page from the PDF file.

## Dependencies

The application requires the following dependencies:

- `tkinter`: This library provides the GUI framework for the application.
- `PyPDF2`: It is used for reading, writing, and manipulating PDF files.
- `reportlab`: It is used for adding text and images to the PDF pages.
- `Pillow`: It is used for image processing and manipulation.
- `io`: It is a core module in Python that provides functionality for working with streams and file-like objects.
- `os`: It is a module in Python that provides functions for interacting with the operating system.

You can install the required dependencies using the following command:

```bash
pip install -r requirements.txt
```

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to create an issue or submit a pull request.


## Project by

Shoaib Ahmad,
Ahmed Mehmood,
Furqan Rafique
