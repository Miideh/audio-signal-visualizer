# Signal Laboratory #001

## Experiment: Changing Sine Wave Parameters

## Objective

Understand how frequency, amplitude, and sampling rate affect the digital representation of a signal.

## Tools

- Python
- NumPy
- Matplotlib

---

# Frequency

Frequency controls how many cycles occur per second.

## Change

Tested different frequency values:

- 5Hz
- 10Hz
- 20Hz

## Observation

- Higher frequency produced more oscillations within the same time period.
- The signal changed faster.
- Amplitude remained constant.

---

# Amplitude

Amplitude controls the strength or magnitude of the signal.

## Change

Increased amplitude values:

- A = 1
- A = 3

## Observation

- Higher amplitude produced a taller waveform.
- Signal strength increased.
- Frequency remained unchanged.

---

# Sampling Rate

Sampling rate determines how many measurements are taken from a continuous signal per second.

## Change

Compared different sampling rates:

- High sampling rate: 200 samples/sec
- Low sampling rate: 8 samples/sec

## Observation

- Higher sampling rates produced more sample points.
- The digital representation was closer to the original waveform.
- Lower sampling rates caused loss of signal detail.

---

# Engineering Insight

A computer does not store the original continuous signal.

It stores measurements of that signal.

The sampling rate affects how accurately the physical signal can be represented digitally.

This conversion from signal → numbers is the first step before data becomes arrays, tensors, and eventually AI computations.
