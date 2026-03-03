from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO

def generate_pdf(cover_letter_text):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer)
    styles = getSampleStyleSheet()
    elements = []

    for line in cover_letter_text.split("\n"):
        elements.append(Paragraph(line, styles["Normal"]))

    doc.build(elements)
    buffer.seek(0)
    return buffer