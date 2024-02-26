# import struct

# file_path = r'C:\Users\varsh\Desktop\92f0cb6bc92577783eac306e5f50b06a.pcm'
# # Read binary PCM data from file
# with open(file_path, 'rb') as file:
#     pcm_data = file.read()

# # Convert PCM data to words
# words = [struct.unpack('<h', pcm_data[i:i+2])[0] for i in range(0, len(pcm_data), 2)]

# # Print the result
# print(words)

import wave
import struct

# Input PCM file path
# input_pcm_path = r'output.pcm'
# input_pcm_path = r'C:\Users\varsh\Desktop\92f0cb6bc92577783eac306e5f50b06a.pcm'
input_pcm_path = "output.pcm"

# Output WAV file path
output_wav_path = 'output.wav'

# Read binary PCM data from file
with open(input_pcm_path, 'rb') as file:
    pcm_data = file.read()

# Create a WAV file
with wave.open(output_wav_path, 'w') as wav_file:
    wav_file.setnchannels(1)  # 1 channel for mono, 2 channels for stereo
    wav_file.setsampwidth(2)  # 16-bit PCM
    wav_file.setframerate(44100)  # Adjust based on your desired sample rate
    wav_file.writeframes(pcm_data)

print(f"WAV file '{output_wav_path}' created successfully.")
