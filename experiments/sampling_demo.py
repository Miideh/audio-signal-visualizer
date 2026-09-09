print("Sampling experiment started")

import numpy as np
import matplotlib.pyplot as plt


frequency = 5
duration = 1


# High sampling rate
high_sampling_rate = 100

t_high = np.linspace(0, duration, high_sampling_rate)

signal_high = np.sin(2 * np.pi * frequency * t_high)


# Low sampling rate
low_sampling_rate = 8

t_low = np.linspace(0, duration, low_sampling_rate)

signal_low = np.sin(2 * np.pi * frequency * t_low)


plt.figure(figsize=(10,4))

plt.plot(
    t_high,
    signal_high,
    label="High Sampling Rate (100 samples/sec)"
)

plt.scatter(
    t_low,
    signal_low,
    label="Low Sampling Rate (8 samples/sec)"
)


plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.title("Effect of Sampling Rate on Signal Representation")

plt.grid(True)
plt.legend()

plt.show()