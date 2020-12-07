from utils.enum import *

from utils.plot import plot, plots
from utils.img import add_img
from utils.signal import Signal

import numpy as np

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

        # self.sub_task_1()
        # self.sub_task_2()
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

        A = self.settings['TASK_2']['a_b_pr']
        q = 2
        f = eval(self.settings['TASK_2']['f_gr'])

        task_2 = []

        t = eval(self.settings['TASK_2']['t_pr'])
        t_tick = t/100
        t_line = np.arange(-3*t, 3*t, t_tick)
        def st(T):
            if abs(T) <= t/2:
                return A
            return 0

        def st_s(i):
            return int(i*q*t/t_tick)

        s = Signal(st, t_line, [0])
        task_2.append([s.base_time_line, s.base_signal_line])

        w_alt = 18*np.pi*(1/t)
        w_tick_alt = w_alt/1000
        w_line_alt = np.arange(-w_alt,w_alt,w_tick_alt)
        def sw(W):
            return abs(A*t*(np.sin(W*t/2)/(W*t/2)))

        

        def sf(W):
            if A*t*(np.sin(W*t/2)/(W*t/2)) < 0:
                if W >= 0:
                    return -np.pi
                return np.pi

            return 0

        s_alt = Signal(sw, w_line_alt, [0])
        task_2.append([s_alt.base_time_line, s_alt.create_signal_line()])

        s = Signal(sf, w_line_alt, [0])
        task_2.append([s.base_time_line, s.create_signal_line()])


        w = 3*np.pi*f
        w_tick = w/1000
        w_line = np.arange(-w,w,w_tick)
        def sw_alt(W):
            return sw(W-f)/2

        def sw_s(i):
            return int(i*w/w_tick)

        s = Signal(sw_alt, w_line, [sw_s(-0.75), sw_s(0.55)])
        task_2.append([s.base_time_line, s.create_signal_line()])

        plots(task_2)

    def sub_task_2(self):
        def line(text, style="Base", alignment=LEFT):
            line = self.document.add_paragraph(text, style=style)
            line.alignment = alignment

        def line_b(text, base_text="", style="Base" ,alignment=LEFT):
            line2 = self.document.add_paragraph(base_text, style=style)
            line2.add_run(text).bold = True

        line_b("Трикутний сигнал.", "2)")

        A = self.settings['TASK_2']['a_b_tr']
        f = eval(self.settings['TASK_2']['f_gr'])

        task_2 = []

        t = eval(self.settings['TASK_2']['t_tr'])
        t_tick = t/100
        t_line = np.arange(-3*t, 3*t, t_tick)
        def st(T):
            if abs(T) <= t/2:
                return A * (1 - abs(T)/(t/2))
            return 0

        def st_s(i):
            return int(i*t/t_tick)

        s = Signal(st, t_line, [0])
        task_2.append([s.base_time_line, s.base_signal_line])

        w_alt = 24*np.pi*(1/t)
        w_tick_alt = w_alt/1000
        w_line_alt = np.arange(-w_alt,w_alt,w_tick_alt)
        def sw(W):
            return (t/2)*((np.sin(W*t/4)**2)/((W*t/4)**2))

        def sf(W):
            return 0

        s_alt = Signal(sw, w_line_alt, [0])
        task_2.append([s_alt.base_time_line, s_alt.create_signal_line()])

        s = Signal(sf, w_line_alt, [0])
        task_2.append([s.base_time_line, s.create_signal_line()])


        w = 3*np.pi*f
        w_tick = w/1000
        w_line = np.arange(-w,w,w_tick)
        def sw_alt(W):
            return sw(W-f)/2

        def sw_s(i):
            return int(i*w/w_tick)

        s = Signal(sw_alt, w_line, [sw_s(-0.75), sw_s(0.55)])
        task_2.append([s.base_time_line, s.create_signal_line()])

        plots(task_2)

    def sub_task_3(self):
        def line(text, style="Base", alignment=LEFT):
            line = self.document.add_paragraph(text, style=style)
            line.alignment = alignment

        def line_b(text, base_text="", style="Base" ,alignment=LEFT):
            line2 = self.document.add_paragraph(base_text, style=style)
            line2.add_run(text).bold = True

        line_b("Двосторонній експоненційний сигнал.", "3)")

        A = self.settings['TASK_2']['a_b_ex']
        f = eval(self.settings['TASK_2']['f_gr'])
        AT0 = eval(self.settings['TASK_2']['a_ex']) #1700000

        task_2 = []

        t = 1/f
        t_tick = t/100
        t_line = np.arange(-3*t, 3*t, t_tick)
        def st(T):
            if abs(T) > 0:
                return A * np.exp(-AT0*abs(T))
            return 0

        def st_s(i):
            return int(i*t/t_tick)

        s = Signal(st, t_line, [0])
        task_2.append([s.base_time_line, s.base_signal_line])

        w_alt = 24*np.pi*(1/t)
        w_tick_alt = w_alt/1000
        w_line_alt = np.arange(-w_alt,w_alt,w_tick_alt)
        def sw(W):
            return A*2*AT0/(W**2+AT0**2)

        def sf(W):
            return 0

        s_alt = Signal(sw, w_line_alt, [0])
        task_2.append([s_alt.base_time_line, s_alt.create_signal_line()])

        s = Signal(sf, w_line_alt, [0])
        task_2.append([s.base_time_line, s.create_signal_line()])


        w = 12*np.pi*f
        w_tick = w/1000
        w_line = np.arange(-w,w,w_tick)
        def sw_alt(W):
            return sw(W)/2

        def sw_s(i):
            return int(i*w/w_tick)

        class SignalSpec(Signal):
            def strategy(self, x, y):
                if x > y:
                    return x
                return y
        s = SignalSpec(sw_alt, w_line, [sw_s(-0.65), sw_s(0.65)])
        task_2.append([s.base_time_line, s.create_signal_line()])

        plots(task_2)