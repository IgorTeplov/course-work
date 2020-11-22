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

        def list_number(doc, par, prev=None, level=None, num=True):
            xpath_options = {
                True: {'single': 'count(w:lvl)=1 and ', 'level': 0},
                False: {'single': '', 'level': level},
            }

            def style_xpath(prefer_single=True):
                style = par.style.style_id
                return (
                    'w:abstractNum['
                        '{single}w:lvl[@w:ilvl="{level}"]/w:pStyle[@w:val="{style}"]'
                    ']/@w:abstractNumId'
                ).format(style=style, **xpath_options[prefer_single])

            def type_xpath(prefer_single=True):
                type = 'decimal' if num else 'bullet'
                return (
                    'w:abstractNum['
                        '{single}w:lvl[@w:ilvl="{level}"]/w:numFmt[@w:val="{type}"]'
                    ']/@w:abstractNumId'
                ).format(type=type, **xpath_options[prefer_single])

            def get_abstract_id():
                for fn in (style_xpath, type_xpath):
                    for prefer_single in (True, False):
                        xpath = fn(prefer_single)
                        ids = numbering.xpath(xpath)
                        if ids:
                            return min(int(x) for x in ids)
                return 0

            if (prev is None or
                    prev._p.pPr is None or
                    prev._p.pPr.numPr is None or
                    prev._p.pPr.numPr.numId is None):
                if level is None:
                    level = 0
                numbering = doc.part.numbering_part.numbering_definitions._numbering
                anum = get_abstract_id()
                num = numbering.add_num(anum)
                num.add_lvlOverride(ilvl=level).add_startOverride(1)
                num = num.numId
            else:
                if level is None:
                    level = prev._p.pPr.numPr.ilvl.val
                num = prev._p.pPr.numPr.numId.val
            par._p.get_or_add_pPr().get_or_add_numPr().get_or_add_numId().val = num
            par._p.get_or_add_pPr().get_or_add_numPr().get_or_add_ilvl().val = level

        line_b("Завдання №1")
        p = self.document.add_paragraph('''Отримати представлення сигналу у вигляді ряду Фур'є (в синусно-косинусній формі, дійсній формі та в комплексної формі) з розрахунком перших десяти членів ряду (частоти, амплітуди і фази перших десятигармонік) для кожного з вказаних сигналів.''', style='List Number')
        list_number(self.document, p, level=0)

        p1 = self.document.add_paragraph('''Для кожного з сигналів:''', style='List Number')
        list_number(self.document, p1, p, level=0)

        p2 = self.document.add_paragraph('Представити графік зміни сигналу за часом.', style='List Number')
        list_number(self.document, p2, p1, level=1)
        p2 = self.document.add_paragraph('Представити амплітудну та фазову спектральні діаграми (число гармонік не менше 10-ти).', style='List Number')
        list_number(self.document, p2, p1, level=1)

        line("")

        table = self.document.add_table(rows=3, cols=10, style='BaseTable')
        table.rows[0].cells[0].merge(table.rows[1].cells[0])
        table.rows[0].cells[0].text = "№ Вар."

        table.rows[0].cells[1].merge(table.rows[0].cells[2])
        table.rows[0].cells[2].merge(table.rows[0].cells[3])
        table.rows[0].cells[1].text = "Прямокутний"

        table.rows[0].cells[4].merge(table.rows[0].cells[5])
        table.rows[0].cells[4].text = "Пилкоподібний"

        table.rows[0].cells[6].merge(table.rows[0].cells[7])
        table.rows[0].cells[6].text = "Трикутний"

        table.rows[0].cells[8].merge(table.rows[0].cells[9])
        table.rows[0].cells[8].text = "Меандр"

        table.rows[1].cells[1].text = table.rows[1].cells[4].text = table.rows[1].cells[6].text = table.rows[1].cells[8].text = "f, Гц"
        table.rows[1].cells[2].text = table.rows[1].cells[5].text = table.rows[1].cells[7].text = table.rows[1].cells[9].text = "A, В"
        table.rows[1].cells[3].text = "q"

        table.rows[2].cells[0].text = f"{self.settings['TASK_1']['v']}"

        table.rows[2].cells[1].text = f"{self.settings['TASK_1']['f_pr']}"
        table.rows[2].cells[2].text = f"{self.settings['TASK_1']['a_b_pr']}"
        table.rows[2].cells[3].text = f"{self.settings['TASK_1']['q_pr']}"

        table.rows[2].cells[4].text = f"{self.settings['TASK_1']['f_pl']}"
        table.rows[2].cells[5].text = f"{self.settings['TASK_1']['a_b_pl']}"

        table.rows[2].cells[6].text = f"{self.settings['TASK_1']['f_tr']}"
        table.rows[2].cells[7].text = f"{self.settings['TASK_1']['a_b_tr']}"

        table.rows[2].cells[8].text = f"{self.settings['TASK_1']['f_me']}"
        table.rows[2].cells[9].text = f"{self.settings['TASK_1']['a_b_me']}"

        line("")

        line_b("Завдання №2")

        p = self.document.add_paragraph('''Записати в аналітичному вигляді спектральну функцію для заданого відеоімпульсу, побудувати і представити у вигляді графіків амплітудний і фазовий спектри сигналу.''', style='List Number')
        list_number(self.document, p, level=0)

        p1 = self.document.add_paragraph('''Записати в аналітичному вигляді спектральну функцію для заданого радіоімпульсу, побудувати і представити у вигляді графіку (для позитивних частот) амплітудний спектр сигналу.''', style='List Number')
        list_number(self.document, p1, p, level=0)

        line("")
        line("")

        table = self.document.add_table(rows=3, cols=8, style='BaseTable')
        table.rows[0].cells[0].merge(table.rows[1].cells[0])
        table.rows[0].cells[0].text = "№ Вар."

        table.rows[0].cells[1].merge(table.rows[0].cells[2])
        table.rows[0].cells[1].text = "Прямокутний"

        table.rows[0].cells[3].merge(table.rows[0].cells[4])
        table.rows[0].cells[3].text = "Трикутний"

        table.rows[0].cells[5].merge(table.rows[0].cells[6])
        table.rows[0].cells[5].text = "Двосторонній експоненційний"

        table.rows[0].cells[7].text = "Меандр"

        table.rows[1].cells[1].text = table.rows[1].cells[3].text = table.rows[1].cells[5].text = "A, В"
        table.rows[1].cells[2].text = table.rows[1].cells[4].text = "t, c"
        table.rows[1].cells[6].text = "a, 1/c"
        table.rows[1].cells[7].text = "f0, кГц"

        table.rows[2].cells[0].text = f"{self.settings['TASK_2']['v']}"

        table.rows[2].cells[1].text = f"{self.settings['TASK_2']['a_b_pr']}"
        table.rows[2].cells[2].text = f"{self.settings['TASK_2']['t_pr']}"

        table.rows[2].cells[3].text = f"{self.settings['TASK_2']['a_b_tr']}"
        table.rows[2].cells[4].text = f"{self.settings['TASK_2']['t_tr']}"

        table.rows[2].cells[5].text = f"{self.settings['TASK_2']['a_b_ex']}"
        table.rows[2].cells[6].text = f"{self.settings['TASK_2']['a_ex']}"
        
        table.rows[2].cells[7].text = f"{self.settings['TASK_2']['f_gr']}"

        return self.document, self.settings