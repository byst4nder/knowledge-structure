# 参考：https://blog.csdn.net/qq_40878431/article/details/82941982
import PIL.Image as Image


img = Image.open("1.png")
img = img.convert("RGBA")    # 图片转换为四通道。第四个通道就是我们要修改的透明度。
L, H = img.size
color_0 = img.getpixel((0, 0))   # 返回图片某个坐标点颜色。
print(color_0)
for h in range(H):
    for l in range(L):
        dot = (l, h)
        color_1 = img.getpixel(dot)
        if color_1 == color_0:
            color_1 = color_1[:-1]+(0,)
            img.putpixel(dot, color_1)  # 修改此坐标点的颜色，没有返回值，直接修改img
img.save("output.png")
