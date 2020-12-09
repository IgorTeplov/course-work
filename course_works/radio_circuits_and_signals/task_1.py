from utils.enum import *

from utils.plot import plot
from utils.furie import Furie
from utils.signal import Signal
from utils.img import add_img

from math import sqrt, pow
import numpy as np

def round(func):
    def wrap(*args):
        return np.around(func(*args), 3)
    return wrap

def kone(k):
    v = -1
    for _ in range(k):
        v *= -1
    return v

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
        line_b("Завдання №1")

        line("Загальні формули")

        line("Періодичний сигнал s(t) характеризується наступними параметрами:")
        line("f (Гц) - частота зміни сигналу")
        line("T=1/f (с) - період повторення сигналу")
        line("ω=2*π*f (Гц)- кругова частота (інші назви: циклічна частота або кутова частота)")

        line("Синусно-косинусна форма представлення періодичного сигналу рядом Фур’є має наступний вигляд:")
        line("s(t) = a0/2 + Σ(k=0,∞)(ak*cos(k*ω*t)+bk*sin(k*ω*t)")

        line("Дійсна форма представлення періодичного сигналу рядом Фур’є має такий вигляд:")
        line("s(t) = a0/2 + Σ(k=0,∞)Ak*cos(k*ω*t + φk)")

        line("Комплексна форма представлення періодичного сигналу рядом Фур’є має наступний вигляд:")
        line("s(t) = Σ(-∞,∞)Ck*e^(j*k*ω*t)")

        line("Коефіцієнти ряду аk і bk за формулами:")
        line("ak = (2/T)*∫(T/2, -T/2)s(t)*cos(k*ω*t)*dt")
        line("bk = (2/T)*∫(T/2, -T/2)s(t)*sin(k*ω*t)*dt")

        line("Коефіцієнти синусно-косинусної (аk і bk) і дійсної форм (амплітуда Ak та фаза φk) розкладання періодичного сигналу в ряд Фур'є пов'язані таким чином:")
        line("Ak = √(ak^2 + bk^2)")
        line("tg(φ) = -(bk/ak)")

        line("Комплексні коефіцієнти ряду пов'язані з амплітудами Аk , і фазами φk, що фігурують в дійсній записи ряду Фур'є, наступними співвідношеннями:")
        line("Ck = (1/2)*Ak*e^(j*φk)")

        self.sub_task_1()
        self.sub_task_2()
        self.sub_task_3()
        self.sub_task_4()

        return self.document, self.settings

    def sub_task_1(self):
        def line(text, style="Base", alignment=LEFT):
            line = self.document.add_paragraph(text, style=style)
            line.alignment = alignment

        def line_b(text, base_text="", style="Base" ,alignment=LEFT):
            line2 = self.document.add_paragraph(base_text, style=style)
            line2.add_run(text).bold = True

        line_b("Прямокутний сигнал.", "1)")

        # MATH

        k_max = self.settings['TASK_1']['_pr_k_max']
        f = self.settings['TASK_1']['f_pr']
        A = self.settings['TASK_1']['a_b_pr']
        q = self.settings['TASK_1']['q_pr']

        T = 1/f
        t = T/q
        w = np.around(2*np.pi*f, 3)
        a0 = A/q

        ak_ = []
        bk_ = []
        Ak_ = []
        fk_ = []
        Ck_ = []


        def st(T):
            if abs(T) <= t/2:
                return A
            return 0
        t_tick = t/100
        t_line = np.arange(-t, t, t_tick)
        s = Signal(st, t_line, [0])
        plot(s.base_time_line, s.base_signal_line, name="pr_x_y", linewidth = 1, color = 'crimson')


        @round
        def ak(k):
            if k == 0:
                return a0*2
            if k % q == 0:
                return 0
            else:
                return (2*A)/(np.pi*k) * np.sin(np.pi*k/q)

        def bk(k):
            return 0

        furie = Furie(a0, ak, bk, t/2, T, self.settings['TASK_1']['_pr_k_max_graph'])

        def Ck(k):
            k = abs(k)
            if k == 0:
                return (furie.Ak(k), 0)
            if k % q == 0:
                return (0,0)
            else:
                return (furie.Ak(k)/2, np.around(k*w*t, 3))

        @round
        def fk(k):
            k_o = k
            k = abs(k)
            if furie.ak(k) <= 0:
                v = np.pi
                if k_o < 0:
                    return v*-1
                return v
            else:
                try:
                    v = np.arctan(-(furie.bk(k)/furie.ak(k)))
                    if k_o < 0:
                        return v * -1
                    return v
                except ZeroDivisionError:
                    return None

        for k in range(0, k_max+1):
            ak_.append(furie.ak(k))
            bk_.append(furie.bk(k))
            Ak_.append(furie.Ak(k))
        for k in range((-k_max//2), (k_max//2)+1):
            Ck_.append(Ck(k))
            fk_.append(fk(k))

        print("Прямокутний сигнал.")
        print('ak: ', ak_)
        print('bk: ', bk_)
        print('Ak: ', Ak_)
        print('Ck: ', Ck_)
        print('fk: ', fk_)

        # PLOTS

        pr_min = self.settings['TASK_1']['_pr_t_min']
        pr_max = self.settings['TASK_1']['_pr_t_max']
        pr_step = self.settings['TASK_1']['_pr_t_steep']
        pr_pos = self.settings['TASK_1']['_pr_t_pos']

        x = np.arange(pr_min,pr_max,pr_step)
        y = [furie.f(t, only_pos=pr_pos) for t in x]
        x_k_11 = range(0, k_max+1)
        x_k_5 = range((-k_max//2), (k_max//2)+1)

        # plot(x, y, name="pr_x_y", linewidth = 1, color = 'crimson')
        plot(x_k_11, Ak_, 'ro', name="pr_Ak", linewidth = 1, color = 'crimson')
        plot(x_k_5, fk_, 'ro', name="pr_fk", linewidth = 1, color = 'crimson')

        # TEXT

        line(f"k = {k_max}; f = {f} (Гц); A = {A} (В); q = {q}; τ = T/q = {t} (с); ω = {w} (Гц)")
        line(f"a0/2 = A/q = {a0} (В)")

        line("Оскільки прямокутний сигнал є парною функцією, то в синусно-косинусній формі ряду Фур'є синусна складова буде дорівнювати нулю (bk = 0).")
        line("")
        line("Для прямокутного сигналу ak має формулу:")
        line("ak = (2*A)/(π*k) * sin(π*k/q)")
        line(f"Таблиця розрахунків ak та Ak для прямокутного сигналу при k 0...{k_max}")
        table = self.document.add_table(rows=1, cols=3, style='BaseTable')
        hdr_cells = table.rows[0].cells
        hdr_cells[0].text = 'k'
        hdr_cells[1].text = 'ak'
        hdr_cells[2].text = 'Ak'
        for k in x_k_11:
            row_cells = table.add_row().cells
            row_cells[0].text = str(k)
            row_cells[1].text = str(ak_[k])
            row_cells[2].text = str(Ak_[k])

        line("")
        line(f"Таблиця розрахунків Ck та φk для прямокутного сигналу при k {-k_max//2}...{k_max//2}")
        table = self.document.add_table(rows=1, cols=3, style='BaseTable')
        hdr_cells = table.rows[0].cells
        hdr_cells[0].text = 'k'
        hdr_cells[1].text = 'Ck'
        hdr_cells[2].text = 'φk'
        c = 0
        for k in x_k_5:
            row_cells = table.add_row().cells
            row_cells[0].text = str(k)
            row_cells[1].text = str(f"{Ck_[c][0]}*e^(j*{Ck_[c][1]})")
            row_cells[2].text = str(fk_[c])
            c += 1
        line("")

        add_img(self.document, 'img/pr_x_y.png', "Прямокутный сигнал")

        add_img(self.document, 'img/pr_Ak.png', "Амплітудна спектральна діаграма прямокутного сигналу")

        add_img(self.document, 'img/pr_fk.png', "Фазова спектральна діаграма прямокутного сигналу")

        furie_sin_cos = f's(t) = {a0*2}/2'
        for k in range(1, k_max+1):
            furie_sin_cos += f" + {ak_[k]}*cos({np.around(k*w, 3)}*t)"
        furie_diysn = f's(t) = {a0*2}/2'
        for k in range(1, k_max+1):
            furie_diysn += f" + {Ak_[k]}*cos({np.around(k*w, 3)}*t + {fk_[k]})"
        furie_comlex = f's(t) = {Ck_[0][0]}*e^(j*{Ck_[0][1]}*t)'
        for ck in Ck_[1:]:
            furie_comlex += f" + {ck[0]}*e^(j*{ck[1]}*t)"

        line("")
        line("Синусно-косинусна форма ппрямокутного сигналу:")
        line(furie_sin_cos)
        line("Дійсна форма прямокутного сигналу:")
        line(furie_diysn)
        line("Комплексна форма прямокутного сигналу:")
        line(furie_comlex)
    def sub_task_2(self):
        def line(text, style="Base", alignment=LEFT):
            line = self.document.add_paragraph(text, style=style)
            line.alignment = alignment

        def line_b(text, base_text="", style="Base" ,alignment=LEFT):
            line2 = self.document.add_paragraph(base_text, style=style)
            line2.add_run(text).bold = True

        line_b("Пилкоподібний сигнал.", "2)")

        # MATH

        k_max = self.settings['TASK_1']['_pl_k_max']
        f = self.settings['TASK_1']['f_pl']
        A = self.settings['TASK_1']['a_b_pl']

        T = 1/f
        t = T
        w = np.around(2*np.pi*f, 3)
        a0 = 0

        ak_ = []
        bk_ = []
        Ak_ = []
        fk_ = []
        Ck_ = []

        # VIEW

        furie_sin_cos = ''
        furie_diysn = ''
        furie_comlex = ''

        def ak(k):
            return 0

        @round
        def bk(k):
            if k == 0:
                return 0

            return (2*A/np.pi)*(kone(k)/k)

        furie = Furie(a0, ak, bk, t/4, T, self.settings['TASK_1']['_pl_k_max_graph'])

        def Ck(k):
            k = abs(k)
            if k == 0:
                return (furie.Ak(k), 0)
            return (furie.Ak(k)/2, np.around((k*w/2)*t), 3)

        @round
        def fk(k):
            k_o = k
            k = abs(k)
            v = np.pi/2
            if k == 0:
                return 0
            if furie.bk(k) >= 0:
                if k_o < 0:
                    return v*-1
                return v
            else:
                if k_o < 0:
                    return v*-1*-1
                return v*-1

        for k in range(0, k_max+1):
            ak_.append(furie.ak(k))
            bk_.append(furie.bk(k))
            Ak_.append(furie.Ak(k))
        for k in range((-k_max//2), (k_max//2)+1):
            Ck_.append(Ck(k))
            fk_.append(fk(k))

        print("Пилкоподібний сигнал.")
        print('ak: ', ak_)
        print('bk: ', bk_)
        print('Ak: ', Ak_)
        print('Ck: ', Ck_)
        print('fk: ', fk_)

        # PLOT 

        pl_min = self.settings['TASK_1']['_pl_t_min']
        pl_max = self.settings['TASK_1']['_pl_t_max']
        pl_step = self.settings['TASK_1']['_pl_t_steep']
        pl_pos = self.settings['TASK_1']['_pl_t_pos']

        x = np.arange(pl_min,pl_max,pl_step)
        y = [furie.f(t, only_pos=pl_pos) for t in x]
        x_k_11 = range(0, k_max+1)
        x_k_5 = range((-k_max//2), (k_max//2)+1)

        plot(x, y, name="pl_x_y", linewidth = 1, color = 'crimson')
        plot(x_k_11, Ak_, 'ro', name="pl_Ak", linewidth = 1, color = 'crimson')
        plot(x_k_5, fk_, 'ro', name="pl_fk", linewidth = 1, color = 'crimson')

        line(f"k = {k_max}; f = {f} (Гц); A = {A} (В); τ = T = {t} (с); ω = {w} (Гц)")
        line(f"a0 = {a0} (В)")

        line("Оскільки пилкоподібний сигнал є непарною функцією, то в синусно-косинусній формі ряду Фур'є косинусна складова буде дорівнювати нулю (ak = 0).")
        line("")
        line("Для пилкоподібного сигналу ak має формулу:")
        line("bk = (2*A/π)*((-1^k)/k)")

        line(f"Таблиця розрахунків bk та Ak для пилкоподібного сигналу при k 0...{k_max}")
        table = self.document.add_table(rows=1, cols=3, style='BaseTable')
        hdr_cells = table.rows[0].cells
        hdr_cells[0].text = 'k'
        hdr_cells[1].text = 'bk'
        hdr_cells[2].text = 'Ak'
        for k in x_k_11:
            row_cells = table.add_row().cells
            row_cells[0].text = str(k)
            row_cells[1].text = str(bk_[k])
            row_cells[2].text = str(Ak_[k])

        line("")
        line(f"Таблиця розрахунків Ck та φk для пилкоподібного сигналу при k {-k_max//2}...{k_max//2}")
        table = self.document.add_table(rows=1, cols=3, style='BaseTable')
        hdr_cells = table.rows[0].cells
        hdr_cells[0].text = 'k'
        hdr_cells[1].text = 'Ck'
        hdr_cells[2].text = 'φk'
        c = 0
        for k in x_k_5:
            row_cells = table.add_row().cells
            row_cells[0].text = str(k)
            row_cells[1].text = str(f"{Ck_[c][0]}*e^(j*{Ck_[c][1]})")
            row_cells[2].text = str(fk_[c])
            c += 1
        line("")

        add_img(self.document, 'img/pl_x_y.png', "Пилкоподібний сигнал")

        add_img(self.document, 'img/pl_Ak.png', "Амплітудна спектральна діаграма пилкоподібного сигналу")

        add_img(self.document, 'img/pl_fk.png', "Фазова спектральна діаграма пилкоподібного сигналу")

        furie_sin_cos = f's(t) = {a0}'
        for k in range(1, k_max+1):
            furie_sin_cos += f" + {bk_[k]}*sin({np.around(k*w, 3)}*t)"
        furie_diysn = f's(t) = {a0}'
        for k in range(1, k_max+1):
            furie_diysn += f" + {Ak_[k]}*cos({np.around(k*w, 3)}*t + {fk_[k]})"
        furie_comlex = f's(t) = {Ck_[0][0]}*e^(j*{Ck_[0][1]}*t)'
        for ck in Ck_[1:]:
            furie_comlex += f" + {ck[0]}*e^(j*{ck[1]}*t)"

        line("")
        line("Синусно-косинусна форма пилкоподібного сигналу:")
        line(furie_sin_cos)
        line("Дійсна форма пилкоподібного сигналу:")
        line(furie_diysn)
        line("Комплексна форма пилкоподібного сигналу:")
        line(furie_comlex)

    def sub_task_3(self):
        def line(text, style="Base", alignment=LEFT):
            line = self.document.add_paragraph(text, style=style)
            line.alignment = alignment

        def line_b(text, base_text="", style="Base" ,alignment=LEFT):
            line2 = self.document.add_paragraph(base_text, style=style)
            line2.add_run(text).bold = True

        line_b("Трикутний сигнал.", "3)")

        # MATH

        k_max = self.settings['TASK_1']['_tr_k_max']
        f = self.settings['TASK_1']['f_tr']
        A = self.settings['TASK_1']['a_b_tr']

        T = 1/f
        t = T
        w = np.around(2*np.pi*f, 3)
        a0 = 0

        ak_ = []
        bk_ = []
        Ak_ = []
        fk_ = []
        Ck_ = []

        def st(T):
            if abs(T) <= t/2:
                return A * (1 - abs(T)/(t/2))
            return 0
        t_tick = t/100
        t_line = np.arange(-t, t, t_tick)
        s = Signal(st, t_line, [0])
        plot(s.base_time_line, s.base_signal_line, name="tr_x_y", linewidth = 1, color = 'crimson')

        # VIEW

        furie_sin_cos = ''
        furie_diysn = ''
        furie_comlex = ''

        @round
        def ak(k):
            if k == 0:
                return 0
            if k % 2 == 0:
                return 0
            else:
                v = (4*A/((np.pi*k)**2))*(1-pow(-1, k))
                return v

        def bk(k):
            return 0

        furie = Furie(a0, ak, bk, t/2, T, self.settings['TASK_1']['_tr_k_max_graph'])

        def Ck(k):
            k = abs(k)
            if k == 0:
                return (furie.Ak(k), 0)
            if k % 2 == 0:
                return (0,0)
            else:
                return (furie.Ak(k)/2, np.around(k*w*t, 3))

        def fk(k):
            return 0

        for k in range(0, k_max+1):
            ak_.append(furie.ak(k))
            bk_.append(furie.bk(k))
            Ak_.append(furie.Ak(k))
        for k in range((-k_max//2), (k_max//2)+1):
            Ck_.append(Ck(k))
            fk_.append(fk(k))

        print("Трикутний сигнал.")
        print('ak: ', ak_)
        print('bk: ', bk_)
        print('Ak: ', Ak_)
        print('Ck: ', Ck_)
        print('fk: ', fk_)

        # PLOT 

        tr_min = self.settings['TASK_1']['_tr_t_min']
        tr_max = self.settings['TASK_1']['_tr_t_max']
        tr_step = self.settings['TASK_1']['_tr_t_steep']
        tr_pos = self.settings['TASK_1']['_tr_t_pos']

        x = np.arange(tr_min,tr_max,tr_step)
        y = [furie.f(t, only_pos=tr_pos) for t in x]
        x_k_11 = range(0, k_max+1)
        x_k_5 = range((-k_max//2), (k_max//2)+1)

        # plot(x, y, name="tr_x_y", linewidth = 1, color = 'crimson')
        plot(x_k_11, Ak_, 'ro', name="tr_Ak", linewidth = 1, color = 'crimson')
        plot(x_k_5, fk_, 'ro', name="tr_fk", linewidth = 1, color = 'crimson')

        # TEXT

        line(f"k = {k_max}; f = {f} (Гц); A = {A} (В); τ = T = {t} (с); ω = {w} (Гц)")
        line(f"a0/2 = {a0} (В)")

        line("Оскільки трикутний сигнал є парною функцією, то в синусно-косинусній формі ряду Фур'є синусна складова буде дорівнювати нулю (bk = 0).")
        line("")
        line("Для трикутного сигналу ak має формулу:")
        line("ak = (4*A)/((π*k)^2) * (1-(-1^k)")
        # (4*A/(np.pi*k**2))*(1-pow(-1, k))
        line(f"Таблиця розрахунків ak та Ak для трикутного сигналу при k 0...{k_max}")
        table = self.document.add_table(rows=1, cols=3, style='BaseTable')
        hdr_cells = table.rows[0].cells
        hdr_cells[0].text = 'k'
        hdr_cells[1].text = 'ak'
        hdr_cells[2].text = 'Ak'
        for k in x_k_11:
            row_cells = table.add_row().cells
            row_cells[0].text = str(k)
            row_cells[1].text = str(ak_[k])
            row_cells[2].text = str(Ak_[k])

        line("")
        line(f"Таблиця розрахунків Ck та φk для трикутного сигналу при k {-k_max//2}...{k_max//2}")
        table = self.document.add_table(rows=1, cols=3, style='BaseTable')
        hdr_cells = table.rows[0].cells
        hdr_cells[0].text = 'k'
        hdr_cells[1].text = 'Ck'
        hdr_cells[2].text = 'φk'
        c = 0
        for k in x_k_5:
            row_cells = table.add_row().cells
            row_cells[0].text = str(k)
            row_cells[1].text = str(f"{Ck_[c][0]}*e^(j*{Ck_[c][1]})")
            row_cells[2].text = str(fk_[c])
            c += 1
        line("")

        add_img(self.document, 'img/tr_x_y.png', "Трикутний сигнал")

        add_img(self.document, 'img/tr_Ak.png', "Амплітудна спектральна діаграма трикутного сигналу")

        add_img(self.document, 'img/tr_fk.png', "Фазова спектральна діаграма трикутного сигналу")

        furie_sin_cos = f's(t) = {a0*2}/2'
        for k in range(1, k_max+1):
            furie_sin_cos += f" + {ak_[k]}*cos({np.around(k*w, 3)}*t)"
        furie_diysn = f's(t) = {a0*2}/2'
        for k in range(1, k_max+1):
            furie_diysn += f" + {Ak_[k]}*cos({np.around(k*w, 3)}*t + {fk_[k]})"
        furie_comlex = f's(t) = {Ck_[0][0]}*e^(j*{Ck_[0][1]}*t)'
        for ck in Ck_[1:]:
            furie_comlex += f" + {ck[0]}*e^(j*{ck[1]}*t)"

        line("")
        line("Синусно-косинусна форма трикутного сигналу:")
        line(furie_sin_cos)
        line("Дійсна форма трикутного сигналу:")
        line(furie_diysn)
        line("Комплексна форма трикутного сигналу:")
        line(furie_comlex)
    def sub_task_4(self):
        def line(text, style="Base", alignment=LEFT):
            line = self.document.add_paragraph(text, style=style)
            line.alignment = alignment

        def line_b(text, base_text="", style="Base" ,alignment=LEFT):
            line2 = self.document.add_paragraph(base_text, style=style)
            line2.add_run(text).bold = True

        line_b("Меандр. сигнал.", "4)")

        # MATH

        k_max = self.settings['TASK_1']['_me_k_max']
        f = self.settings['TASK_1']['f_me']
        A = self.settings['TASK_1']['a_b_me']
        q = 2

        T = 1/f
        t = T/q
        w = np.around(2*np.pi*f, 3)

        a0 = A/q

        ak_ = []
        bk_ = []
        Ak_ = []
        fk_ = []
        Ck_ = []

        def st(T):
            if abs(T) <= t/2:
                return A
            return 0
        t_tick = t/100
        t_line = np.arange(-t, t, t_tick)
        s = Signal(st, t_line, [0])
        plot(s.base_time_line, s.base_signal_line, name="me_x_y", linewidth = 1, color = 'crimson')

        #VIEW

        furie_sin_cos = f'{a0}/2'
        furie_diysn = f'{a0}/2'
        furie_comlex = ''

        @round
        def ak(k):
            if k == 0:
                return a0
            if k % q == 0:
                return 0
            else:
                return (2*A)/(np.pi*k) * np.sin((np.pi*k)/q)

        def bk(k):
            return 0

        furie = Furie(a0, ak, bk, t/2, T, self.settings['TASK_1']['_me_k_max_graph'])

        def Ck(k):
            k = abs(k)
            if k == 0:
                return (furie.Ak(k), 0)
            if k % q == 0:
                return (0,0)
            else:
                return (furie.Ak(k)/2, np.around(k*w*t, 3))

        @round
        def fk(k):
            k_o = k
            k = abs(k)
            v = np.pi
            if k == 0:
                return 0
            if k % 4 == 0:
                if k_o < 0:
                    return v*-1
                return v
            else:
                if k % 2 == 0:
                    return 0
                elif k % 2 == 1 and k % 4 == 3:
                    if k_o < 0:
                        return v*-1
                    return v
                return 0

        for k in range(0, k_max+1):
            ak_.append(furie.ak(k))
            bk_.append(furie.bk(k))
            Ak_.append(furie.Ak(k))
        for k in range((-k_max//2), (k_max//2)+1):
            Ck_.append(Ck(k))
            fk_.append(fk(k))

        print("Меандр. сигнал.")
        print('ak: ', ak_)
        print('bk: ', bk_)
        print('Ak: ', Ak_)
        print('Ck: ', Ck_)
        print('fk: ', fk_)

        # PLOT

        me_min = self.settings['TASK_1']['_me_t_min']
        me_max = self.settings['TASK_1']['_me_t_max']
        me_step = self.settings['TASK_1']['_me_t_steep']
        me_pos = self.settings['TASK_1']['_me_t_pos']

        x = np.arange(me_min,me_max,me_step)
        y = [furie.f(t, only_pos=me_pos) for t in x]
        x_k_11 = range(0, k_max+1)
        x_k_5 = range((-k_max//2), (k_max//2)+1)

        # plot(x, y, name="me_x_y", linewidth = 1, color = 'crimson')
        plot(x_k_11, Ak_, 'ro', name="me_Ak", linewidth = 1, color = 'crimson')
        plot(x_k_5, fk_, 'ro', name="me_fk", linewidth = 1, color = 'crimson')

        # TEXT

        line(f"k = {k_max}; f = {f} (Гц); A = {A} (В); q = {q}; τ = T/q = {t} (с); ω = {w} (Гц)")
        line(f"a0/2 = A/q = {a0} (В)")

        line("Оскільки меандр сигнал є парною функцією, то в синусно-косинусній формі ряду Фур'є синусна складова буде дорівнювати нулю (bk = 0).")
        line("")
        line("Для меандр сигналу ak має формулу:")
        line("ak = (2*A)/(π*k) * sin((π*k)/q)")
        line(f"Таблиця розрахунків ak та Ak для меандр сигналу при k 0...{k_max}")
        table = self.document.add_table(rows=1, cols=3, style='BaseTable')
        hdr_cells = table.rows[0].cells
        hdr_cells[0].text = 'k'
        hdr_cells[1].text = 'ak'
        hdr_cells[2].text = 'Ak'
        for k in x_k_11:
            row_cells = table.add_row().cells
            row_cells[0].text = str(k)
            row_cells[1].text = str(ak_[k])
            row_cells[2].text = str(Ak_[k])

        line("")
        line(f"Таблиця розрахунків Ck та φk для меандр сигналу при k {-k_max//2}...{k_max//2}")
        table = self.document.add_table(rows=1, cols=3, style='BaseTable')
        hdr_cells = table.rows[0].cells
        hdr_cells[0].text = 'k'
        hdr_cells[1].text = 'Ck'
        hdr_cells[2].text = 'φk'
        c = 0
        for k in x_k_5:
            row_cells = table.add_row().cells
            row_cells[0].text = str(k)
            row_cells[1].text = str(f"{Ck_[c][0]}*e^(j*{Ck_[c][1]})")
            row_cells[2].text = str(fk_[c])
            c += 1
        line("")

        add_img(self.document, 'img/me_x_y.png', "Меандр сигнал")

        add_img(self.document, 'img/me_Ak.png', "Амплітудна спектральна діаграма меандр сигналу")

        add_img(self.document, 'img/me_fk.png', "Фазова спектральна діаграма меандр сигналу")

        furie_sin_cos = f's(t) = {a0*2}/2'
        for k in range(1, k_max+1):
            furie_sin_cos += f" + {ak_[k]}*cos({np.around(k*w, 3)}*t)"
        furie_diysn = f's(t) = {a0*2}/2'
        for k in range(1, k_max+1):
            furie_diysn += f" + {Ak_[k]}*cos({np.around(k*w, 3)}*t + {fk_[k]})"
        furie_comlex = f's(t) = {Ck_[0][0]}*e^(j*{Ck_[0][1]}*t)'
        for ck in Ck_[1:]:
            furie_comlex += f" + {ck[0]}*e^(j*{ck[1]}*t)"

        line("")
        line("Синусно-косинусна форма меандр сигналу:")
        line(furie_sin_cos)
        line("Дійсна форма меандр сигналу:")
        line(furie_diysn)
        line("Комплексна форма меандр сигналу:")
        line(furie_comlex)