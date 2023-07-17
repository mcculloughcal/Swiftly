import pyaudio
import wave

format = pyaudio.paInt16

channels = 1
rate = 44100
chunk = 1024
seconds = 5

audio = pyaudio.PyAudio()

# start Recording
stream = audio.open(format=format, channels=channels,
            rate=rate, input=True,
            frames_per_buffer=chunk)
print("recording...")
frames = []

for i in range(0, int(rate / chunk * seconds)):
    data = stream.read(chunk)
    frames.append(data)
print("finished recording")


# stop Recording
stream.stop_stream()
stream.close()
audio.terminate()

'''
# create binary file from recording
file = open('newFile.mp3', "wb")
file.write((b''.join(frames)))
file.close()
'''

# create wav from recording
file = wave.open('newWav.wav', 'wb')
file.setnchannels(channels)
file.setsampwidth(audio.get_sample_size(format))
file.setframerate(rate)
file.writeframes(b''.join(frames))
file.close
