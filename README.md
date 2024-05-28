# Processamento de Sinais

Este repositório contém arquivos em Python que gerenciam uma interface Tkinter para criar e processar sinais de áudio. As principais funcionalidades incluem:

- Geração de sinais CW (Continuous Wave)
- Geração de sinais Chirp
- Cálculo e exibição do espectrograma do sinal
- Cálculo e exibição da Transformada Rápida de Fourier (FFT) do sinal
- Salvamento do sinal como um arquivo WAV

O arquivo `teste.wav` contém um exemplo de um sinal gerado com características da nota musical A4 (440 Hz).

## Execução

Para executar a aplicação, basta ter o Python instalado, clonar este repositório e executar o arquivo `main.py`, que gerencia toda a aplicação.

## Entradas

Existem cinco campos de entrada na interface:

- Frequência: obrigatório, resulta em um erro se não for adicionado
- Amplitude: opcional, padrão é 1.0
- Frequência final: obrigatório apenas para o caso de ser um Chirp, não é utilizado nos demais, padrão é 1.0
- Frequência de amostragem (fs): opcional, segue o Teorema de Nyquist, onde fs = 2 * f, porém adicionamos +1 para garantir que esteja acima do mínimo.
- Duração do sinal: opcional, padrão é 1.0

Essas entradas permitem configurar os parâmetros do sinal a ser gerado ou processado.

 ##  :woman: Desenvolvedora
 
 [<img src="https://avatars.githubusercontent.com/u/66324902?s=400&u=6d21db611880cf437c25d3e4c5445ad80a642a8f&v=4" width=115><br><sub>Isabela Assis Cardoso</sub>](https://github.com/IsabelaAC)

  
 Qualquer dúvida estou a disposição, até mais!
