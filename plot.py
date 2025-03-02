# this script was used to verify the simulation was giving us good output

import numpy as np
import matplotlib.pyplot as plt

# Load the data from file (whitespace-delimited)
data = np.loadtxt("rc_lpf_data.csv")

# columns go
# time freq 0 time mag_db time phase_deg

freq = data[:, 1]  # Frequency (Hz)
mag_db = data[:, 4]  # Magnitude (dB)
phase_deg = data[:, 6]  # Phase (degrees)

# sort by frequency and plot
sorted_indices = np.argsort(freq)
freq = freq[sorted_indices]
mag_db = mag_db[sorted_indices]
phase_deg = phase_deg[sorted_indices]

# Plot Bode Magnitude
plt.figure()
plt.semilogx(freq, mag_db, label="Magnitude")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude (dB)")
plt.title("Bode Plot - Magnitude")
plt.grid(True, which="both")
plt.legend()

# Plot Bode Phase
plt.figure()
plt.semilogx(freq, phase_deg, label="Phase", color="r")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Phase (degrees)")
plt.title("Bode Plot - Phase")
plt.grid(True, which="both")
plt.legend()

plt.show()



