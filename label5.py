import binascii
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


########################### Design Label 5 ######################################
def getLabel():
    width, height = 304,135
    img_bg = Image.new('1', (width, height), 1)
    texts = ['Warning', 'intended for 24V supply connections and 40V max control circuits only', 'Advertisment', "Destiné aux connexions d'alimentation 24V et aux circuits de",'commande 40V max uniquement']
    draw = ImageDraw.Draw(img_bg)
    font1 = ImageFont.truetype('arialbd.ttf', 18)
    font2 = ImageFont.truetype('arial', 9)
    draw.text((width/2, 22), texts[0],0, font=font1, anchor="mm")

    xspace = 110
    yspace = 20
    draw.text((width/2, 22 + yspace), texts[1], 0, font=font2, anchor="mm")
    draw.text((width/2, 30 + yspace * 2), texts[2], 0, font=font1, anchor="mm")
    draw.text((width/2, 30 + yspace * 3), texts[3], 0, font=font2, anchor="mm")
    draw.text((width/2, 30 + yspace * 3.7), texts[4], 0, font=font2, anchor="mm")
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
        ###########################################################
        c = conv_list(k)
        hstr = '%0*X' % ((len(c) + 3) // 4, int(c, 2))
        # print(bytearray(hstr,encoding='utf-8'))
        newFileByteArray = bytearray(hstr, encoding='utf-8')
        # newFile.write(newFileByteArray)
        newFile.write(binascii.unhexlify(''.join(hstr.split())))

if __name__ == '__main__':

    label = getLabel()
    labelName = 'label5'
    label.save(f'{labelName}.png', format='png')
    createBinary(f'{labelName}')