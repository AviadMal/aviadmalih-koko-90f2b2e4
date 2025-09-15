import os
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Word Document Converted to PDF', border=False, ln=True, align='C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', align='C')

def convert_word_to_pdf(word_file, output_pdf):
    pdf = PDF()
    pdf.add_page()
    pdf.set_font('Arial', '', 12)
    with open(word_file, 'r') as file:
        for line in file:
            pdf.multi_cell(0, 10, line)
    pdf.output(output_pdf)

if __name__ == '__main__':
    input_word = 'example_word.txt'  # Input text file path
    output_pdf_file = 'output_document.pdf'  # Desired output PDF path
    if os.path.exists(input_word):
        convert_word_to_pdf(input_word, output_pdf_file)
        print(f'Successfully converted {input_word} to {output_pdf_file}.')
    else:
        print(f'The file {input_word} does not exist.')