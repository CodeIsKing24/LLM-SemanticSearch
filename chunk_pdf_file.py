# Sample code.. Needs to be refined for Phase-4
import PyPDF2
import os

def pdf_to_txt(pdf_path, output_dir):
    """Reads a PDF file and writes its content into multiple TXT files.

    Args:
        pdf_path (str): Path to the PDF file.
        output_dir (str): Path to the output directory.
    """

    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        num_pages = len(pdf_reader.pages)

        for page_num in range(num_pages):
            page  = pdf_reader.pages[page_num]
            text = page.extract_text()  


            output_filename = f"page_{page_num + 1}.txt"
            output_path = os.path.join(output_dir, output_filename)

            with open(output_path, 'w', encoding='utf-8') as txt_file:
                txt_file.write(text)

# Example usage
pdf_path = "your_pdf_file.pdf"
output_dir = "output_txt_files"

pdf_to_txt(pdf_path, output_dir)