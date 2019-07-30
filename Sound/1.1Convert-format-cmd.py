import os
import subprocess


in_file = "./a.mp3"
out_file = "./a.wav"


def convert2wav(in_path, out_path):
	path, name = os.path.split(in_path)
	if name.split(".")[-1] != "mp3":
		print("not a mp3 file.")
		return 0
	if out_path is None or out_file.split(".")[-1] != "wav":
		out_path = os.path.join(path, name.split('.')[0] + ".wav")
	# ffmpeg -i input.mp3 output.wav   此处应该将ffmpeg的安装包支持调用路径写明。根据环境来变动。
	cmd_msg = subprocess.call(["../../software/ffmpeg/bin/ffmpeg", '-i', in_path, out_path])
	print(cmd_msg)
	if cmd_msg:
		return 0
	print("Success")
	return out_path


if __name__ == '__main__':
	convert2wav(in_file, out_file)
