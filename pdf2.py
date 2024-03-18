from PyPDF2 import PdfWriter, PdfReader

def split_pdf(input_pdf_path):
    input_pdf = PdfReader(open(input_pdf_path, "rb"))
    doc_name = input_pdf_path.split(".")[0]  # Extract the document name (without extension)

    for i in range(len(input_pdf.pages)):
        output = PdfWriter()
        output.add_page(input_pdf.pages[i])

        # Save each page as a separate PDF
        output_pdf_path = f"{doc_name}-{i + 1}hk.pdf"
        with open(output_pdf_path, "wb") as output_stream:
            output.write(output_stream)
            print(f"Saved {output_pdf_path}")

# Example usage:
input_pdf_path = ".\hk.pdf"  # Replace with your actual PDF file path
split_pdf(input_pdf_path)
