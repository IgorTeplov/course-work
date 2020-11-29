from utils.enum import *
class Task:

    def __init__(self, document, settings):
        self.document = document
        self.settings = settings

    def run(self):

        def line(text, style="Base", alignment=LEFT):
            line = self.document.add_paragraph(text, style=style)
            line.alignment = alignment

        def line_b(text, style="Base" ,alignment=LEFT):
            line2 = self.document.add_paragraph('', style=style)
            line2.add_run(text).bold = True

        line("")
        line_b("Завдання №2")

        self.sub_task_1()
        self.sub_task_2()
        self.sub_task_3()

        return self.document, self.settings

    def sub_task_1(self):
        def line(text, style="Base", alignment=LEFT):
            line = self.document.add_paragraph(text, style=style)
            line.alignment = alignment

        def line_b(text, base_text="", style="Base" ,alignment=LEFT):
            line2 = self.document.add_paragraph(base_text, style=style)
            line2.add_run(text).bold = True

        line_b("Прямокутний сигнал.", "1)")

    def sub_task_2(self):
        def line(text, style="Base", alignment=LEFT):
            line = self.document.add_paragraph(text, style=style)
            line.alignment = alignment

        def line_b(text, base_text="", style="Base" ,alignment=LEFT):
            line2 = self.document.add_paragraph(base_text, style=style)
            line2.add_run(text).bold = True

        line_b("Трикутний сигнал.", "2)")

    def sub_task_3(self):
        def line(text, style="Base", alignment=LEFT):
            line = self.document.add_paragraph(text, style=style)
            line.alignment = alignment

        def line_b(text, base_text="", style="Base" ,alignment=LEFT):
            line2 = self.document.add_paragraph(base_text, style=style)
            line2.add_run(text).bold = True

        line_b("Двосторонній експоненційний сигнал.", "3)")