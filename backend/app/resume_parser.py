import PyPDF2

async def extract_text(file):
    pdf_reader = PyPDF2.PdfReader(file.file)
    text = ""
    
    for page in pdf_reader.pages:
        text += page.extract_text()
    
    return text