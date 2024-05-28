#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 27 18:08:11 2024

Contém funções auxiliares para criar componentes da interface do usuário, como entradas de parâmetros e botões.

@author: isa
"""

import tkinter as tk


def create_param_entries(param_frame):
    tk.Label(param_frame, text="Amplitude:").grid(row=0, column=0)
    amplitude_entry = tk.Entry(param_frame)
    amplitude_entry.grid(row=0, column=1)

    tk.Label(param_frame,
             text="Frequência (CW) / Frequência Inicial (Chirp) (Hz):").grid(row=1,
                                                                             column=0)
    frequency_entry = tk.Entry(param_frame)
    frequency_entry.grid(row=1, column=1)

    tk.Label(
        param_frame,
        text="Frequência Final (Chirp) (Hz):").grid(
        row=2,
        column=0)
    freq_end_entry = tk.Entry(param_frame)
    freq_end_entry.grid(row=2, column=1)

    tk.Label(
        param_frame,
        text="Frequência de amostragem (Hz):").grid(
        row=3,
        column=0)
    fs_entry = tk.Entry(param_frame)
    fs_entry.grid(row=3, column=1)

    tk.Label(param_frame, text="Duração (s):").grid(row=4, column=0)
    duration_entry = tk.Entry(param_frame)
    duration_entry.grid(row=4, column=1)

    return amplitude_entry, frequency_entry, freq_end_entry, fs_entry, duration_entry


def create_buttons(button_frame, app):
    tk.Button(
        button_frame,
        text="Generate CW Signal",
        command=app.generate_cw_signal).pack(
        side=tk.LEFT)
    tk.Button(
        button_frame,
        text="Generate Chirp Signal",
        command=app.generate_chirp_signal).pack(
        side=tk.LEFT)
    tk.Button(
        button_frame,
        text="Compute FFT",
        command=app.compute_fft).pack(
        side=tk.LEFT)
    tk.Button(
        button_frame,
        text="Show Spectrogram",
        command=app.show_spectrogram).pack(
        side=tk.LEFT)
    tk.Button(
        button_frame,
        text="Save as WAV",
        command=app.save_as_wav).pack(
        side=tk.LEFT)
