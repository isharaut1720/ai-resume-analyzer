
from PyPDF2 import PdfReader
from fastapi import HTTPException


async def extract_text(file):

    try:
        pdf_reader = PdfReader(file.file)

        if len(pdf_reader.pages) == 0:
            raise HTTPException(
                status_code=400,
                detail="The uploaded PDF is empty."
            )

        text = ""

        for page in pdf_reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        if not text.strip():
            raise HTTPException(
                status_code=400,
                detail="Could not extract text. Please upload a text-based PDF."
            )

        return text.strip()

    except HTTPException:
        raise

    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Unable to read this PDF. Please upload a valid PDF."
        )
