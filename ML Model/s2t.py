import struct
import wave
import librosa
import soundfile as sf
from pvcheetah import CheetahActivationLimitError, create


def s2t(path):

    aud,_=librosa.load(path,sr=16000,mono=True)
    sf.write("temp.wav",aud,16000)

    o = create(
        access_key="insert your API key here",
        enable_automatic_punctuation=True)

    try:
        with wave.open("temp.wav", 'rb') as f:
            if f.getframerate() != o.sample_rate:
                raise ValueError(
                    "invalid sample rate of `%d`. cheetah only accepts `%d`" % (f.getframerate(), o.sample_rate))
            if f.getnchannels() != 1:
                raise ValueError("this demo can only process single-channel WAV files")
            if f.getsampwidth() != 2:
                raise ValueError("this demo can only process 16-bit WAV files")

            buffer = f.readframes(f.getnframes())
            audio = struct.unpack('%dh' % (len(buffer) / struct.calcsize('h')), buffer)

        num_frames = len(audio) // o.frame_length
        transcript = ''
        for i in range(num_frames):
            frame = audio[i * o.frame_length:(i + 1) * o.frame_length]
            partial_transcript, _ = o.process(frame)
            print(partial_transcript, end='', flush=True)
            transcript += partial_transcript

        final_transcript = o.flush()
        print(final_transcript)

    except CheetahActivationLimitError:
        print('AccessKey has reached its processing limit.')
    finally:
        o.delete()
    
    return final_transcript


if __name__=="__main__":
    path="Recording (2).wav"
    s2t(path)
