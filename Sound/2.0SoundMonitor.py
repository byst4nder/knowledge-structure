# 参考一：https://www.cnblogs.com/demodashi/p/9437491.html

# import wave
import numpy as np
import pyaudio
import matplotlib.pylab as plt


def Sound_record(rec_time):
    # 定义数据流块
    CHUNK = 1024   # 一次性录音采样字节的大小
    FORMAT = pyaudio.paInt16   # 16bit编码格式
    CHANNELS = 1  # 单声道
    RATE = 44100   # 16000采样频率, 44100

    # 创建PyAudio对象，实例化
    p = pyaudio.PyAudio()

    # 创建音频流
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
    print("Start Recording...")

    frame = []  # 录制的音频流、录音缓存数组
    for i in range(0, int(RATE / CHUNK * rec_time)):
        data = stream.read(CHUNK)

        # print(type(data))   # <class 'bytes'>
        # print(len(data))
        # print(data)
        # 对于data有两种处理方式：
        # 1、https://cloud.tencent.com/developer/article/1359843
        #   将波形数据转换为数组
        #   A new 1-D array initialized from raw binary or text data in a string.
        data = np.fromstring(data, dtype=np.short)
        # print(type(data))
        # print(data.shape)
        # 将wave_data数组改为2列，行数自动匹配。在修改shape的属性时，需使得数组的总长度不变。
        data.shape = -1, 2
        # print(data.shape)
        # 将数组转置
        data = data.T
        # print(len(data))
        data = data[0][:]
        # print("data:", data)
        frame += list(data)
        # print(frame)
    c = np.fft.fft(frame) * 2 / RATE
    abs_y = np.abs(c)
    # print(abs_y[7200:7800])
    # print(len(abs_y))
    print(np.where(abs_y[800:10000] > 1200), )
    # x = np.arange(RATE)  # 频率个数
    # # half_x = x[range(int(RATE / 2))]  # 取一半区间
    # half_x = x[20:22050]  # 人的发声频率在100Hz（男低音）到10000Hz（女高音）范围内。
    # # half_y = abs_y[range(int(RATE / 2))]
    # half_y = abs_y[20:22050]
    #
    # plt.plot(half_x, half_y, 'blue')
    # plt.title('单边振幅谱(归一化)', fontsize=9, color='blue')
    #
    # plt.show()


if __name__ == '__main__':
    num = 0
    while num < 10:
        Sound_record(0.5)
        num += 1

    # Sound_record(3)
