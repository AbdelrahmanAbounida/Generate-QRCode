import binascii
import qrcode
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

inpt = "00000000000000000000000000000"

########################### Create QRcode ######################################
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=4,
    border=0
)
qr.add_data(inpt)
qr.make(fit=True)
imgQR = qr.make_image(fill_color="black", back_color="white")


########################### Design Label 3 ######################################
def getLabel():
    img_bg = Image.new('1', (304, 135), 1)
    texts = ['ENA SOLUTION INC', 'ENASTAT GEN2 WALL MOUNTED', '24VAC 60Hz AC 1ph 12.5A', 'Software: 000.001.000']
    draw = ImageDraw.Draw(img_bg)
    font = ImageFont.truetype('arialbd.ttf', 17)
    draw.text((4, 105), inpt, 0, font=font)
    font = ImageFont.truetype('arialbd.ttf', 12)
    xspace = 110
    yspace = 25
    draw.text((xspace, 5), texts[0], 0, font=font)
    draw.text((xspace, 5 + yspace), texts[1], 0, font=font)
    draw.text((xspace, 5 + yspace * 2), texts[2], 0, font=font)
    draw.text((xspace, 5 + yspace * 3), texts[3], 0, font=font)

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
    pos = (5, 5)
    label = getLabel()
    label.paste(imgQR, pos)
    labelName = 'label3'
    label.save(f'{labelName}.png', format='png')
    createBinary(f'{labelName}')
