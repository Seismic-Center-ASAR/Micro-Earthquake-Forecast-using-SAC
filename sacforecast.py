import numpy as np
from obspy import read
import matplotlib.pyplot as plt
import time

while True:
    # Read the SAC file
    st = read("data.sac")
    
    # Compute the PSD for the first trace
    trace = st[0]
    npts = trace.stats.npts
    sampling_rate = trace.stats.sampling_rate
    psd = np.abs(np.fft.rfft(trace.data, n=npts))**2 / (sampling_rate * npts)

    # Compute the corresponding frequency array
    freqs = trace.stats.sac['delta'] * np.arange(npts // 2 + 1)

    # Estimate the remaining time until the next frequency variation
    threshold = 1  # dB/Hz
    above_threshold = np.where(10 * np.log10(psd) > threshold)[0]
    if len(above_threshold) > 0:
        remaining_time = 1 / freqs[above_threshold[0]]
        print("Remaining time until the next frequency variation:", remaining_time, "seconds")
    else:
        remaining_time = np.nan
        print("No frequency variation above the threshold detected.")
    
    # Plot the PSD
    plt.clf()
    plt.semilogx(freqs, 10 * np.log10(psd))
    plt.xlabel("Frequency [Hz]")
    plt.ylabel("Power/Frequency [dB/Hz]")
    plt.title("Remaining time to next event: {:.2f} seconds".format(remaining_time))
    plt.suptitle("Power Spectral Density and Earthquake Forecast")
    plt.pause(2)

