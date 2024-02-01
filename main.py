import numpy as np
import soundfile as sf

def read_bin(filename):
    with open(filename, 'rb') as file:
        binary_data = file.read()

    return ''.join(format(byte, '08b') for byte in binary_data)

def save_audio(wave, sample_rate, filename):
    sf.write(filename, wave, sample_rate)

data = read_bin("input.txt")

length = len(data)
frequency = 2000.0
sample_rate = 44100
bit_duration = 0.1
duration = bit_duration * length
print(f"duration = {duration}")

t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
carrier_wave = np.sin(2 * np.pi * frequency * t)
wave = np.zeros_like(t)

for i, bit in enumerate(data):
    if bit == '1':
        start_index = i * int(sample_rate * bit_duration)
        end_index = (i+1) * int(sample_rate * bit_duration)
        wave[start_index:end_index] = carrier_wave[0:(end_index - start_index)]

save_audio(wave, sample_rate, "output.wav")
