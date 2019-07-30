import wave
import numpy as np
# import soundfile as sf
from scipy.io import wavfile
import matplotlib.pyplot as plt

"""
		本文件可有写成一个函数，直接调用更方便。
		输入时一个文件，直接绘图，直接提取信息，返回变量运算等。
		
"""
wav_path = "./a.wav"
with wave.open(wav_path, "rb") as f:
	print(f.getparams())
	print(f.getparams()[:4])

frames_num = f.getparams().nframes     # 总帧数
frequency = f.getparams().framerate  # 采样频率  1秒钟采样帧数。
sample_time = 1 / frequency    # 采样时间间隔，一帧的时长
time = frames_num / frequency     # 采样总数除以采样速度等于时长
print("frames_num:", frames_num)
print("frequency:", frequency)
print(time)

# 可以使用scipy.io.wavfile.read(somefile)来读取.wav音频文件。
# 它会返回一个元组，第一项为音频的采样率，第二项为音频数据的numpy数组。
sample_frequency, audio_sequence = wavfile.read(wav_path)
print("sample_frequency:", sample_frequency)
print("audio_sequence:", audio_sequence)

# 也可以使用PySoundFile，它也是返回一个元组，指示第一项为数据，第二项为采样率。
# data, samplerate = sf.read('a.wav')


# 绘图：
x_seq = np.arange(0, time, sample_time)

plt.plot(x_seq, audio_sequence, "blue")
plt.xlabel("time(s)")
plt.show()
