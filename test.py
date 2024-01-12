import speech_2_text
# Example usage:
# converter = Conversion()
# converter.speech('path/to/your/audio/file.wav')
instance1= speech_2_text.Conversion()
label,conf =instance1.speech('sample2.mp3')

print(label, conf)
