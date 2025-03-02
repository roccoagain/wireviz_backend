import numpy as np
import matplotlib.pyplot as plt

# Load the data from file (whitespace-delimited)
data = np.loadtxt("output.csv")

# Export frequency and magnitude to CSV for Desmos
freq_mag_data = np.column_stack((data[:, 1], data[:, 4]))
sorted_indices = np.argsort(freq_mag_data[:, 0])
freq_mag_data = freq_mag_data[sorted_indices]
np.savetxt(
    "freq_mag_for_desmos.csv",
    freq_mag_data,
    delimiter=",",
    header="frequency,magnitude_db",
    comments="",
)

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

# Create a figure with subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

# Plot Bode Magnitude
ax1.semilogx(freq, mag_db, label="Magnitude")
ax1.set_xlabel("Frequency (Hz)")
ax1.set_ylabel("Magnitude (dB)")
ax1.set_title("Bode Plot - Magnitude")
ax1.grid(True, which="both")
ax1.legend()

# Plot Bode Phase
ax2.semilogx(freq, phase_deg, label="Phase", color="r")
ax2.set_xlabel("Frequency (Hz)")
ax2.set_ylabel("Phase (degrees)")
ax2.set_title("Bode Plot - Phase")
ax2.grid(True, which="both")
ax2.legend()

# Adjust layout
plt.tight_layout()

# Save the figure
plt.savefig("bode_plot.png", dpi=300)
print("Bode plot saved as 'bode_plot.png'")

# Uncomment to display the plot
# plt.show()
