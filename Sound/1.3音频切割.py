import os
import sys
import pandas
from scipy.io import wavfile
from python_speech_features.base import mfcc
from pydub.audio_segment import AudioSegment


# 音频的截取，通过时间片段来获取部分音频
# 因为音频以毫秒计时，在截取音频时，统统转为了毫秒
AudioSegment.converter = r'../../software/ffmpeg/bin/ffmpeg.exe'
# song = AudioSegment.from_file('./a.MP3', format='MP3')  # 测试只支持wav格式，不支持MP3
sound = AudioSegment.from_mp3("a.wav")    # 测试只支持wav格式，不支持MP3
part = sound[21500:100000]
part.export("./part.wav", format="wav")
print(sound)


# 比较大的音频文件，将分钟和秒进行结合，然后在自己拆分
def segeS(start_time, end_time):
	start_time = (int(start_time.split(":")[0])*60 + int(start_time.split(":")[1])) * 1000
	end_time = (int(end_time.split(':')[0])*60+int(end_time.split(':')[1]))*1000
	# 格式
	# start_time = "0:35"
	# end_time = "0:38"

# https://blog.csdn.net/xuqingda/article/details/86540333
# python+ffmpeg实现wav文件切割
# 单文件切割成小文件，这样实现了数据容量的扩增。

import os
def audio_cut(audio_in_path, audio_out_path, start_time, dur_time):
    """
    :param audio_in_path: 输入音频的绝对路径
    :param audio_out_path: 切分后输出音频的绝对路径
    :param start_time: 切分开始时间
    :param dur_time: 切分持续时间
    :return:
    """

	os.system(
		"ffmpeg -i {in_path} -vn -acodec copy -ss {Start_time} -t {Dur_time} {out_path}".format(
			in_path=audio_in_path,
			out_path=audio_out_path,
			Start_time=start_time,
			Dur_time=dur_time
			)
		)

