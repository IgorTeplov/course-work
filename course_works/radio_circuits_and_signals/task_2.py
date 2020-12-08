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

        line("Загальні формули")

        line("Гармонійна функція:")
        line("g(t) = cos(ω0*t+φ0)")

        line("Перемножена основна функція на гармонійну:")
        line("s1(t) = s(t)*cos(2*π*f)")
        line("Спектральна функция для нового сигналу (основна функція D(ω) для кожного типу сигналу описується окремо):")
        line("D1(ω) = (1/2)*D(ω-2*π*f)+(1/2)*D(ω+2*π*f)")

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

        A = self.settings['TASK_2']['a_b_pr']
        q = 2
        f = eval(self.settings['TASK_2']['f_gr'])
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
        plot(s.base_time_line, s.base_signal_line, name="2pr", linewidth = 1, color = 'crimson')

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
        plot(s_alt.base_time_line, s_alt.create_signal_line(), name="2pr_w", linewidth = 1, color = 'crimson')

        s = Signal(sf, w_line_alt, [0])
        plot(s.base_time_line, s.create_signal_line(), name="2pr_f", linewidth = 1, color = 'crimson')

        w = 3*np.pi*f
        w_tick = w/1000
        w_line = np.arange(-w,w,w_tick)
        def sw_alt(W):
            return sw(W-f)/2

        def sw_s(i):
            return int(i*w/w_tick)

        s = Signal(sw_alt, w_line, [sw_s(-0.75), sw_s(0.55)])
        plot(s.base_time_line, s.create_signal_line(), name="2pr_line", linewidth = 1, color = 'crimson')

        add_img(self.document, 'img/2pr.png', 'Графік прямокутного сигналу s(t)')
        line("Спектральна функція прямокутного імпульсу:")
        line("D(ω) = A*τ*(sin(ω*τ/2))/(ω*τ/2)")
        line("Представимо у вигляді графіків амплітудний і фазовий спектри сигналу")
        add_img(self.document, 'img/2pr_w.png', 'Амплітудний спектр прямокутного сигналу')
        add_img(self.document, 'img/2pr_f.png', 'Фазовий спектр прямокутного сигналу')
        line("Помножимо сигнал s(t) на гармонійну функцію (s1(t)), а потім знайдемо спектральну функцію D1(ω) нового сигналу s1(t)")
        add_img(self.document, 'img/2pr_line.png', 'Амплітудний спектр прямокутного радіоімпульсу')

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
        plot(s.base_time_line, s.base_signal_line, name="2tr", linewidth = 1, color = 'crimson')

        w_alt = 24*np.pi*(1/t)
        w_tick_alt = w_alt/1000
        w_line_alt = np.arange(-w_alt,w_alt,w_tick_alt)
        def sw(W):
            return (t/2)*((np.sin(W*t/4)**2)/((W*t/4)**2))

        def sf(W):
            return 0

        s_alt = Signal(sw, w_line_alt, [0])
        plot(s_alt.base_time_line, s_alt.create_signal_line(), name="2tr_w", linewidth = 1, color = 'crimson')

        s = Signal(sf, w_line_alt, [0])
        plot(s.base_time_line, s.create_signal_line(), name="2tr_f", linewidth = 1, color = 'crimson')

        w = 3*np.pi*f
        w_tick = w/1000
        w_line = np.arange(-w,w,w_tick)
        def sw_alt(W):
            return sw(W-f)/2

        def sw_s(i):
            return int(i*w/w_tick)

        s = Signal(sw_alt, w_line, [sw_s(-0.75), sw_s(0.55)])
        plot(s.base_time_line, s.create_signal_line(), name="2tr_line", linewidth = 1, color = 'crimson')

        add_img(self.document, 'img/2tr.png', 'Графік трикутного сигналу s(t)')
        line("Спектральна функція трикутного імпульсу:")
        line("D(ω) = τ/2 * (sin(ω*τ/4)^2/(ω*τ/4)^2)")
        line("Представимо у вигляді графіків амплітудний і фазовий спектри сигналу")
        add_img(self.document, 'img/2tr_w.png', 'Амплітудний спектр трикутного сигналу')
        add_img(self.document, 'img/2tr_f.png', 'Фазовий спектр трикутного сигналу')
        line("Помножимо сигнал s(t) на гармонійну функцію (s1(t)), а потім знайдемо спектральну функцію D1(ω) нового сигналу s1(t)")
        add_img(self.document, 'img/2tr_line.png', 'Амплітудний спектр трикутного радіоімпульсу')

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
        plot(s.base_time_line, s.base_signal_line, name="2ex", linewidth = 1, color = 'crimson')

        w_alt = 24*np.pi*(1/t)
        w_tick_alt = w_alt/1000
        w_line_alt = np.arange(-w_alt,w_alt,w_tick_alt)
        def sw(W):
            return A*2*AT0/(W**2+AT0**2)

        def sf(W):
            return 0

        s_alt = Signal(sw, w_line_alt, [0])
        plot(s_alt.base_time_line, s_alt.create_signal_line(), name="2ex_w", linewidth = 1, color = 'crimson')

        s = Signal(sf, w_line_alt, [0])
        plot(s.base_time_line, s.create_signal_line(), name="2ex_f", linewidth = 1, color = 'crimson')

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
        plot(s.base_time_line, s.create_signal_line(), name="2ex_line", linewidth = 1, color = 'crimson')

        add_img(self.document, 'img/2ex.png', 'Графік двостороннього експоненційного сигналу s(t)')
        line("Спектральна функція двостороннього експоненційного імпульсу:")
        line("D(ω) = A*2*a/(a^2 + ω^2)")
        line("Представимо у вигляді графіків амплітудний і фазовий спектри сигналу")
        add_img(self.document, 'img/2ex_w.png', 'Амплітудний спектр двостороннього експоненційного сигналу')
        add_img(self.document, 'img/2ex_f.png', 'Фазовий спектр двостороннього експоненційного сигналу')
        line("Помножимо сигнал s(t) на гармонійну функцію (s1(t)), а потім знайдемо спектральну функцію D1(ω) нового сигналу s1(t)")
        add_img(self.document, 'img/2ex_line.png', 'Амплітудний двостороннього експоненційного сигналу')