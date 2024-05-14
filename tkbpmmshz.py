import tkinter as tk
import tkinter.ttk as ttk
from itertools import count
import decimal

""" Set a bpm and click the buttons to copy ms and hz values to the clipboard.
    Set a frequency for A4 and click the buttons to copy hz values to the clipboard.
"""

power = decimal.getcontext().power
D = decimal.Decimal
_1 = D(1)
_2 = D(2)
_12 = D(12)



def nextnote(freq):
    return freq * power(_2,_1/_12)
def prevnote(freq):
    return freq * power(_2,-_1/_12)

class App(tk.Tk):
    # {{{1 trace_freq_var
    def trace_freq_var(self,*traceargs):
        freq = self.freq_var.get()
        _F = D(freq)
        notes_up = []
        notes_dn = [_F]
        _f = _F
        for i in range((12*7)+3):
            _f = nextnote(_f)
            notes_up.append(_f)
        _f = _F
        for i in range((12*5)-3):
            _f = prevnote(_f)
            notes_dn.append(_f)
        notes = list(reversed(notes_dn))
        notes.extend(notes_up)
        note_iter = iter(notes)

        self.freq_var_oct_0_note_C.set(next(note_iter))
        self.freq_var_oct_0_note_Cs.set(next(note_iter))
        self.freq_var_oct_0_note_D.set(next(note_iter))
        self.freq_var_oct_0_note_Ds.set(next(note_iter))
        self.freq_var_oct_0_note_E.set(next(note_iter))
        self.freq_var_oct_0_note_F.set(next(note_iter))
        self.freq_var_oct_0_note_Fs.set(next(note_iter))
        self.freq_var_oct_0_note_G.set(next(note_iter))
        self.freq_var_oct_0_note_Gs.set(next(note_iter))
        self.freq_var_oct_0_note_A.set(next(note_iter))
        self.freq_var_oct_0_note_As.set(next(note_iter))
        self.freq_var_oct_0_note_B.set(next(note_iter))

        self.freq_var_oct_1_note_C.set(next(note_iter))
        self.freq_var_oct_1_note_Cs.set(next(note_iter))
        self.freq_var_oct_1_note_D.set(next(note_iter))
        self.freq_var_oct_1_note_Ds.set(next(note_iter))
        self.freq_var_oct_1_note_E.set(next(note_iter))
        self.freq_var_oct_1_note_F.set(next(note_iter))
        self.freq_var_oct_1_note_Fs.set(next(note_iter))
        self.freq_var_oct_1_note_G.set(next(note_iter))
        self.freq_var_oct_1_note_Gs.set(next(note_iter))
        self.freq_var_oct_1_note_A.set(next(note_iter))
        self.freq_var_oct_1_note_As.set(next(note_iter))
        self.freq_var_oct_1_note_B.set(next(note_iter))

        self.freq_var_oct_2_note_C.set(next(note_iter))
        self.freq_var_oct_2_note_Cs.set(next(note_iter))
        self.freq_var_oct_2_note_D.set(next(note_iter))
        self.freq_var_oct_2_note_Ds.set(next(note_iter))
        self.freq_var_oct_2_note_E.set(next(note_iter))
        self.freq_var_oct_2_note_F.set(next(note_iter))
        self.freq_var_oct_2_note_Fs.set(next(note_iter))
        self.freq_var_oct_2_note_G.set(next(note_iter))
        self.freq_var_oct_2_note_Gs.set(next(note_iter))
        self.freq_var_oct_2_note_A.set(next(note_iter))
        self.freq_var_oct_2_note_As.set(next(note_iter))
        self.freq_var_oct_2_note_B.set(next(note_iter))

        self.freq_var_oct_3_note_C.set(next(note_iter))
        self.freq_var_oct_3_note_Cs.set(next(note_iter))
        self.freq_var_oct_3_note_D.set(next(note_iter))
        self.freq_var_oct_3_note_Ds.set(next(note_iter))
        self.freq_var_oct_3_note_E.set(next(note_iter))
        self.freq_var_oct_3_note_F.set(next(note_iter))
        self.freq_var_oct_3_note_Fs.set(next(note_iter))
        self.freq_var_oct_3_note_G.set(next(note_iter))
        self.freq_var_oct_3_note_Gs.set(next(note_iter))
        self.freq_var_oct_3_note_A.set(next(note_iter))
        self.freq_var_oct_3_note_As.set(next(note_iter))
        self.freq_var_oct_3_note_B.set(next(note_iter))

        self.freq_var_oct_4_note_C.set(next(note_iter))
        self.freq_var_oct_4_note_Cs.set(next(note_iter))
        self.freq_var_oct_4_note_D.set(next(note_iter))
        self.freq_var_oct_4_note_Ds.set(next(note_iter))
        self.freq_var_oct_4_note_E.set(next(note_iter))
        self.freq_var_oct_4_note_F.set(next(note_iter))
        self.freq_var_oct_4_note_Fs.set(next(note_iter))
        self.freq_var_oct_4_note_G.set(next(note_iter))
        self.freq_var_oct_4_note_Gs.set(next(note_iter))
        self.freq_var_oct_4_note_A.set(next(note_iter))
        self.freq_var_oct_4_note_As.set(next(note_iter))
        self.freq_var_oct_4_note_B.set(next(note_iter))

        self.freq_var_oct_5_note_C.set(next(note_iter))
        self.freq_var_oct_5_note_Cs.set(next(note_iter))
        self.freq_var_oct_5_note_D.set(next(note_iter))
        self.freq_var_oct_5_note_Ds.set(next(note_iter))
        self.freq_var_oct_5_note_E.set(next(note_iter))
        self.freq_var_oct_5_note_F.set(next(note_iter))
        self.freq_var_oct_5_note_Fs.set(next(note_iter))
        self.freq_var_oct_5_note_G.set(next(note_iter))
        self.freq_var_oct_5_note_Gs.set(next(note_iter))
        self.freq_var_oct_5_note_A.set(next(note_iter))
        self.freq_var_oct_5_note_As.set(next(note_iter))
        self.freq_var_oct_5_note_B.set(next(note_iter))

        self.freq_var_oct_6_note_C.set(next(note_iter))
        self.freq_var_oct_6_note_Cs.set(next(note_iter))
        self.freq_var_oct_6_note_D.set(next(note_iter))
        self.freq_var_oct_6_note_Ds.set(next(note_iter))
        self.freq_var_oct_6_note_E.set(next(note_iter))
        self.freq_var_oct_6_note_F.set(next(note_iter))
        self.freq_var_oct_6_note_Fs.set(next(note_iter))
        self.freq_var_oct_6_note_G.set(next(note_iter))
        self.freq_var_oct_6_note_Gs.set(next(note_iter))
        self.freq_var_oct_6_note_A.set(next(note_iter))
        self.freq_var_oct_6_note_As.set(next(note_iter))
        self.freq_var_oct_6_note_B.set(next(note_iter))

        self.freq_var_oct_7_note_C.set(next(note_iter))
        self.freq_var_oct_7_note_Cs.set(next(note_iter))
        self.freq_var_oct_7_note_D.set(next(note_iter))
        self.freq_var_oct_7_note_Ds.set(next(note_iter))
        self.freq_var_oct_7_note_E.set(next(note_iter))
        self.freq_var_oct_7_note_F.set(next(note_iter))
        self.freq_var_oct_7_note_Fs.set(next(note_iter))
        self.freq_var_oct_7_note_G.set(next(note_iter))
        self.freq_var_oct_7_note_Gs.set(next(note_iter))
        self.freq_var_oct_7_note_A.set(next(note_iter))
        self.freq_var_oct_7_note_As.set(next(note_iter))
        self.freq_var_oct_7_note_B.set(next(note_iter))

        self.freq_var_oct_8_note_C.set(next(note_iter))
        self.freq_var_oct_8_note_Cs.set(next(note_iter))
        self.freq_var_oct_8_note_D.set(next(note_iter))
        self.freq_var_oct_8_note_Ds.set(next(note_iter))
        self.freq_var_oct_8_note_E.set(next(note_iter))
        self.freq_var_oct_8_note_F.set(next(note_iter))
        self.freq_var_oct_8_note_Fs.set(next(note_iter))
        self.freq_var_oct_8_note_G.set(next(note_iter))
        self.freq_var_oct_8_note_Gs.set(next(note_iter))
        self.freq_var_oct_8_note_A.set(next(note_iter))
        self.freq_var_oct_8_note_As.set(next(note_iter))
        self.freq_var_oct_8_note_B.set(next(note_iter))

        self.freq_var_oct_9_note_C.set(next(note_iter))
        self.freq_var_oct_9_note_Cs.set(next(note_iter))
        self.freq_var_oct_9_note_D.set(next(note_iter))
        self.freq_var_oct_9_note_Ds.set(next(note_iter))
        self.freq_var_oct_9_note_E.set(next(note_iter))
        self.freq_var_oct_9_note_F.set(next(note_iter))
        self.freq_var_oct_9_note_Fs.set(next(note_iter))
        self.freq_var_oct_9_note_G.set(next(note_iter))
        self.freq_var_oct_9_note_Gs.set(next(note_iter))
        self.freq_var_oct_9_note_A.set(next(note_iter))
        self.freq_var_oct_9_note_As.set(next(note_iter))
        self.freq_var_oct_9_note_B.set(next(note_iter))

        self.freq_var_oct_10_note_C.set(next(note_iter))
        self.freq_var_oct_10_note_Cs.set(next(note_iter))
        self.freq_var_oct_10_note_D.set(next(note_iter))
        self.freq_var_oct_10_note_Ds.set(next(note_iter))
        self.freq_var_oct_10_note_E.set(next(note_iter))
        self.freq_var_oct_10_note_F.set(next(note_iter))
        self.freq_var_oct_10_note_Fs.set(next(note_iter))
        self.freq_var_oct_10_note_G.set(next(note_iter))
        self.freq_var_oct_10_note_Gs.set(next(note_iter))
        self.freq_var_oct_10_note_A.set(next(note_iter))
        self.freq_var_oct_10_note_As.set(next(note_iter))
        self.freq_var_oct_10_note_B.set(next(note_iter))
        # }}}1

    # {{{1 trace_bpm_var
    def trace_bpm_var(self,*traceargs):
        bpm = self.bpm_var.get()
        use_1k = self.ms_x1k.get()
        print("use_1k:",use_1k)
        scale = [1,1000][use_1k]
        print("scale:",scale)

        ms_128_bar = 60*512 / bpm * scale
        ms_64_bar = 60*256 / bpm * scale
        ms_32_bar = 60*128 / bpm * scale
        ms_16_bar = 60*64 / bpm * scale
        ms_8_bar = 60*32 / bpm * scale
        ms_4_bar = 60*16 / bpm * scale
        ms_2_bar = 60*8 / bpm * scale
        ms_1_bar = 60*4 / bpm * scale
        ms_1_2_note = 60*2 / bpm * scale
        ms_1_4_note = 60 / bpm * scale
        ms_1_8_note = 60 / 2 / bpm * scale
        ms_1_16_note = 60 / 4 / bpm * scale
        ms_1_32_note = 60 / 8 / bpm * scale
        ms_1_64_note = 60 / 16 / bpm * scale
        ms_1_128_note = 60 / 32 / bpm * scale

        ms_1_2_note_dotted = 180 / bpm * scale
        ms_1_4_note_dotted = 90 / bpm * scale
        ms_1_8_note_dotted = 45 / bpm * scale
        ms_1_16_note_dotted = 22.5 / bpm * scale

        ms_1_2_note_triplet = 80 / bpm * scale
        ms_1_4_note_triplet = 40 / bpm * scale
        ms_1_8_note_triplet = 20 / bpm * scale
        ms_1_16_note_triplet = 10 / bpm * scale

        self.ms_128_bar.set(f"{ms_128_bar:.06f}")
        self.ms_64_bar.set(f"{ms_64_bar:.06f}")
        self.ms_32_bar.set(f"{ms_32_bar:.06f}")
        self.ms_16_bar.set(f"{ms_16_bar:.06f}")
        self.ms_8_bar.set(f"{ms_8_bar:.06f}")
        self.ms_4_bar.set(f"{ms_4_bar:.06f}")
        self.ms_2_bar.set(f"{ms_2_bar:.06f}")
        self.ms_1_bar.set(f"{ms_1_bar:.06f}")
        self.ms_1_2_note.set(f"{ms_1_2_note:.06f}")
        self.ms_1_4_note.set(f"{ms_1_4_note:.06f}")
        self.ms_1_8_note.set(f"{ms_1_8_note:.06f}")
        self.ms_1_16_note.set(f"{ms_1_16_note:.06f}")
        self.ms_1_32_note.set(f"{ms_1_32_note:.06f}")
        self.ms_1_64_note.set(f"{ms_1_64_note:.06f}")
        self.ms_1_128_note.set(f"{ms_1_128_note:.06f}")

        self.ms_1_2_note_dotted.set(f"{ms_1_2_note_dotted:.06f}")
        self.ms_1_4_note_dotted.set(f"{ms_1_4_note_dotted:.06f}")
        self.ms_1_8_note_dotted.set(f"{ms_1_8_note_dotted:.06f}")
        self.ms_1_16_note_dotted.set(f"{ms_1_16_note_dotted:.06f}")

        self.ms_1_2_note_triplet.set(f"{ms_1_2_note_triplet:.06f}")
        self.ms_1_4_note_triplet.set(f"{ms_1_4_note_triplet:.06f}")
        self.ms_1_8_note_triplet.set(f"{ms_1_8_note_triplet:.06f}")
        self.ms_1_16_note_triplet.set(f"{ms_1_16_note_triplet:.06f}")

        hz_128_bar = bpm/60/512
        hz_64_bar = bpm/60/256
        hz_32_bar = bpm/60/128
        hz_16_bar = bpm/60/64
        hz_8_bar = bpm/60/32
        hz_4_bar = bpm/60/16
        hz_2_bar = bpm/60/8
        hz_1_bar = bpm/60/4
        hz_1_2_note = bpm/60/2
        hz_1_4_note = bpm/60
        hz_1_8_note = bpm/60*2
        hz_1_16_note = bpm/60*4
        hz_1_32_note = bpm/60*8
        hz_1_64_note = bpm/60*16
        hz_1_128_note = bpm/60*32

        hz_1_2_note_dotted = bpm/180
        hz_1_4_note_dotted =  bpm/90
        hz_1_8_note_dotted =  bpm/45
        hz_1_16_note_dotted =  bpm/22.5

        hz_1_2_note_triplet = bpm/80
        hz_1_4_note_triplet =  bpm/40
        hz_1_8_note_triplet =  bpm/20
        hz_1_16_note_triplet =  bpm/10
        
        self.hz_128_bar.set(f"{hz_128_bar:.06f}")
        self.hz_64_bar.set(f"{hz_64_bar:.06f}")
        self.hz_32_bar.set(f"{hz_32_bar:.06f}")
        self.hz_16_bar.set(f"{hz_16_bar:.06f}")
        self.hz_8_bar.set(f"{hz_8_bar:.06f}")
        self.hz_4_bar.set(f"{hz_4_bar:.06f}")
        self.hz_2_bar.set(f"{hz_2_bar:.06f}")
        self.hz_1_bar.set(f"{hz_1_bar:.06f}")
        self.hz_1_2_note.set(f"{hz_1_2_note:.06f}")
        self.hz_1_4_note.set(f"{hz_1_4_note:.06f}")
        self.hz_1_8_note.set(f"{hz_1_8_note:.06f}")
        self.hz_1_16_note.set(f"{hz_1_16_note:.06f}")
        self.hz_1_32_note.set(f"{hz_1_32_note:.06f}")
        self.hz_1_64_note.set(f"{hz_1_64_note:.06f}")
        self.hz_1_128_note.set(f"{hz_1_128_note:.06f}")

        self.hz_1_2_note_dotted.set(f"{hz_1_2_note_dotted:.06f}")
        self.hz_1_4_note_dotted.set(f"{hz_1_4_note_dotted:.06f}")
        self.hz_1_8_note_dotted.set(f"{hz_1_8_note_dotted:.06f}")
        self.hz_1_16_note_dotted.set(f"{hz_1_16_note_dotted:.06f}")

        self.hz_1_2_note_triplet.set(f"{hz_1_2_note_triplet:.06f}")
        self.hz_1_4_note_triplet.set(f"{hz_1_4_note_triplet:.06f}")
        self.hz_1_8_note_triplet.set(f"{hz_1_8_note_triplet:.06f}")
        self.hz_1_16_note_triplet.set(f"{hz_1_16_note_triplet:.06f}")
        # }}}1

    def __init__(self):
        super().__init__()
        self.bpm_var = tk.DoubleVar()
        self.freq_var = tk.DoubleVar()
        self.ms_x1k = tk.IntVar()

        # {{{1 instantiate frequency variables
        self.freq_var_oct_0_note_C = tk.DoubleVar()
        self.freq_var_oct_0_note_Cs = tk.DoubleVar()
        self.freq_var_oct_0_note_D = tk.DoubleVar()
        self.freq_var_oct_0_note_Ds = tk.DoubleVar()
        self.freq_var_oct_0_note_E = tk.DoubleVar()
        self.freq_var_oct_0_note_F = tk.DoubleVar()
        self.freq_var_oct_0_note_Fs = tk.DoubleVar()
        self.freq_var_oct_0_note_G = tk.DoubleVar()
        self.freq_var_oct_0_note_Gs = tk.DoubleVar()
        self.freq_var_oct_0_note_A = tk.DoubleVar()
        self.freq_var_oct_0_note_As = tk.DoubleVar()
        self.freq_var_oct_0_note_B = tk.DoubleVar()

        self.freq_var_oct_1_note_C = tk.DoubleVar()
        self.freq_var_oct_1_note_Cs = tk.DoubleVar()
        self.freq_var_oct_1_note_D = tk.DoubleVar()
        self.freq_var_oct_1_note_Ds = tk.DoubleVar()
        self.freq_var_oct_1_note_E = tk.DoubleVar()
        self.freq_var_oct_1_note_F = tk.DoubleVar()
        self.freq_var_oct_1_note_Fs = tk.DoubleVar()
        self.freq_var_oct_1_note_G = tk.DoubleVar()
        self.freq_var_oct_1_note_Gs = tk.DoubleVar()
        self.freq_var_oct_1_note_A = tk.DoubleVar()
        self.freq_var_oct_1_note_As = tk.DoubleVar()
        self.freq_var_oct_1_note_B = tk.DoubleVar()

        self.freq_var_oct_2_note_C = tk.DoubleVar()
        self.freq_var_oct_2_note_Cs = tk.DoubleVar()
        self.freq_var_oct_2_note_D = tk.DoubleVar()
        self.freq_var_oct_2_note_Ds = tk.DoubleVar()
        self.freq_var_oct_2_note_E = tk.DoubleVar()
        self.freq_var_oct_2_note_F = tk.DoubleVar()
        self.freq_var_oct_2_note_Fs = tk.DoubleVar()
        self.freq_var_oct_2_note_G = tk.DoubleVar()
        self.freq_var_oct_2_note_Gs = tk.DoubleVar()
        self.freq_var_oct_2_note_A = tk.DoubleVar()
        self.freq_var_oct_2_note_As = tk.DoubleVar()
        self.freq_var_oct_2_note_B = tk.DoubleVar()

        self.freq_var_oct_3_note_C = tk.DoubleVar()
        self.freq_var_oct_3_note_Cs = tk.DoubleVar()
        self.freq_var_oct_3_note_D = tk.DoubleVar()
        self.freq_var_oct_3_note_Ds = tk.DoubleVar()
        self.freq_var_oct_3_note_E = tk.DoubleVar()
        self.freq_var_oct_3_note_F = tk.DoubleVar()
        self.freq_var_oct_3_note_Fs = tk.DoubleVar()
        self.freq_var_oct_3_note_G = tk.DoubleVar()
        self.freq_var_oct_3_note_Gs = tk.DoubleVar()
        self.freq_var_oct_3_note_A = tk.DoubleVar()
        self.freq_var_oct_3_note_As = tk.DoubleVar()
        self.freq_var_oct_3_note_B = tk.DoubleVar()

        self.freq_var_oct_4_note_C = tk.DoubleVar()
        self.freq_var_oct_4_note_Cs = tk.DoubleVar()
        self.freq_var_oct_4_note_D = tk.DoubleVar()
        self.freq_var_oct_4_note_Ds = tk.DoubleVar()
        self.freq_var_oct_4_note_E = tk.DoubleVar()
        self.freq_var_oct_4_note_F = tk.DoubleVar()
        self.freq_var_oct_4_note_Fs = tk.DoubleVar()
        self.freq_var_oct_4_note_G = tk.DoubleVar()
        self.freq_var_oct_4_note_Gs = tk.DoubleVar()
        self.freq_var_oct_4_note_A = tk.DoubleVar()
        self.freq_var_oct_4_note_As = tk.DoubleVar()
        self.freq_var_oct_4_note_B = tk.DoubleVar()

        self.freq_var_oct_5_note_C = tk.DoubleVar()
        self.freq_var_oct_5_note_Cs = tk.DoubleVar()
        self.freq_var_oct_5_note_D = tk.DoubleVar()
        self.freq_var_oct_5_note_Ds = tk.DoubleVar()
        self.freq_var_oct_5_note_E = tk.DoubleVar()
        self.freq_var_oct_5_note_F = tk.DoubleVar()
        self.freq_var_oct_5_note_Fs = tk.DoubleVar()
        self.freq_var_oct_5_note_G = tk.DoubleVar()
        self.freq_var_oct_5_note_Gs = tk.DoubleVar()
        self.freq_var_oct_5_note_A = tk.DoubleVar()
        self.freq_var_oct_5_note_As = tk.DoubleVar()
        self.freq_var_oct_5_note_B = tk.DoubleVar()

        self.freq_var_oct_6_note_C = tk.DoubleVar()
        self.freq_var_oct_6_note_Cs = tk.DoubleVar()
        self.freq_var_oct_6_note_D = tk.DoubleVar()
        self.freq_var_oct_6_note_Ds = tk.DoubleVar()
        self.freq_var_oct_6_note_E = tk.DoubleVar()
        self.freq_var_oct_6_note_F = tk.DoubleVar()
        self.freq_var_oct_6_note_Fs = tk.DoubleVar()
        self.freq_var_oct_6_note_G = tk.DoubleVar()
        self.freq_var_oct_6_note_Gs = tk.DoubleVar()
        self.freq_var_oct_6_note_A = tk.DoubleVar()
        self.freq_var_oct_6_note_As = tk.DoubleVar()
        self.freq_var_oct_6_note_B = tk.DoubleVar()

        self.freq_var_oct_7_note_C = tk.DoubleVar()
        self.freq_var_oct_7_note_Cs = tk.DoubleVar()
        self.freq_var_oct_7_note_D = tk.DoubleVar()
        self.freq_var_oct_7_note_Ds = tk.DoubleVar()
        self.freq_var_oct_7_note_E = tk.DoubleVar()
        self.freq_var_oct_7_note_F = tk.DoubleVar()
        self.freq_var_oct_7_note_Fs = tk.DoubleVar()
        self.freq_var_oct_7_note_G = tk.DoubleVar()
        self.freq_var_oct_7_note_Gs = tk.DoubleVar()
        self.freq_var_oct_7_note_A = tk.DoubleVar()
        self.freq_var_oct_7_note_As = tk.DoubleVar()
        self.freq_var_oct_7_note_B = tk.DoubleVar()

        self.freq_var_oct_8_note_C = tk.DoubleVar()
        self.freq_var_oct_8_note_Cs = tk.DoubleVar()
        self.freq_var_oct_8_note_D = tk.DoubleVar()
        self.freq_var_oct_8_note_Ds = tk.DoubleVar()
        self.freq_var_oct_8_note_E = tk.DoubleVar()
        self.freq_var_oct_8_note_F = tk.DoubleVar()
        self.freq_var_oct_8_note_Fs = tk.DoubleVar()
        self.freq_var_oct_8_note_G = tk.DoubleVar()
        self.freq_var_oct_8_note_Gs = tk.DoubleVar()
        self.freq_var_oct_8_note_A = tk.DoubleVar()
        self.freq_var_oct_8_note_As = tk.DoubleVar()
        self.freq_var_oct_8_note_B = tk.DoubleVar()

        self.freq_var_oct_9_note_C = tk.DoubleVar()
        self.freq_var_oct_9_note_Cs = tk.DoubleVar()
        self.freq_var_oct_9_note_D = tk.DoubleVar()
        self.freq_var_oct_9_note_Ds = tk.DoubleVar()
        self.freq_var_oct_9_note_E = tk.DoubleVar()
        self.freq_var_oct_9_note_F = tk.DoubleVar()
        self.freq_var_oct_9_note_Fs = tk.DoubleVar()
        self.freq_var_oct_9_note_G = tk.DoubleVar()
        self.freq_var_oct_9_note_Gs = tk.DoubleVar()
        self.freq_var_oct_9_note_A = tk.DoubleVar()
        self.freq_var_oct_9_note_As = tk.DoubleVar()
        self.freq_var_oct_9_note_B = tk.DoubleVar()

        self.freq_var_oct_10_note_C = tk.DoubleVar()
        self.freq_var_oct_10_note_Cs = tk.DoubleVar()
        self.freq_var_oct_10_note_D = tk.DoubleVar()
        self.freq_var_oct_10_note_Ds = tk.DoubleVar()
        self.freq_var_oct_10_note_E = tk.DoubleVar()
        self.freq_var_oct_10_note_F = tk.DoubleVar()
        self.freq_var_oct_10_note_Fs = tk.DoubleVar()
        self.freq_var_oct_10_note_G = tk.DoubleVar()
        self.freq_var_oct_10_note_Gs = tk.DoubleVar()
        self.freq_var_oct_10_note_A = tk.DoubleVar()
        self.freq_var_oct_10_note_As = tk.DoubleVar()
        self.freq_var_oct_10_note_B = tk.DoubleVar()
        # }}}1

        # {{{1 instantiate milliseconds variables
        self.ms_128_bar = tk.DoubleVar()
        self.ms_64_bar = tk.DoubleVar()
        self.ms_32_bar = tk.DoubleVar()
        self.ms_16_bar = tk.DoubleVar()
        self.ms_8_bar = tk.DoubleVar()
        self.ms_4_bar = tk.DoubleVar()
        self.ms_2_bar = tk.DoubleVar()
        self.ms_1_bar = tk.DoubleVar()
        self.ms_1_2_note = tk.DoubleVar()
        self.ms_1_4_note = tk.DoubleVar()
        self.ms_1_8_note = tk.DoubleVar()
        self.ms_1_16_note = tk.DoubleVar()
        self.ms_1_32_note = tk.DoubleVar()
        self.ms_1_64_note = tk.DoubleVar()
        self.ms_1_128_note = tk.DoubleVar()

        self.ms_1_2_note_dotted = tk.DoubleVar()
        self.ms_1_4_note_dotted = tk.DoubleVar()
        self.ms_1_8_note_dotted = tk.DoubleVar()
        self.ms_1_16_note_dotted = tk.DoubleVar()

        self.ms_1_2_note_triplet = tk.DoubleVar()
        self.ms_1_4_note_triplet = tk.DoubleVar()
        self.ms_1_8_note_triplet = tk.DoubleVar()
        self.ms_1_16_note_triplet = tk.DoubleVar()

        self.hz_1_128_note = tk.DoubleVar()
        self.hz_1_64_note = tk.DoubleVar()
        self.hz_1_32_note = tk.DoubleVar()
        self.hz_1_16_note = tk.DoubleVar()
        self.hz_1_8_note = tk.DoubleVar()
        self.hz_1_4_note = tk.DoubleVar()
        self.hz_1_2_note = tk.DoubleVar()
        self.hz_1_bar = tk.DoubleVar()
        self.hz_2_bar = tk.DoubleVar()
        self.hz_4_bar = tk.DoubleVar()
        self.hz_8_bar = tk.DoubleVar()
        self.hz_16_bar = tk.DoubleVar()
        self.hz_32_bar = tk.DoubleVar()
        self.hz_64_bar = tk.DoubleVar()
        self.hz_128_bar = tk.DoubleVar()

        self.hz_1_2_note_dotted = tk.DoubleVar()
        self.hz_1_4_note_dotted = tk.DoubleVar()
        self.hz_1_8_note_dotted = tk.DoubleVar()
        self.hz_1_16_note_dotted = tk.DoubleVar()

        self.hz_1_2_note_triplet = tk.DoubleVar()
        self.hz_1_4_note_triplet = tk.DoubleVar()
        self.hz_1_8_note_triplet = tk.DoubleVar()
        self.hz_1_16_note_triplet = tk.DoubleVar()
        # }}}1

        self.bpm_var.set(120.0)
        self.freq_var.set(440.0)

        self.bpm_var.trace("w",self.trace_bpm_var)
        self.ms_x1k.trace("w",self.trace_bpm_var)
        self.freq_var.trace("w",self.trace_freq_var)

        self.bpmlabel = ttk.Label(self,textvariable=self.bpm_var)
        self.freqlabel = ttk.Label(self,textvariable=self.freq_var)

        self.leftframe = ttk.Frame(self)
        self.rightframe = ttk.Frame(self)
        self.leftframe.pack(side="left",anchor="nw")
        self.rightframe.pack(side="right",anchor="nw")

        self.bpm_spinbox = tk.Spinbox(self.leftframe,
                                      textvariable=self.bpm_var,
                                      from_=30.0,
                                      to=420.0,
                                      increment=1.0)
        self.bpm_spinbox.pack()
        
        self.ms_x1k_chkbtn = ttk.Checkbutton(self.leftframe,
                                             text="x1000",
                                             variable=self.ms_x1k)
        self.ms_x1k_chkbtn.pack()

        self.btnframe = ttk.Labelframe(self.leftframe,labelwidget=self.bpmlabel)
        self.btnframe.pack()

        self.lbl_ms = ttk.Label(self.btnframe,text="ms")
        
        # {{{1 instantiate millisecond buttons
        self.btn_ms_1_128_note = ttk.Button(self.btnframe,textvariable=self.ms_1_128_note,command=lambda s=self,v=self.ms_1_128_note:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])
        self.btn_ms_1_64_note = ttk.Button(self.btnframe,textvariable=self.ms_1_64_note,command=lambda s=self,v=self.ms_1_64_note:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])
        self.btn_ms_1_32_note = ttk.Button(self.btnframe,textvariable=self.ms_1_32_note,command=lambda s=self,v=self.ms_1_32_note:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])
        self.btn_ms_1_16_note = ttk.Button(self.btnframe,textvariable=self.ms_1_16_note,command=lambda s=self,v=self.ms_1_16_note:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])
        self.btn_ms_1_8_note = ttk.Button(self.btnframe,textvariable=self.ms_1_8_note,command=lambda s=self,v=self.ms_1_8_note:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])
        self.btn_ms_1_4_note = ttk.Button(self.btnframe,textvariable=self.ms_1_4_note,command=lambda s=self,v=self.ms_1_4_note:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])
        self.btn_ms_1_2_note = ttk.Button(self.btnframe,textvariable=self.ms_1_2_note,command=lambda s=self,v=self.ms_1_2_note:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])
        self.btn_ms_1_bar = ttk.Button(self.btnframe,textvariable=self.ms_1_bar,command=lambda s=self,v=self.ms_1_bar:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])
        self.btn_ms_2_bar = ttk.Button(self.btnframe,textvariable=self.ms_2_bar,command=lambda s=self,v=self.ms_2_bar:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])
        self.btn_ms_4_bar = ttk.Button(self.btnframe,textvariable=self.ms_4_bar,command=lambda s=self,v=self.ms_4_bar:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])
        self.btn_ms_8_bar = ttk.Button(self.btnframe,textvariable=self.ms_8_bar,command=lambda s=self,v=self.ms_8_bar:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])
        self.btn_ms_16_bar = ttk.Button(self.btnframe,textvariable=self.ms_16_bar,command=lambda s=self,v=self.ms_16_bar:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])
        self.btn_ms_32_bar = ttk.Button(self.btnframe,textvariable=self.ms_32_bar,command=lambda s=self,v=self.ms_32_bar:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])
        self.btn_ms_64_bar = ttk.Button(self.btnframe,textvariable=self.ms_64_bar,command=lambda s=self,v=self.ms_64_bar:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])
        self.btn_ms_128_bar = ttk.Button(self.btnframe,textvariable=self.ms_128_bar,command=lambda s=self,v=self.ms_128_bar:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.btn_ms_1_2_note_dotted = ttk.Button(self.btnframe,textvariable=self.ms_1_2_note_dotted,command=lambda s=self,v=self.ms_1_2_note_dotted:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])
        self.btn_ms_1_4_note_dotted = ttk.Button(self.btnframe,textvariable=self.ms_1_4_note_dotted,command=lambda s=self,v=self.ms_1_4_note_dotted:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])
        self.btn_ms_1_8_note_dotted = ttk.Button(self.btnframe,textvariable=self.ms_1_8_note_dotted,command=lambda s=self,v=self.ms_1_8_note_dotted:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])
        self.btn_ms_1_16_note_dotted = ttk.Button(self.btnframe,textvariable=self.ms_1_16_note_dotted,command=lambda s=self,v=self.ms_1_16_note_dotted:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.btn_ms_1_2_note_triplet = ttk.Button(self.btnframe,textvariable=self.ms_1_2_note_triplet,command=lambda s=self,v=self.ms_1_2_note_triplet:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])
        self.btn_ms_1_4_note_triplet = ttk.Button(self.btnframe,textvariable=self.ms_1_4_note_triplet,command=lambda s=self,v=self.ms_1_4_note_triplet:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])
        self.btn_ms_1_8_note_triplet = ttk.Button(self.btnframe,textvariable=self.ms_1_8_note_triplet,command=lambda s=self,v=self.ms_1_8_note_triplet:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])
        self.btn_ms_1_16_note_triplet = ttk.Button(self.btnframe,textvariable=self.ms_1_16_note_triplet,command=lambda s=self,v=self.ms_1_16_note_triplet:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])
        # }}}1

        self.lbl_duration = ttk.Label(self.btnframe,text="")

        # {{{1 instantiate duration labels
        self.lbl_1_128_note = ttk.Label(self.btnframe,text="1/128th")
        self.lbl_1_64_note = ttk.Label(self.btnframe,text="1/64th")
        self.lbl_1_32_note = ttk.Label(self.btnframe,text="1/32nd")
        self.lbl_1_16_note = ttk.Label(self.btnframe,text="1/16th")
        self.lbl_1_8_note = ttk.Label(self.btnframe,text="1/8th")
        self.lbl_1_4_note = ttk.Label(self.btnframe,text="1/4")
        self.lbl_1_2_note = ttk.Label(self.btnframe,text="1/2")
        self.lbl_1_bar = ttk.Label(self.btnframe,text="1 bar")
        self.lbl_2_bar = ttk.Label(self.btnframe,text="2 bar")
        self.lbl_4_bar = ttk.Label(self.btnframe,text="4 bar")
        self.lbl_8_bar = ttk.Label(self.btnframe,text="8 bar")
        self.lbl_16_bar = ttk.Label(self.btnframe,text="16 bar")
        self.lbl_32_bar = ttk.Label(self.btnframe,text="32 bar")
        self.lbl_64_bar = ttk.Label(self.btnframe,text="64 bar")
        self.lbl_128_bar = ttk.Label(self.btnframe,text="128 bar")

        self.lbl_1_2_note_dotted = ttk.Label(self.btnframe,text="·1/2")
        self.lbl_1_4_note_dotted = ttk.Label(self.btnframe,text="·1/4")
        self.lbl_1_8_note_dotted = ttk.Label(self.btnframe,text="·1/8")
        self.lbl_1_16_note_dotted = ttk.Label(self.btnframe,text="·1/16")

        self.lbl_1_2_note_triplet = ttk.Label(self.btnframe,text="1/2t")
        self.lbl_1_4_note_triplet = ttk.Label(self.btnframe,text="1/4t")
        self.lbl_1_8_note_triplet = ttk.Label(self.btnframe,text="1/8t")
        self.lbl_1_16_note_triplet = ttk.Label(self.btnframe,text="1/16t")

        # }}}1

        self.lbl_hz = ttk.Label(self.btnframe,text="hz")

        # {{{1 instantiate hertz ratios buttons
        self.btn_hz_1_128_note = ttk.Button(self.btnframe,textvariable=self.hz_1_128_note,command=lambda s=self,v=self.hz_1_128_note:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])
        self.btn_hz_1_64_note = ttk.Button(self.btnframe,textvariable=self.hz_1_64_note,command=lambda s=self,v=self.hz_1_64_note:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])
        self.btn_hz_1_32_note = ttk.Button(self.btnframe,textvariable=self.hz_1_32_note,command=lambda s=self,v=self.hz_1_32_note:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])
        self.btn_hz_1_16_note = ttk.Button(self.btnframe,textvariable=self.hz_1_16_note,command=lambda s=self,v=self.hz_1_16_note:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])
        self.btn_hz_1_8_note = ttk.Button(self.btnframe,textvariable=self.hz_1_8_note,command=lambda s=self,v=self.hz_1_8_note:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])
        self.btn_hz_1_4_note = ttk.Button(self.btnframe,textvariable=self.hz_1_4_note,command=lambda s=self,v=self.hz_1_4_note:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])
        self.btn_hz_1_2_note = ttk.Button(self.btnframe,textvariable=self.hz_1_2_note,command=lambda s=self,v=self.hz_1_2_note:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])
        self.btn_hz_1_bar = ttk.Button(self.btnframe,textvariable=self.hz_1_bar,command=lambda s=self,v=self.hz_1_bar:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])
        self.btn_hz_2_bar = ttk.Button(self.btnframe,textvariable=self.hz_2_bar,command=lambda s=self,v=self.hz_2_bar:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])
        self.btn_hz_4_bar = ttk.Button(self.btnframe,textvariable=self.hz_4_bar,command=lambda s=self,v=self.hz_4_bar:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])
        self.btn_hz_8_bar = ttk.Button(self.btnframe,textvariable=self.hz_8_bar,command=lambda s=self,v=self.hz_8_bar:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])
        self.btn_hz_16_bar = ttk.Button(self.btnframe,textvariable=self.hz_16_bar,command=lambda s=self,v=self.hz_16_bar:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])
        self.btn_hz_32_bar = ttk.Button(self.btnframe,textvariable=self.hz_32_bar,command=lambda s=self,v=self.hz_32_bar:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])
        self.btn_hz_64_bar = ttk.Button(self.btnframe,textvariable=self.hz_64_bar,command=lambda s=self,v=self.hz_64_bar:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])
        self.btn_hz_128_bar = ttk.Button(self.btnframe,textvariable=self.hz_128_bar,command=lambda s=self,v=self.hz_128_bar:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.btn_hz_1_2_note_dotted = ttk.Button(self.btnframe,textvariable=self.hz_1_2_note_dotted,command=lambda s=self,v=self.hz_1_2_note_dotted:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])
        self.btn_hz_1_4_note_dotted = ttk.Button(self.btnframe,textvariable=self.hz_1_4_note_dotted,command=lambda s=self,v=self.hz_1_4_note_dotted:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])
        self.btn_hz_1_8_note_dotted = ttk.Button(self.btnframe,textvariable=self.hz_1_8_note_dotted,command=lambda s=self,v=self.hz_1_8_note_dotted:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])
        self.btn_hz_1_16_note_dotted = ttk.Button(self.btnframe,textvariable=self.hz_1_16_note_dotted,command=lambda s=self,v=self.hz_1_16_note_dotted:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.btn_hz_1_2_note_triplet = ttk.Button(self.btnframe,textvariable=self.hz_1_2_note_triplet,command=lambda s=self,v=self.hz_1_2_note_triplet:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])
        self.btn_hz_1_4_note_triplet = ttk.Button(self.btnframe,textvariable=self.hz_1_4_note_triplet,command=lambda s=self,v=self.hz_1_4_note_triplet:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])
        self.btn_hz_1_8_note_triplet = ttk.Button(self.btnframe,textvariable=self.hz_1_8_note_triplet,command=lambda s=self,v=self.hz_1_8_note_triplet:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])
        self.btn_hz_1_16_note_triplet = ttk.Button(self.btnframe,textvariable=self.hz_1_16_note_triplet,command=lambda s=self,v=self.hz_1_16_note_triplet:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])
        # }}}1
        r = count()
        self.lbl_ms.grid(column=0,row=next(r))

        # {{{1 layout millisecond buttons
        self.btn_ms_1_128_note.grid(column=0,row=next(r))
        self.btn_ms_1_64_note.grid(column=0,row=next(r))
        self.btn_ms_1_32_note.grid(column=0,row=next(r))
        self.btn_ms_1_16_note.grid(column=0,row=next(r))
        self.btn_ms_1_8_note.grid(column=0,row=next(r))
        self.btn_ms_1_4_note.grid(column=0,row=next(r))
        self.btn_ms_1_2_note.grid(column=0,row=next(r))
        self.btn_ms_1_bar.grid(column=0,row=next(r))
        self.btn_ms_2_bar.grid(column=0,row=next(r))
        self.btn_ms_4_bar.grid(column=0,row=next(r))
        self.btn_ms_8_bar.grid(column=0,row=next(r))
        self.btn_ms_16_bar.grid(column=0,row=next(r))
        self.btn_ms_32_bar.grid(column=0,row=next(r))
        self.btn_ms_64_bar.grid(column=0,row=next(r))
        self.btn_ms_128_bar.grid(column=0,row=next(r))

        self.btn_ms_1_2_note_dotted.grid(column=0,row=next(r))
        self.btn_ms_1_4_note_dotted.grid(column=0,row=next(r))
        self.btn_ms_1_8_note_dotted.grid(column=0,row=next(r))
        self.btn_ms_1_16_note_dotted.grid(column=0,row=next(r))

        self.btn_ms_1_2_note_triplet.grid(column=0,row=next(r))
        self.btn_ms_1_4_note_triplet.grid(column=0,row=next(r))
        self.btn_ms_1_8_note_triplet.grid(column=0,row=next(r))
        self.btn_ms_1_16_note_triplet.grid(column=0,row=next(r))
        # }}}1

        r = count()
        self.lbl_duration.grid(column=1,row=next(r))

        # {{{1 layout duration labels
        self.lbl_1_128_note.grid(column=1,row=next(r))
        self.lbl_1_64_note.grid(column=1,row=next(r))
        self.lbl_1_32_note.grid(column=1,row=next(r))
        self.lbl_1_16_note.grid(column=1,row=next(r))
        self.lbl_1_8_note.grid(column=1,row=next(r))
        self.lbl_1_4_note.grid(column=1,row=next(r))
        self.lbl_1_2_note.grid(column=1,row=next(r))
        self.lbl_1_bar.grid(column=1,row=next(r))
        self.lbl_2_bar.grid(column=1,row=next(r))
        self.lbl_4_bar.grid(column=1,row=next(r))
        self.lbl_8_bar.grid(column=1,row=next(r))
        self.lbl_16_bar.grid(column=1,row=next(r))
        self.lbl_32_bar.grid(column=1,row=next(r))
        self.lbl_64_bar.grid(column=1,row=next(r))
        self.lbl_128_bar.grid(column=1,row=next(r))

        self.lbl_1_2_note_dotted.grid(column=1,row=next(r))
        self.lbl_1_4_note_dotted.grid(column=1,row=next(r))
        self.lbl_1_8_note_dotted.grid(column=1,row=next(r))
        self.lbl_1_16_note_dotted.grid(column=1,row=next(r))

        self.lbl_1_2_note_triplet.grid(column=1,row=next(r))
        self.lbl_1_4_note_triplet.grid(column=1,row=next(r))
        self.lbl_1_8_note_triplet.grid(column=1,row=next(r))
        self.lbl_1_16_note_triplet.grid(column=1,row=next(r))
        # }}}1
        r = count()
        self.lbl_hz.grid(column=2,row=next(r))
        
        # {{{1 layout hertz ratio buttons
        self.btn_hz_1_128_note.grid(column=2,row=next(r))
        self.btn_hz_1_64_note.grid(column=2,row=next(r))
        self.btn_hz_1_32_note.grid(column=2,row=next(r))
        self.btn_hz_1_16_note.grid(column=2,row=next(r))
        self.btn_hz_1_8_note.grid(column=2,row=next(r))
        self.btn_hz_1_4_note.grid(column=2,row=next(r))
        self.btn_hz_1_2_note.grid(column=2,row=next(r))
        self.btn_hz_1_bar.grid(column=2,row=next(r))
        self.btn_hz_2_bar.grid(column=2,row=next(r))
        self.btn_hz_4_bar.grid(column=2,row=next(r))
        self.btn_hz_8_bar.grid(column=2,row=next(r))
        self.btn_hz_16_bar.grid(column=2,row=next(r))
        self.btn_hz_32_bar.grid(column=2,row=next(r))
        self.btn_hz_64_bar.grid(column=2,row=next(r))
        self.btn_hz_128_bar.grid(column=2,row=next(r))

        self.btn_hz_1_2_note_dotted.grid(column=2,row=next(r))
        self.btn_hz_1_4_note_dotted.grid(column=2,row=next(r))
        self.btn_hz_1_8_note_dotted.grid(column=2,row=next(r))
        self.btn_hz_1_16_note_dotted.grid(column=2,row=next(r))

        self.btn_hz_1_2_note_triplet.grid(column=2,row=next(r))
        self.btn_hz_1_4_note_triplet.grid(column=2,row=next(r))
        self.btn_hz_1_8_note_triplet.grid(column=2,row=next(r))
        self.btn_hz_1_16_note_triplet.grid(column=2,row=next(r))
        # }}}1

        self.freq_spinbox = tk.Spinbox(self.rightframe,
                                       textvariable=self.freq_var,
                                       from_=1.0,
                                       to=1000.0,
                                       increment=1.0)
        self.freq_spinbox.pack()

        self.btnframe2 = ttk.Labelframe(self.rightframe,
                                        labelwidget=self.freqlabel)
        self.btnframe2.pack()

        # {{{1 instantiate note frequency buttons
        self.freq_btn_oct_0_note_C = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_0_note_C,
                                      command=lambda s=self,v=self.freq_var_oct_0_note_C:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_0_note_Cs = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_0_note_Cs,
                                      command=lambda s=self,v=self.freq_var_oct_0_note_Cs:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_0_note_D = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_0_note_D,
                                      command=lambda s=self,v=self.freq_var_oct_0_note_D:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_0_note_Ds = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_0_note_Ds,
                                      command=lambda s=self,v=self.freq_var_oct_0_note_Ds:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_0_note_E = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_0_note_E,
                                      command=lambda s=self,v=self.freq_var_oct_0_note_E:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_0_note_F = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_0_note_F,
                                      command=lambda s=self,v=self.freq_var_oct_0_note_F:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_0_note_Fs = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_0_note_Fs,
                                      command=lambda s=self,v=self.freq_var_oct_0_note_Fs:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_0_note_G = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_0_note_G,
                                      command=lambda s=self,v=self.freq_var_oct_0_note_G:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_0_note_Gs = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_0_note_Gs,
                                      command=lambda s=self,v=self.freq_var_oct_0_note_Gs:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_0_note_A = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_0_note_A,
                                      command=lambda s=self,v=self.freq_var_oct_0_note_A:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_0_note_As = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_0_note_As,
                                      command=lambda s=self,v=self.freq_var_oct_0_note_As:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_0_note_B = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_0_note_B,
                                      command=lambda s=self,v=self.freq_var_oct_0_note_B:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])


        self.freq_btn_oct_1_note_C = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_1_note_C,
                                      command=lambda s=self,v=self.freq_var_oct_1_note_C:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_1_note_Cs = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_1_note_Cs,
                                      command=lambda s=self,v=self.freq_var_oct_1_note_Cs:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_1_note_D = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_1_note_D,
                                      command=lambda s=self,v=self.freq_var_oct_1_note_D:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_1_note_Ds = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_1_note_Ds,
                                      command=lambda s=self,v=self.freq_var_oct_1_note_Ds:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_1_note_E = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_1_note_E,
                                      command=lambda s=self,v=self.freq_var_oct_1_note_E:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_1_note_F = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_1_note_F,
                                      command=lambda s=self,v=self.freq_var_oct_1_note_F:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_1_note_Fs = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_1_note_Fs,
                                      command=lambda s=self,v=self.freq_var_oct_1_note_Fs:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_1_note_G = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_1_note_G,
                                      command=lambda s=self,v=self.freq_var_oct_1_note_G:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_1_note_Gs = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_1_note_Gs,
                                      command=lambda s=self,v=self.freq_var_oct_1_note_Gs:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_1_note_A = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_1_note_A,
                                      command=lambda s=self,v=self.freq_var_oct_1_note_A:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_1_note_As = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_1_note_As,
                                      command=lambda s=self,v=self.freq_var_oct_1_note_As:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_1_note_B = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_1_note_B,
                                      command=lambda s=self,v=self.freq_var_oct_1_note_B:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])


        self.freq_btn_oct_2_note_C = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_2_note_C,
                                      command=lambda s=self,v=self.freq_var_oct_2_note_C:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_2_note_Cs = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_2_note_Cs,
                                      command=lambda s=self,v=self.freq_var_oct_2_note_Cs:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_2_note_D = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_2_note_D,
                                      command=lambda s=self,v=self.freq_var_oct_2_note_D:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_2_note_Ds = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_2_note_Ds,
                                      command=lambda s=self,v=self.freq_var_oct_2_note_Ds:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_2_note_E = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_2_note_E,
                                      command=lambda s=self,v=self.freq_var_oct_2_note_E:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_2_note_F = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_2_note_F,
                                      command=lambda s=self,v=self.freq_var_oct_2_note_F:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_2_note_Fs = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_2_note_Fs,
                                      command=lambda s=self,v=self.freq_var_oct_2_note_Fs:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_2_note_G = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_2_note_G,
                                      command=lambda s=self,v=self.freq_var_oct_2_note_G:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_2_note_Gs = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_2_note_Gs,
                                      command=lambda s=self,v=self.freq_var_oct_2_note_Gs:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_2_note_A = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_2_note_A,
                                      command=lambda s=self,v=self.freq_var_oct_2_note_A:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_2_note_As = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_2_note_As,
                                      command=lambda s=self,v=self.freq_var_oct_2_note_As:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_2_note_B = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_2_note_B,
                                      command=lambda s=self,v=self.freq_var_oct_2_note_B:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])


        self.freq_btn_oct_3_note_C = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_3_note_C,
                                      command=lambda s=self,v=self.freq_var_oct_3_note_C:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_3_note_Cs = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_3_note_Cs,
                                      command=lambda s=self,v=self.freq_var_oct_3_note_Cs:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_3_note_D = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_3_note_D,
                                      command=lambda s=self,v=self.freq_var_oct_3_note_D:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_3_note_Ds = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_3_note_Ds,
                                      command=lambda s=self,v=self.freq_var_oct_3_note_Ds:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_3_note_E = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_3_note_E,
                                      command=lambda s=self,v=self.freq_var_oct_3_note_E:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_3_note_F = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_3_note_F,
                                      command=lambda s=self,v=self.freq_var_oct_3_note_F:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_3_note_Fs = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_3_note_Fs,
                                      command=lambda s=self,v=self.freq_var_oct_3_note_Fs:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_3_note_G = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_3_note_G,
                                      command=lambda s=self,v=self.freq_var_oct_3_note_G:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_3_note_Gs = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_3_note_Gs,
                                      command=lambda s=self,v=self.freq_var_oct_3_note_Gs:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_3_note_A = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_3_note_A,
                                      command=lambda s=self,v=self.freq_var_oct_3_note_A:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_3_note_As = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_3_note_As,
                                      command=lambda s=self,v=self.freq_var_oct_3_note_As:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_3_note_B = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_3_note_B,
                                      command=lambda s=self,v=self.freq_var_oct_3_note_B:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])


        self.freq_btn_oct_4_note_C = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_4_note_C,
                                      command=lambda s=self,v=self.freq_var_oct_4_note_C:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_4_note_Cs = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_4_note_Cs,
                                      command=lambda s=self,v=self.freq_var_oct_4_note_Cs:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_4_note_D = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_4_note_D,
                                      command=lambda s=self,v=self.freq_var_oct_4_note_D:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_4_note_Ds = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_4_note_Ds,
                                      command=lambda s=self,v=self.freq_var_oct_4_note_Ds:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_4_note_E = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_4_note_E,
                                      command=lambda s=self,v=self.freq_var_oct_4_note_E:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_4_note_F = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_4_note_F,
                                      command=lambda s=self,v=self.freq_var_oct_4_note_F:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_4_note_Fs = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_4_note_Fs,
                                      command=lambda s=self,v=self.freq_var_oct_4_note_Fs:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_4_note_G = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_4_note_G,
                                      command=lambda s=self,v=self.freq_var_oct_4_note_G:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_4_note_Gs = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_4_note_Gs,
                                      command=lambda s=self,v=self.freq_var_oct_4_note_Gs:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_4_note_A = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_4_note_A,
                                      command=lambda s=self,v=self.freq_var_oct_4_note_A:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_4_note_As = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_4_note_As,
                                      command=lambda s=self,v=self.freq_var_oct_4_note_As:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_4_note_B = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_4_note_B,
                                      command=lambda s=self,v=self.freq_var_oct_4_note_B:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])


        self.freq_btn_oct_5_note_C = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_5_note_C,
                                      command=lambda s=self,v=self.freq_var_oct_5_note_C:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_5_note_Cs = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_5_note_Cs,
                                      command=lambda s=self,v=self.freq_var_oct_5_note_Cs:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_5_note_D = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_5_note_D,
                                      command=lambda s=self,v=self.freq_var_oct_5_note_D:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_5_note_Ds = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_5_note_Ds,
                                      command=lambda s=self,v=self.freq_var_oct_5_note_Ds:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_5_note_E = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_5_note_E,
                                      command=lambda s=self,v=self.freq_var_oct_5_note_E:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_5_note_F = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_5_note_F,
                                      command=lambda s=self,v=self.freq_var_oct_5_note_F:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_5_note_Fs = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_5_note_Fs,
                                      command=lambda s=self,v=self.freq_var_oct_5_note_Fs:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_5_note_G = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_5_note_G,
                                      command=lambda s=self,v=self.freq_var_oct_5_note_G:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_5_note_Gs = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_5_note_Gs,
                                      command=lambda s=self,v=self.freq_var_oct_5_note_Gs:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_5_note_A = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_5_note_A,
                                      command=lambda s=self,v=self.freq_var_oct_5_note_A:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_5_note_As = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_5_note_As,
                                      command=lambda s=self,v=self.freq_var_oct_5_note_As:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_5_note_B = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_5_note_B,
                                      command=lambda s=self,v=self.freq_var_oct_5_note_B:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])


        self.freq_btn_oct_6_note_C = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_6_note_C,
                                      command=lambda s=self,v=self.freq_var_oct_6_note_C:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_6_note_Cs = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_6_note_Cs,
                                      command=lambda s=self,v=self.freq_var_oct_6_note_Cs:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_6_note_D = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_6_note_D,
                                      command=lambda s=self,v=self.freq_var_oct_6_note_D:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_6_note_Ds = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_6_note_Ds,
                                      command=lambda s=self,v=self.freq_var_oct_6_note_Ds:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_6_note_E = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_6_note_E,
                                      command=lambda s=self,v=self.freq_var_oct_6_note_E:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_6_note_F = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_6_note_F,
                                      command=lambda s=self,v=self.freq_var_oct_6_note_F:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_6_note_Fs = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_6_note_Fs,
                                      command=lambda s=self,v=self.freq_var_oct_6_note_Fs:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_6_note_G = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_6_note_G,
                                      command=lambda s=self,v=self.freq_var_oct_6_note_G:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_6_note_Gs = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_6_note_Gs,
                                      command=lambda s=self,v=self.freq_var_oct_6_note_Gs:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_6_note_A = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_6_note_A,
                                      command=lambda s=self,v=self.freq_var_oct_6_note_A:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_6_note_As = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_6_note_As,
                                      command=lambda s=self,v=self.freq_var_oct_6_note_As:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_6_note_B = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_6_note_B,
                                      command=lambda s=self,v=self.freq_var_oct_6_note_B:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])


        self.freq_btn_oct_7_note_C = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_7_note_C,
                                      command=lambda s=self,v=self.freq_var_oct_7_note_C:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_7_note_Cs = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_7_note_Cs,
                                      command=lambda s=self,v=self.freq_var_oct_7_note_Cs:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_7_note_D = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_7_note_D,
                                      command=lambda s=self,v=self.freq_var_oct_7_note_D:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_7_note_Ds = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_7_note_Ds,
                                      command=lambda s=self,v=self.freq_var_oct_7_note_Ds:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_7_note_E = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_7_note_E,
                                      command=lambda s=self,v=self.freq_var_oct_7_note_E:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_7_note_F = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_7_note_F,
                                      command=lambda s=self,v=self.freq_var_oct_7_note_F:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_7_note_Fs = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_7_note_Fs,
                                      command=lambda s=self,v=self.freq_var_oct_7_note_Fs:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_7_note_G = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_7_note_G,
                                      command=lambda s=self,v=self.freq_var_oct_7_note_G:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_7_note_Gs = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_7_note_Gs,
                                      command=lambda s=self,v=self.freq_var_oct_7_note_Gs:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_7_note_A = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_7_note_A,
                                      command=lambda s=self,v=self.freq_var_oct_7_note_A:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_7_note_As = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_7_note_As,
                                      command=lambda s=self,v=self.freq_var_oct_7_note_As:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_7_note_B = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_7_note_B,
                                      command=lambda s=self,v=self.freq_var_oct_7_note_B:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])


        self.freq_btn_oct_8_note_C = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_8_note_C,
                                      command=lambda s=self,v=self.freq_var_oct_8_note_C:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_8_note_Cs = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_8_note_Cs,
                                      command=lambda s=self,v=self.freq_var_oct_8_note_Cs:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_8_note_D = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_8_note_D,
                                      command=lambda s=self,v=self.freq_var_oct_8_note_D:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_8_note_Ds = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_8_note_Ds,
                                      command=lambda s=self,v=self.freq_var_oct_8_note_Ds:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_8_note_E = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_8_note_E,
                                      command=lambda s=self,v=self.freq_var_oct_8_note_E:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_8_note_F = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_8_note_F,
                                      command=lambda s=self,v=self.freq_var_oct_8_note_F:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_8_note_Fs = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_8_note_Fs,
                                      command=lambda s=self,v=self.freq_var_oct_8_note_Fs:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_8_note_G = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_8_note_G,
                                      command=lambda s=self,v=self.freq_var_oct_8_note_G:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_8_note_Gs = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_8_note_Gs,
                                      command=lambda s=self,v=self.freq_var_oct_8_note_Gs:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_8_note_A = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_8_note_A,
                                      command=lambda s=self,v=self.freq_var_oct_8_note_A:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_8_note_As = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_8_note_As,
                                      command=lambda s=self,v=self.freq_var_oct_8_note_As:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_8_note_B = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_8_note_B,
                                      command=lambda s=self,v=self.freq_var_oct_8_note_B:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])


        self.freq_btn_oct_9_note_C = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_9_note_C,
                                      command=lambda s=self,v=self.freq_var_oct_9_note_C:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_9_note_Cs = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_9_note_Cs,
                                      command=lambda s=self,v=self.freq_var_oct_9_note_Cs:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_9_note_D = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_9_note_D,
                                      command=lambda s=self,v=self.freq_var_oct_9_note_D:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_9_note_Ds = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_9_note_Ds,
                                      command=lambda s=self,v=self.freq_var_oct_9_note_Ds:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_9_note_E = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_9_note_E,
                                      command=lambda s=self,v=self.freq_var_oct_9_note_E:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_9_note_F = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_9_note_F,
                                      command=lambda s=self,v=self.freq_var_oct_9_note_F:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_9_note_Fs = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_9_note_Fs,
                                      command=lambda s=self,v=self.freq_var_oct_9_note_Fs:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_9_note_G = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_9_note_G,
                                      command=lambda s=self,v=self.freq_var_oct_9_note_G:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_9_note_Gs = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_9_note_Gs,
                                      command=lambda s=self,v=self.freq_var_oct_9_note_Gs:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_9_note_A = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_9_note_A,
                                      command=lambda s=self,v=self.freq_var_oct_9_note_A:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_9_note_As = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_9_note_As,
                                      command=lambda s=self,v=self.freq_var_oct_9_note_As:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_9_note_B = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_9_note_B,
                                      command=lambda s=self,v=self.freq_var_oct_9_note_B:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])


        self.freq_btn_oct_10_note_C = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_10_note_C,
                                      command=lambda s=self,v=self.freq_var_oct_10_note_C:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_10_note_Cs = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_10_note_Cs,
                                      command=lambda s=self,v=self.freq_var_oct_10_note_Cs:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_10_note_D = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_10_note_D,
                                      command=lambda s=self,v=self.freq_var_oct_10_note_D:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_10_note_Ds = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_10_note_Ds,
                                      command=lambda s=self,v=self.freq_var_oct_10_note_Ds:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_10_note_E = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_10_note_E,
                                      command=lambda s=self,v=self.freq_var_oct_10_note_E:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_10_note_F = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_10_note_F,
                                      command=lambda s=self,v=self.freq_var_oct_10_note_F:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_10_note_Fs = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_10_note_Fs,
                                      command=lambda s=self,v=self.freq_var_oct_10_note_Fs:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_10_note_G = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_10_note_G,
                                      command=lambda s=self,v=self.freq_var_oct_10_note_G:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_10_note_Gs = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_10_note_Gs,
                                      command=lambda s=self,v=self.freq_var_oct_10_note_Gs:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_10_note_A = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_10_note_A,
                                      command=lambda s=self,v=self.freq_var_oct_10_note_A:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_10_note_As = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_10_note_As,
                                      command=lambda s=self,v=self.freq_var_oct_10_note_As:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])

        self.freq_btn_oct_10_note_B = ttk.Button(self.btnframe2,
                                      textvariable=self.freq_var_oct_10_note_B,
                                      command=lambda s=self,v=self.freq_var_oct_10_note_B:[s.clipboard_clear(),s.clipboard_append(str(v.get()))][:])
        # }}}1

        self.freq_lbl_xy = ttk.Label(self.btnframe2,text="")
        self.freq_lbl_xy.grid(column=0,row=0)

        # {{{1 instantiate note frequency labels
        self.freq_lbl_note_C = ttk.Label(self.btnframe2,text="C")
        self.freq_lbl_note_Cs = ttk.Label(self.btnframe2,text="C#")
        self.freq_lbl_note_D = ttk.Label(self.btnframe2,text="D")
        self.freq_lbl_note_Ds = ttk.Label(self.btnframe2,text="D#")
        self.freq_lbl_note_E = ttk.Label(self.btnframe2,text="E")
        self.freq_lbl_note_F = ttk.Label(self.btnframe2,text="F")
        self.freq_lbl_note_Fs = ttk.Label(self.btnframe2,text="F#")
        self.freq_lbl_note_G = ttk.Label(self.btnframe2,text="G")
        self.freq_lbl_note_Gs = ttk.Label(self.btnframe2,text="G#")
        self.freq_lbl_note_A = ttk.Label(self.btnframe2,text="A")
        self.freq_lbl_note_As = ttk.Label(self.btnframe2,text="A#")
        self.freq_lbl_note_B = ttk.Label(self.btnframe2,text="B")

        self.freq_lbl_oct_0 = ttk.Label(self.btnframe2,text="0")
        self.freq_lbl_oct_1 = ttk.Label(self.btnframe2,text="1")
        self.freq_lbl_oct_2 = ttk.Label(self.btnframe2,text="2")
        self.freq_lbl_oct_3 = ttk.Label(self.btnframe2,text="3")
        self.freq_lbl_oct_4 = ttk.Label(self.btnframe2,text="4")
        self.freq_lbl_oct_5 = ttk.Label(self.btnframe2,text="5")
        self.freq_lbl_oct_6 = ttk.Label(self.btnframe2,text="6")
        self.freq_lbl_oct_7 = ttk.Label(self.btnframe2,text="7")
        self.freq_lbl_oct_8 = ttk.Label(self.btnframe2,text="8")
        self.freq_lbl_oct_9 = ttk.Label(self.btnframe2,text="9")
        self.freq_lbl_oct_10 = ttk.Label(self.btnframe2,text="10")
        # }}}1

        # {{{1 layout note frequency labels
        self.freq_lbl_note_C.grid(column=0,row=1)
        self.freq_lbl_note_Cs.grid(column=0,row=2)
        self.freq_lbl_note_D.grid(column=0,row=3)
        self.freq_lbl_note_Ds.grid(column=0,row=4)
        self.freq_lbl_note_E.grid(column=0,row=5)
        self.freq_lbl_note_F.grid(column=0,row=6)
        self.freq_lbl_note_Fs.grid(column=0,row=7)
        self.freq_lbl_note_G.grid(column=0,row=8)
        self.freq_lbl_note_Gs.grid(column=0,row=9)
        self.freq_lbl_note_A.grid(column=0,row=10)
        self.freq_lbl_note_As.grid(column=0,row=11)
        self.freq_lbl_note_B.grid(column=0,row=12)

        self.freq_lbl_oct_0.grid(column=1,row=0)
        self.freq_lbl_oct_1.grid(column=2,row=0)
        self.freq_lbl_oct_2.grid(column=3,row=0)
        self.freq_lbl_oct_3.grid(column=4,row=0)
        self.freq_lbl_oct_4.grid(column=5,row=0)
        self.freq_lbl_oct_5.grid(column=6,row=0)
        self.freq_lbl_oct_6.grid(column=7,row=0)
        self.freq_lbl_oct_7.grid(column=8,row=0)
        self.freq_lbl_oct_8.grid(column=9,row=0)
        self.freq_lbl_oct_9.grid(column=10,row=0)
        self.freq_lbl_oct_10.grid(column=11,row=0)
        # }}}1

        # {{{1 layout note frequency buttons
        self.freq_btn_oct_0_note_C.grid( column=1, row=1)
        self.freq_btn_oct_0_note_Cs.grid(column=1, row=2)
        self.freq_btn_oct_0_note_D.grid( column=1, row=3)
        self.freq_btn_oct_0_note_Ds.grid(column=1, row=4)
        self.freq_btn_oct_0_note_E.grid( column=1, row=5)
        self.freq_btn_oct_0_note_F.grid( column=1, row=6)
        self.freq_btn_oct_0_note_Fs.grid(column=1, row=7)
        self.freq_btn_oct_0_note_G.grid( column=1, row=8)
        self.freq_btn_oct_0_note_Gs.grid(column=1, row=9)
        self.freq_btn_oct_0_note_A.grid( column=1, row=10)
        self.freq_btn_oct_0_note_As.grid(column=1, row=11)
        self.freq_btn_oct_0_note_B.grid( column=1, row=12)

        self.freq_btn_oct_1_note_C.grid( column=2, row=1)
        self.freq_btn_oct_1_note_Cs.grid(column=2, row=2)
        self.freq_btn_oct_1_note_D.grid( column=2, row=3)
        self.freq_btn_oct_1_note_Ds.grid(column=2, row=4)
        self.freq_btn_oct_1_note_E.grid( column=2, row=5)
        self.freq_btn_oct_1_note_F.grid( column=2, row=6)
        self.freq_btn_oct_1_note_Fs.grid(column=2, row=7)
        self.freq_btn_oct_1_note_G.grid( column=2, row=8)
        self.freq_btn_oct_1_note_Gs.grid(column=2, row=9)
        self.freq_btn_oct_1_note_A.grid( column=2, row=10)
        self.freq_btn_oct_1_note_As.grid(column=2, row=11)
        self.freq_btn_oct_1_note_B.grid( column=2, row=12)

        self.freq_btn_oct_2_note_C.grid( column=3, row=1)
        self.freq_btn_oct_2_note_Cs.grid(column=3, row=2)
        self.freq_btn_oct_2_note_D.grid( column=3, row=3)
        self.freq_btn_oct_2_note_Ds.grid(column=3, row=4)
        self.freq_btn_oct_2_note_E.grid( column=3, row=5)
        self.freq_btn_oct_2_note_F.grid( column=3, row=6)
        self.freq_btn_oct_2_note_Fs.grid(column=3, row=7)
        self.freq_btn_oct_2_note_G.grid( column=3, row=8)
        self.freq_btn_oct_2_note_Gs.grid(column=3, row=9)
        self.freq_btn_oct_2_note_A.grid( column=3, row=10)
        self.freq_btn_oct_2_note_As.grid(column=3, row=11)
        self.freq_btn_oct_2_note_B.grid( column=3, row=12)

        self.freq_btn_oct_3_note_C.grid( column=4, row=1)
        self.freq_btn_oct_3_note_Cs.grid(column=4, row=2)
        self.freq_btn_oct_3_note_D.grid( column=4, row=3)
        self.freq_btn_oct_3_note_Ds.grid(column=4, row=4)
        self.freq_btn_oct_3_note_E.grid( column=4, row=5)
        self.freq_btn_oct_3_note_F.grid( column=4, row=6)
        self.freq_btn_oct_3_note_Fs.grid(column=4, row=7)
        self.freq_btn_oct_3_note_G.grid( column=4, row=8)
        self.freq_btn_oct_3_note_Gs.grid(column=4, row=9)
        self.freq_btn_oct_3_note_A.grid( column=4, row=10)
        self.freq_btn_oct_3_note_As.grid(column=4, row=11)
        self.freq_btn_oct_3_note_B.grid( column=4, row=12)

        self.freq_btn_oct_4_note_C.grid( column=5, row=1)
        self.freq_btn_oct_4_note_Cs.grid(column=5, row=2)
        self.freq_btn_oct_4_note_D.grid( column=5, row=3)
        self.freq_btn_oct_4_note_Ds.grid(column=5, row=4)
        self.freq_btn_oct_4_note_E.grid( column=5, row=5)
        self.freq_btn_oct_4_note_F.grid( column=5, row=6)
        self.freq_btn_oct_4_note_Fs.grid(column=5, row=7)
        self.freq_btn_oct_4_note_G.grid( column=5, row=8)
        self.freq_btn_oct_4_note_Gs.grid(column=5, row=9)
        self.freq_btn_oct_4_note_A.grid( column=5, row=10)
        self.freq_btn_oct_4_note_As.grid(column=5, row=11)
        self.freq_btn_oct_4_note_B.grid( column=5, row=12)

        self.freq_btn_oct_5_note_C.grid( column=6, row=1)
        self.freq_btn_oct_5_note_Cs.grid(column=6, row=2)
        self.freq_btn_oct_5_note_D.grid( column=6, row=3)
        self.freq_btn_oct_5_note_Ds.grid(column=6, row=4)
        self.freq_btn_oct_5_note_E.grid( column=6, row=5)
        self.freq_btn_oct_5_note_F.grid( column=6, row=6)
        self.freq_btn_oct_5_note_Fs.grid(column=6, row=7)
        self.freq_btn_oct_5_note_G.grid( column=6, row=8)
        self.freq_btn_oct_5_note_Gs.grid(column=6, row=9)
        self.freq_btn_oct_5_note_A.grid( column=6, row=10)
        self.freq_btn_oct_5_note_As.grid(column=6, row=11)
        self.freq_btn_oct_5_note_B.grid( column=6, row=12)

        self.freq_btn_oct_6_note_C.grid( column=7, row=1)
        self.freq_btn_oct_6_note_Cs.grid(column=7, row=2)
        self.freq_btn_oct_6_note_D.grid( column=7, row=3)
        self.freq_btn_oct_6_note_Ds.grid(column=7, row=4)
        self.freq_btn_oct_6_note_E.grid( column=7, row=5)
        self.freq_btn_oct_6_note_F.grid( column=7, row=6)
        self.freq_btn_oct_6_note_Fs.grid(column=7, row=7)
        self.freq_btn_oct_6_note_G.grid( column=7, row=8)
        self.freq_btn_oct_6_note_Gs.grid(column=7, row=9)
        self.freq_btn_oct_6_note_A.grid( column=7, row=10)
        self.freq_btn_oct_6_note_As.grid(column=7, row=11)
        self.freq_btn_oct_6_note_B.grid( column=7, row=12)

        self.freq_btn_oct_7_note_C.grid( column=8, row=1)
        self.freq_btn_oct_7_note_Cs.grid(column=8, row=2)
        self.freq_btn_oct_7_note_D.grid( column=8, row=3)
        self.freq_btn_oct_7_note_Ds.grid(column=8, row=4)
        self.freq_btn_oct_7_note_E.grid( column=8, row=5)
        self.freq_btn_oct_7_note_F.grid( column=8, row=6)
        self.freq_btn_oct_7_note_Fs.grid(column=8, row=7)
        self.freq_btn_oct_7_note_G.grid( column=8, row=8)
        self.freq_btn_oct_7_note_Gs.grid(column=8, row=9)
        self.freq_btn_oct_7_note_A.grid( column=8, row=10)
        self.freq_btn_oct_7_note_As.grid(column=8, row=11)
        self.freq_btn_oct_7_note_B.grid( column=8, row=12)

        self.freq_btn_oct_8_note_C.grid( column=9, row=1)
        self.freq_btn_oct_8_note_Cs.grid(column=9, row=2)
        self.freq_btn_oct_8_note_D.grid( column=9, row=3)
        self.freq_btn_oct_8_note_Ds.grid(column=9, row=4)
        self.freq_btn_oct_8_note_E.grid( column=9, row=5)
        self.freq_btn_oct_8_note_F.grid( column=9, row=6)
        self.freq_btn_oct_8_note_Fs.grid(column=9, row=7)
        self.freq_btn_oct_8_note_G.grid( column=9, row=8)
        self.freq_btn_oct_8_note_Gs.grid(column=9, row=9)
        self.freq_btn_oct_8_note_A.grid( column=9, row=10)
        self.freq_btn_oct_8_note_As.grid(column=9, row=11)
        self.freq_btn_oct_8_note_B.grid( column=9, row=12)

        self.freq_btn_oct_9_note_C.grid( column=10, row=1)
        self.freq_btn_oct_9_note_Cs.grid(column=10, row=2)
        self.freq_btn_oct_9_note_D.grid( column=10, row=3)
        self.freq_btn_oct_9_note_Ds.grid(column=10, row=4)
        self.freq_btn_oct_9_note_E.grid( column=10, row=5)
        self.freq_btn_oct_9_note_F.grid( column=10, row=6)
        self.freq_btn_oct_9_note_Fs.grid(column=10, row=7)
        self.freq_btn_oct_9_note_G.grid( column=10, row=8)
        self.freq_btn_oct_9_note_Gs.grid(column=10, row=9)
        self.freq_btn_oct_9_note_A.grid( column=10, row=10)
        self.freq_btn_oct_9_note_As.grid(column=10, row=11)
        self.freq_btn_oct_9_note_B.grid( column=10, row=12)

        self.freq_btn_oct_10_note_C.grid( column=11, row=1)
        self.freq_btn_oct_10_note_Cs.grid(column=11, row=2)
        self.freq_btn_oct_10_note_D.grid( column=11, row=3)
        self.freq_btn_oct_10_note_Ds.grid(column=11, row=4)
        self.freq_btn_oct_10_note_E.grid( column=11, row=5)
        self.freq_btn_oct_10_note_F.grid( column=11, row=6)
        self.freq_btn_oct_10_note_Fs.grid(column=11, row=7)
        self.freq_btn_oct_10_note_G.grid( column=11, row=8)
        self.freq_btn_oct_10_note_Gs.grid(column=11, row=9)
        self.freq_btn_oct_10_note_A.grid( column=11, row=10)
        self.freq_btn_oct_10_note_As.grid(column=11, row=11)
        self.freq_btn_oct_10_note_B.grid( column=11, row=12)
        # }}}1


app = App()
app.mainloop()

