from .enum import CENTER
from docx.shared import Cm

def add_img(doc, img_path, title):
    doc.add_picture(img_path, width=Cm(14.58))
    title = doc.add_paragraph(title)
    title.alignment = CENTER