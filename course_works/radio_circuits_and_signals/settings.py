from docx.shared import Pt

from docx.enum.style import WD_STYLE_TYPE
class Task:

    def __init__(self, document, settings):
        self.document = document
        self.settings = settings

    def run(self):

        obj_styles = self.document.styles
        obj_charstyle = obj_styles.add_style('Base', WD_STYLE_TYPE.PARAGRAPH)
        obj_font = obj_charstyle.font
        obj_font.size = Pt(16)
        obj_font.name = 'Times New Roman'

        return self.document, self.settings