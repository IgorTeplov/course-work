from utils.enum import *
class Task:

    def __init__(self, document, settings):
        self.document = document
        self.settings = settings

    def run(self): 


        def line(text, style="Base", alignment=LEFT):
            line = self.document.add_paragraph(text, style=style)
            line.alignment = alignment

        def line_c(text, style="Base"):
            line(text, style, CENTER)

        def line_r(text, style="Base"):
            line(text, style, RIGHT)

        line_c('''МІНІСТЕРСТВО ОСВІТИ І НАУКИ УКРАЇНИ
ДНІПРОВСЬКИЙ НАЦІОНАЛЬНИЙ УНІВЕРСИТЕТ
ФІЗИКО-ТЕХНІЧНИЙ ФАКУЛЬТЕТ
КАФЕДРА РАДІОЕЛЕКТРОННОЇ АВТОМАТИКИ''')
        line_c("")
        line_c("")
        line_c("КУРСОВА РОБОТА")
        line_c("З дисципліни «Радіотехнічні кола та сигнали»")
        line_c("НА ТЕМУ:")
        line_c("Спектральний аналіз періодичних та неперіодичних детермінованих безперервних сигналів")
        line_c("")
        line_c("")
        line_r("Виконавець:")
        line_r(f"Студент групи {self.settings['GROUP']}")
        line_r(f"{self.settings['NAME']}")
        line_c("")
        line_r("Комісія з прийому курсової роботи:")
        line_r("Петренко О.М.")
        line_r("Мазуренко В.Б.")
        line_r("Селіванов Ю.М.")
        line_c("Дніпро 2020")

        return self.document, self.settings
