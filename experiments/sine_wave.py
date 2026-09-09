print("Sine wave script started")

import numpy as np
import matplotlib.pyplot as plt


frequency = 7
sampling_rate = 200
duration = 2


t = np.linspace(0, duration, sampling_rate)

amplitude = 3

signal = amplitude * np.sin(2*np.pi*frequency*t)

plt.figure(figsize=(10, 4))

plt.plot(t, signal)

plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.title(f"{frequency}Hz Sine Wave")
plt.grid(True)

plt.show(block=True)