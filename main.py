#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 22 13:00:06 2024

Ponto de entrada da aplicação. Inicializa a janela Tkinter e instancia a classe SignalGeneratorApp.

@author:  Isabela Assis Cardoso
"""

import tkinter as tk
from app import SignalGeneratorApp

if __name__ == "__main__":
    root = tk.Tk()  # Cria a janela principal do Tkinter
    app = SignalGeneratorApp(root)  # Instancia a classe principal da aplicação
    root.mainloop()  # Inicia o loop principal da interface gráfica