from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random
import matplotlib.pyplot as plt
import time
import threading

def rzm():
    '''随机生成字母，chr() 用一个范围在 range（256）内的（就是0～255）整数作参数，返回一个对应的字符。'''
    a = random.randint(0,1)
    if a==0:
        return chr(random.randint(65,90))
    else:
        return chr(random.randint(97,122))

#生成颜色不完全是随机的，我们将背景设置得比字母要深一些
def bjys():
    '''随机生成验证码背景颜色'''
    return(random.randint(64,255),random.randint(64,255),random.randint(64,255))
def zmys():
    '''随机生成字母颜色'''
    return(random.randint(32,127),random.randint(32,127),random.randint(32,127))

def zx():
    '''随机生成字形，有四种选择'''
    b = random.randint(0,3)
    if b == 0:
        font = ImageFont.truetype('AslinaBold-2.otf',40)
    elif b == 1:
        font = ImageFont.truetype('Guard-2.ttf',40)
    elif b == 2:
        font = ImageFont.truetype('Restu-Bundah-2.otf',40)
    else :
        font = ImageFont.truetype('Please-2.otf',40)
    return(font)


while True:
    # 设置验证码的大小240x60
    width = 240
    height = 60
    image = Image.new('RGB', (width, height), (255, 255, 255))  # Image.new(mode,size,color)生成一个新的图像
    # 创建画图对象
    draw = ImageDraw.Draw(image)

    # 填充背景
    for i in range(width):
        for j in range(height):
            draw.point((i, j), fill=bjys())
    # 设置一个存储字母的列表
    list = []
    # 填充字体
    for t in range(4):
        RZM=rzm()
        draw.text((60 * t + 10, 10),RZM, font=zx(), fill=zmys())  # 第一个参数是调节位置
        list.append(RZM)
    word = list[0]+list[1]+list[2]+list[3]
    print(word)  #输出验证码便于测试

    # 进行模糊处理
    #image = image.filter(ImageFilter.BLUR)
    # 画图
    plt.imshow(image)
    plt.axis("off")
    plt.show()
    WORD = input('请输入验证码： ')
    if WORD == word:
        print('太棒了！ 你输入准确！')
        break
    else:
        print("你好菜噢，这都错了，重新输入！")














