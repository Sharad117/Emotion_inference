import wave
import array

# Input WAV file path (replace with your file path)
input_wav_path = r'Help.wav'

# Output PCM file path
output_pcm_path = 'output.pcm'

# Desired sample rate
desired_sample_rate = 48000  # replace with your desired sample rate

# Read the WAV file
with wave.open(input_wav_path, 'rb') as wav_file:
    # Get parameters of the original audio file
    sample_width = wav_file.getsampwidth()
    num_channels = wav_file.getnchannels()
    original_sample_rate = wav_file.getframerate()
    num_frames = wav_file.getnframes()
    print("sample width ", sample_width)
    print("num channels ", num_channels)    
    print("original sample rate ", original_sample_rate)
    print("num frames ", num_frames)


    # Read audio data
    audio_data = wav_file.readframes(num_frames)

# Set the desired sample rate
if original_sample_rate != desired_sample_rate:
    # If the sample rate is different, resample the audio data
    audio_data_array = array.array('h', audio_data)
    audio_data_array.byteswap()  # adjust for little-endian or big-endian

    # Resample using the desired sample rate
    new_num_frames = int(num_frames * desired_sample_rate / original_sample_rate)
    audio_data_array = audio_data_array[:new_num_frames]

    # Update the number of frames
    num_frames = new_num_frames

    # Convert back to bytes
    audio_data = audio_data_array.tobytes()

# Write PCM data to file
with open(output_pcm_path, 'wb') as pcm_file:
    pcm_file.write(audio_data)
