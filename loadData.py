import fitz  # PyMuPDF
import argparse
import sys

def load_pdf(file_path):
    try:
        # Load the PDF file
        pdf_document = fitz.open(file_path)
        
        # Get the number of pages in the PDF
        number_of_pages = pdf_document.page_count
        print(f"Number of pages: {number_of_pages}")
        
        # Extract text from all pages
        all_text = ""
        for page_num in range(number_of_pages):
            page = pdf_document.load_page(page_num)
            page_text = page.get_text("text")
            all_text += page_text
            
        return all_text
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
#get input file from terminal
input_file = input()
#send to function to process
pdf_text = load_pdf(input_file)
if pdf_text:
    print(pdf_text)