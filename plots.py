#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 27 18:07:25 2024

Contém funções para criar gráficos usando Matplotlib, incluindo gráficos de sinal, FFT e espectrograma.

@author: Isabela Assis Cardoso
"""
import numpy as np
import matplotlib.pyplot as plt


def plot_signal(t, signal):
    fig, ax = plt.subplots()
    ax.plot(t, signal)
    ax.set(xlabel='Time (s)', ylabel='Amplitude', title='Generated Signal')
    ax.grid()
    return fig


def plot_fft(xf, yf):
    fig, ax = plt.subplots()
    ax.plot(xf, yf)
    ax.set(xlabel='Frequency (Hz)', ylabel='Magnitude', title='FFT of Signal')
    ax.grid()
    return fig


def plot_spectrogram(f, t, Sxx):
    fig, ax = plt.subplots()
    ax.pcolormesh(t, f, 10 * np.log10(Sxx), shading='gouraud')
    ax.set_ylabel('Frequency [Hz]')
    ax.set_xlabel('Time [sec]')
    ax.set_title('Spectrogram')
    return fig
