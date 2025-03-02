# this script turns the monstrous 7 column sim output to freq, mag_dbs csv that we can plot in desmos on the ipad

import numpy as np
import matplotlib.pyplot as plt

# load the data from file (whitespace delimited)
data = np.loadtxt("rc_lpf_data.csv")

# time freq 0 time mag_db time phase_deg
freq = data[:, 1]      # Frequency (Hz)
mag_db = data[:, 4]    # Magnitude (dB)

# sort data by frequency in case its not
sorted_indices = np.argsort(freq)
freq = freq[sorted_indices]
mag_db = mag_db[sorted_indices]

# save to csv
output_data = np.column_stack((freq, mag_db))
np.savetxt("freq_mag_for_desmos.csv", output_data, delimiter=",", comments="", fmt="%.6f")

print("CSV file 'freq_mag_for_desmos.csv' saved successfully!")

# Plot Bode Magnitude
plt.figure()
plt.semilogx(freq, mag_db, label="Magnitude")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude (dB)")
plt.title("Bode Plot - Magnitude")
plt.grid(True, which="both")
plt.legend()

plt.show()
