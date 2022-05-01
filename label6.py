import binascii
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

width, height = 304, 135

########################### Resize Logo ######################################
newWidth = 100
img = Image.open('logo.jpg')
wpercent = (newWidth / float(img.size[0]))
hsize = int((float(img.size[1]) * float(wpercent)))
img = img.resize((newWidth, 100), Image.ANTIALIAS)
img.save('newlogo2.jpg')


########################### Design Label 6 ######################################
def getLabel():
    img_bg = Image.new('1', (width, height), 1)
    texts = ['Certified to CSA Std.', 'C22.2 No.24', 'Conforms to UL Std. 873']
    serialNum = '5022814'
    draw = ImageDraw.Draw(img_bg)
    font1 = ImageFont.truetype('arialbd.ttf', 17)

    xspace = 5
    yspace = 40
    draw.text((xspace, 7), texts[0], 0, font=font1)
    draw.text((xspace, 7 + yspace), texts[1], 0, font=font1)
    draw.text((xspace, 7 + yspace * 2), texts[2], 0, font=font1)

    draw.text((215, 110), serialNum, 0, font=font1)  # number under logo
    return img_bg


########################### Convert the generated pixel values (0,255) >> (1,0) ######################################
def conv_list(l):
    a = ''
    for i in l:
        if i == 0:
            a = a + '1'
        else:
            a = a + '0'
    return a


########################### Generate the Binary file ######################################
def createBinary(imgname):
    im = Image.open(f'{imgname}.png')
    pixels = list(im.getdata())
    width, height = im.size
    pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
    newFile = open(imgname, "wb")
    for k in pixels:
        c = conv_list(k)
        hstr = '%0*X' % ((len(c) + 3) // 4, int(c, 2))
        newFile.write(binascii.unhexlify(''.join(hstr.split())))


if __name__ == '__main__':
    label = getLabel()
    labelName = 'label6'

    logo = Image.open('newlogo2.jpg')
    pos = (width - logo.width - 5, 0)
    label.paste(logo, pos)
    label.save(f'{labelName}.png', format='png')
    createBinary(f'{labelName}')
