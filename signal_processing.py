#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 27 18:06:17 2024

Contém funções para o processamento de sinal, incluindo geração de sinais CW e Chirp, cálculo da FFT e do espectrograma.


@author: Isabela Assis Cardoso
"""

import numpy as np
from scipy.fft import fft, fftfreq
from scipy.signal import chirp, spectrogram

def generate_cw_signal(amplitude, frequency, fs, duration):
    t = np.linspace(0, duration, int(fs), endpoint=False)
    signal = amplitude * np.sin(2 * np.pi * frequency * t)
    return t, signal

def generate_chirp_signal(amplitude, f0, f1, fs, duration):
    t = np.linspace(0, duration, int(fs), endpoint=False)
    signal =  amplitude * chirp(t, f0=f0, f1=f1, t1=duration, method='linear')
    return t, signal

def compute_fft(signal, fs):
    N = len(signal)
    T = 1.0 / fs
    yf = fft(signal)
    xf = fftfreq(N, T)[:N//2]
    return xf, 2.0/N * np.abs(yf[0:N//2])

def compute_spectrogram(signal, fs):
    nperseg = min(256, len(signal))
    f, t, Sxx = spectrogram(signal, fs, nperseg=nperseg)
    return f, t, Sxx
