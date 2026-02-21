import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

st.set_page_config(page_title="ZGL NeuroVision Demo", layout="wide")

st.title("ZGL NeuroVision - Cardio Analysis Demo")
st.markdown("Muhammed Ekrem Özer tarafından geliştirilmiştir.")

# Simulated PPG signal
fs = 100  # sampling frequency
t = np.linspace(0, 10, fs*10)
heart_rate = 75
signal = 0.6 * np.sin(2 * np.pi * heart_rate/60 * t) + 0.05 * np.random.randn(len(t))

# Peak detection
peaks, _ = find_peaks(signal, distance=fs*(60/heart_rate)/2)
rr_intervals = np.diff(peaks) / fs

if len(rr_intervals) > 0:
    bpm = 60 / np.mean(rr_intervals)
    hrv = np.std(rr_intervals)
else:
    bpm = 0
    hrv = 0

# Risk evaluation
if bpm > 100:
    risk = "Tachycardia Risk"
elif bpm < 50:
    risk = "Bradycardia Risk"
else:
    risk = "Normal Range"

col1, col2, col3 = st.columns(3)
col1.metric("BPM", f"{bpm:.1f}")
col2.metric("HRV", f"{hrv:.4f}")
col3.metric("Status", risk)

fig, ax = plt.subplots()
ax.plot(t, signal)
ax.plot(t[peaks], signal[peaks], "ro")
ax.set_title("Simulated PPG Signal")
st.pyplot(fig)
