#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 22 13:06:07 2024

Contém a definição da classe SignalGeneratorApp, que gerencia a interface gráfica e a lógica do sinal.

__init__ relaciona as entradas recebidas
get_parameters obtem os inputs e direciona para cada variável além de tratar os casos necessários

As demais recebem e enviam os parâmetros para a sua respectiva função responsável
pelo cálculo no signal_processing.py e pelo plot em plots.py

display_plot gerencia os frames e plots exibidos

@author: Isabela Assis Cardoso
"""

import tkinter as tk
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import filedialog, messagebox
from signal_processing import generate_cw_signal, generate_chirp_signal, compute_fft, compute_spectrogram
from plots import plot_signal, plot_fft, plot_spectrogram
from ui import create_param_entries, create_buttons
from scipy.io.wavfile import write


class SignalGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Signal Generator")

        self.frame_signal = tk.Frame(self.root)
        self.frame_signal.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.frame_freq = tk.Frame(self.root)
        self.frame_freq.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.param_frame = tk.Frame(self.root)
        self.param_frame.pack(side=tk.TOP, fill=tk.X)

        self.amplitude_entry, self.frequency_entry, self.freq_end_entry, self.fs_entry, self.duration_entry = create_param_entries(
            self.param_frame)

        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(side=tk.TOP, fill=tk.X)

        create_buttons(self.button_frame, self)

        self.signal = None
        self.no_signal_message = "Nenhum sinal gerado. Por favor, gere um sinal primeiro."

    def get_parameters(self):
        try:
            amplitude = float(self.amplitude_entry.get() or 1.0)
            frequency = float(self.frequency_entry.get())
            if not frequency:
                raise ValueError()

            fs = float(self.fs_entry.get() or 2 * (frequency + 1))
            if fs < 2 * frequency:
                fs = 2 * (frequency + 1)
            duration = float(self.duration_entry.get() or 1.0)
        except ValueError:
            messagebox.showerror(
                "Erro de Entrada",
                "A frequência é obrigatória.")
            return None
        return amplitude, frequency, fs, duration

    def generate_cw_signal(self):
        amplitude, frequency, fs, duration = self.get_parameters()

        t, self.signal = generate_cw_signal(amplitude, frequency, fs, duration)
        fig = plot_signal(t, self.signal)
        self.display_plot(self.frame_signal, fig)

    def generate_chirp_signal(self):
        amplitude, f0, fs, duration = self.get_parameters()
        f1 = float(self.freq_end_entry.get() or 1)

        t, self.signal = generate_chirp_signal(amplitude, f0, f1, fs, duration)
        fig = plot_signal(t, self.signal)
        self.display_plot(self.frame_signal, fig)

    def compute_fft(self):
        if self.signal is None:
            messagebox.showwarning("Aviso", self.no_signal_message)
            return
        _, _, fs, _ = self.get_parameters()

        xf, yf = compute_fft(self.signal, fs)
        fig = plot_fft(xf, yf)
        self.display_plot(self.frame_freq, fig)

    def show_spectrogram(self):
        if self.signal is None:
            messagebox.showwarning("Aviso", self.no_signal_message)
            return

        _, _, fs, _ = self.get_parameters()

        f, t, Sxx = compute_spectrogram(self.signal, fs)
        fig = plot_spectrogram(f, t, Sxx)
        self.display_plot(self.frame_freq, fig)

    def save_as_wav(self):
        if self.signal is None:
            messagebox.showwarning("Aviso", self.no_signal_message)
            return
        _, _, fs, _ = self.get_parameters()
        fs = int(round(fs))

        file_path = filedialog.asksaveasfilename(
            defaultextension=".wav", filetypes=[
                ("WAV files", "*.wav")])
        if file_path:
            write(file_path, fs, self.signal.astype(np.float32))

    def display_plot(self, frame, fig):
        for widget in frame.winfo_children():
            widget.destroy()
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
